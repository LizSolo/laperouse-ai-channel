"""Проверяет, что утренний прогон действительно дошёл до конца.

Запускается по расписанию через час после редактора. Смотрит на результаты
цепочки: черновики от автора, его самопроверку по RULES.md и разбор от редактора.
Если за сегодня файл не менялся, значит прогон не состоялся или не сделал push —
и об этом нужно сообщить в Telegram, чтобы сбой не выглядел как тишина.

Самопроверка попала сюда 2026-08-05: пропущенный ШАГ 4.5 выглядит как нормальный
выпуск (посты-то пришли), поэтому его отсутствие ловится кодом, а не на глаз.

Третий статус добавлен 2026-08-06. До него сторож знал два состояния: файлы за
сегодня есть или их нет. День, когда прогон состоялся, но ни одна тема не прошла
отбор, выглядел как сбой — а это законный исход, и агент не должен выдавливать
слабый пост, лишь бы файл обновился. Такой день агент помечает сам, записывая
pipeline/no-topics.md с причинами. Файл за сегодня = спокойное уведомление вместо
тревоги; остальные три файла в этот день не проверяются, их и не должно быть.

Четвёртый статус добавлен 2026-08-11. Автор в тот день отработал полностью, но
push ушёл в свою ветку claude/*, а не в master. Сторож смотрел только master и
сказал «прогон не состоялся» — при том, что посты в группу пришли. Диагноз, не
совпадающий с тем, что человек видит в телефоне, хуже отсутствия диагноза:
чинится это за минуту, а ищется полдня. Поэтому файл, не обновлённый в master,
ищется по остальным веткам, и «нигде нет» отделено от «есть, но не там».
"""

import datetime
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

# Файл результата → чей это шаг, чтобы в сообщении было видно, где оборвалось
WATCHED = {
    "DRAFTS.md": "черновики постов (агент-автор, 09:00)",
    "pipeline/selfcheck.md": "самопроверка автора по RULES.md (агент-автор, 09:00)",
    "REVIEW.md": "разбор редактора (агент-редактор, 09:40)",
}

# Метка законного пустого дня: автор дошёл до конца, но брать было нечего
NO_TOPICS_FILE = "pipeline/no-topics.md"

# Сколько символов причин из no-topics.md дотягивать в уведомление
NO_TOPICS_EXCERPT = 600


def last_commit_date(path: str, ref: str = "HEAD") -> str | None:
    """Дата последнего коммита файла в UTC.

    Берём дату принудительно в UTC (TZ + format-local), иначе git отдаёт её в
    часовом поясе коммитера, и коммит, сделанный ночью по Бангкоку, сравнивался
    бы с сегодняшней датой по UTC как будто он из другого дня.
    """
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d", ref, "--", path],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "TZ": "UTC"},
    )
    return result.stdout.strip() or None


def fetch_other_branches() -> None:
    """Подтягивает остальные ветки: checkout приносит только ту, на которой запущен.

    Результат печатается: без этого «веток не нашлось» и «fetch не отработал»
    выглядят в логе одинаково, а различать их придётся в день сбоя.
    """
    result = subprocess.run(
        ["git", "fetch", "--quiet", "origin", "+refs/heads/*:refs/remotes/origin/*"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"git fetch вернул {result.returncode}: {result.stderr.strip()}")
        return
    print(f"Веток, кроме master, видно: {len(other_branches())}")


def other_branches() -> list[str]:
    result = subprocess.run(
        ["git", "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [r for r in result.stdout.split() if r not in ("origin/HEAD", "origin/master")]


def branches_with_today(path: str, today: str) -> list[str]:
    """Ветки, кроме master, где файл обновлён сегодня.

    Пустой список — обычное дело: агенты пушат прямо в master, и веток тогда нет
    вовсе. Непустой значит, что прогон был, а результат не доехал.
    """
    found = []
    for ref in other_branches():
        if last_commit_date(path, ref) == today:
            found.append(ref[len("origin/"):])
    return found


def read_excerpt(path: str, limit: int) -> str:
    """Причины из no-topics.md для уведомления. Файл пишет агент, доверия ноль."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read().strip()
    except OSError:
        return ""
    if len(text) > limit:
        return text[:limit].rstrip() + "…"
    return text


def send(token: str, chat_id: str, text: str) -> None:
    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "link_preview_options": json.dumps({"is_disabled": True}),
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage", data=payload
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        json.load(response)


def main() -> int:
    # Windows-консоль по умолчанию cp1252: без этого локальный прогон падает на
    # первой же русской строке отчёта. В Actions строка ничего не меняет.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()

    # Пустой день проверяется первым: остальных трёх файлов в этот день быть
    # не должно, и жаловаться на их отсутствие незачем.
    if last_commit_date(NO_TOPICS_FILE) == today:
        lines = ["ℹ️ Прогон состоялся, но подходящих тем сегодня не нашлось."]
        reasons = read_excerpt(NO_TOPICS_FILE, NO_TOPICS_EXCERPT)
        if reasons:
            lines.append(reasons)
        lines.append("Постов и разбора сегодня нет — это не сбой.")
        send(token, chat_id, "\n\n".join(lines))
        print(f"Пустой день: {NO_TOPICS_FILE} обновлён сегодня ({today}), уведомление отправлено")
        return 0

    fetch_other_branches()

    stale = []      # файла за сегодня нет нигде
    elsewhere = []  # файл за сегодня есть, но не в master
    for path, label in WATCHED.items():
        updated = last_commit_date(path)
        if updated == today:
            print(f"Всё в порядке: {path} обновлён сегодня ({updated})")
            continue
        print(f"{path} последний раз менялся {updated}, сегодня {today}")
        branches = branches_with_today(path, today)
        if branches:
            print(f"  но за сегодня он есть в ветках: {', '.join(branches)}")
            elsewhere.append((path, label, updated, branches))
        else:
            stale.append((path, label, updated))

    if not stale and not elsewhere:
        return 0

    lines = []
    if elsewhere:
        lines.append("⚠️ Прогон сегодня был, но результат остался вне master.")
        for path, label, updated, branches in elsewhere:
            when = updated or "никогда"
            lines.append(
                f"• {label}: {path} обновлён сегодня в ветке {', '.join(branches)}, "
                f"в master — {when}."
            )
        lines.append(
            "Редактор и сторож читают master, поэтому дальше цепочка встанет. "
            "Ветку нужно перенести в master."
        )
    if stale:
        if elsewhere:
            lines.append("")
        lines.append("⚠️ Утренний прогон сегодня дошёл не до конца.")
        for path, label, updated in stale:
            when = updated or "никогда"
            lines.append(f"• Не пришло: {label}. Файл {path} последний раз обновлялся {when}.")
        lines.append("Похоже, прогон не состоялся или не отправил результат в репозиторий.")

    send(token, chat_id, "\n".join(lines))
    print(
        f"Уведомление отправлено в Telegram "
        f"(нет нигде: {len(stale)}, есть вне master: {len(elsewhere)})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
