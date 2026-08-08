"""Шлёт в Telegram сообщение о том, что шаг конвейера остановился.

Нужен, чтобы сбой не выглядел как тишина: без уведомления «постов сегодня нет»
и «постов сегодня не выпустили из-за ошибки» читаются одинаково.

Запуск:
    python3 .github/scripts/notify.py "Заголовок" файл-с-подробностями
"""

import json
import os
import sys
import urllib.parse
import urllib.request

MAX_DETAILS = 3000


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

    title = sys.argv[1] if len(sys.argv) > 1 else "Сбой в конвейере"
    details = ""
    if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
        with open(sys.argv[2], encoding="utf-8") as f:
            details = f.read().strip()[:MAX_DETAILS]

    message = f"⚠️ {title}"
    if details:
        message += f"\n\n{details}"

    try:
        send(token, chat_id, message)
        print("Уведомление отправлено")
    except Exception as error:  # noqa: BLE001 — уведомление не должно ронять шаг
        print(f"Не удалось отправить уведомление: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
