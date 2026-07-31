"""Проверяет, что утренний прогон действительно дошёл до конца.

Запускается по расписанию через час после редактора. Смотрит на оба результата
цепочки: черновики от автора и разбор от редактора. Если за сегодня файл не
менялся, значит прогон не состоялся или не сделал push — и об этом нужно
сообщить в Telegram, чтобы сбой не выглядел как тишина.
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
    "REVIEW.md": "разбор редактора (агент-редактор, 09:40)",
}


def last_commit_date(path: str) -> str | None:
    """Дата последнего коммита файла в UTC.

    Берём дату принудительно в UTC (TZ + format-local), иначе git отдаёт её в
    часовом поясе коммитера, и коммит, сделанный ночью по Бангкоку, сравнивался
    бы с сегодняшней датой по UTC как будто он из другого дня.
    """
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d", "--", path],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "TZ": "UTC"},
    )
    return result.stdout.strip() or None


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
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()

    stale = []
    for path, label in WATCHED.items():
        updated = last_commit_date(path)
        if updated == today:
            print(f"Всё в порядке: {path} обновлён сегодня ({updated})")
        else:
            print(f"{path} последний раз менялся {updated}, сегодня {today}")
            stale.append((path, label, updated))

    if not stale:
        return 0

    lines = ["⚠️ Утренний прогон сегодня дошёл не до конца."]
    for path, label, updated in stale:
        when = updated or "никогда"
        lines.append(f"• Не пришло: {label}. Файл {path} последний раз обновлялся {when}.")
    lines.append("Похоже, прогон не состоялся или не отправил результат в репозиторий.")

    send(token, chat_id, "\n".join(lines))
    print(f"Уведомление отправлено в Telegram (не обновилось файлов: {len(stale)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
