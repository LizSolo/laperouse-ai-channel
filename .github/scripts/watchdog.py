"""Проверяет, что утренний прогон действительно обновил DRAFTS.md.

Запускается по расписанию примерно через час после routine. Если за сегодня
файл черновиков не менялся, значит прогон не состоялся или не сделал push —
и об этом нужно сообщить в Telegram, чтобы сбой не выглядел как тишина.
"""

import datetime
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

DRAFTS_FILE = "DRAFTS.md"


def last_commit_date() -> str | None:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", DRAFTS_FILE],
        capture_output=True,
        text=True,
        check=True,
    )
    stamp = result.stdout.strip()
    return stamp[:10] if stamp else None


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
    updated = last_commit_date()

    if updated == today:
        print(f"Всё в порядке: {DRAFTS_FILE} обновлён сегодня ({updated})")
        return 0

    print(f"{DRAFTS_FILE} последний раз менялся {updated}, сегодня {today}")
    send(
        token,
        chat_id,
        "⚠️ Утренняя сводка сегодня не пришла. Прогон не состоялся "
        f"или не отправил черновики в репозиторий (последнее обновление: {updated}).",
    )
    print("Уведомление отправлено в Telegram")
    return 0


if __name__ == "__main__":
    sys.exit(main())
