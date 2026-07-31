"""Отправляет черновики постов из DRAFTS.md в Telegram.

Каждый пост в DRAFTS.md лежит в отдельном блоке с тройными обратными кавычками.
Текст внутри блока отправляется как есть, с parse_mode=HTML и отключённым превью.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

DRAFTS_FILE = "DRAFTS.md"


def extract_posts(markdown: str) -> list[str]:
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", markdown, re.DOTALL)
    return [b.strip() for b in blocks if b.strip()]


def send(token: str, chat_id: str, text: str) -> dict:
    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "link_preview_options": json.dumps({"is_disabled": True}),
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage", data=payload
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> int:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    if not os.path.exists(DRAFTS_FILE):
        print(f"{DRAFTS_FILE} не найден, публиковать нечего")
        return 0

    with open(DRAFTS_FILE, encoding="utf-8") as f:
        posts = extract_posts(f.read())

    if not posts:
        print(f"В {DRAFTS_FILE} нет блоков с постами (тройные обратные кавычки)")
        return 1

    failed = 0
    for number, text in enumerate(posts, start=1):
        try:
            result = send(token, chat_id, text)
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            print(f"Пост {number}: HTTP {error.code} — {body}")
            failed += 1
            continue
        print(f"Пост {number}: отправлен, message_id={result['result']['message_id']}")

    if failed:
        print(f"Не отправлено постов: {failed} из {len(posts)}")
        return 1

    print(f"Готово, отправлено постов: {len(posts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
