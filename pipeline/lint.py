"""Проверяет посты из DRAFTS.md по механическим правилам RULES.md.

Скрипт закрывает те правила, на которые можно ответить да/нет без чтения смысла:
длину, разметку, запрещённые обороты. Судейские правила (T-01, X-02, X-09, X-11,
X-18) и всё, что требует источника, он не трогает — они остаются в selfcheck.md.

Запуск:
    python pipeline/lint.py                # проверить DRAFTS.md
    python pipeline/lint.py FILE           # проверить другой файл

Результат: отчёт в stdout, файл pipeline/lint.md со строками по каждому ID,
код возврата 1, если хоть одно правило нарушено.

Две категории находок:
    ОШИБКА  — правило нарушено, публиковать нельзя, код возврата 1.
    ПРОВЕРЬ — скрипт не может решить сам, нужен человек или агент, код не меняется.
"""

import os
import re
import sys

DRAFTS_FILE = "DRAFTS.md"
VERIFIED_FILE = os.path.join("pipeline", "verified.md")
REPORT_FILE = os.path.join("pipeline", "lint.md")

MIN_CHARS = 900
MAX_CHARS = 1800
MAX_FIRST_LINE = 150
MAX_SENTENCES = 3
SIGNATURE = "#ЛизаСоло 👩‍💻"

EMOJI_RANGES = (
    (0x1F300, 0x1FAFF),
    (0x2600, 0x27BF),
    (0x2B00, 0x2BFF),
    (0x2190, 0x21FF),
    (0x2000, 0x206F),
    (0xFE00, 0xFE0F),
    (0x1F000, 0x1F2FF),
)


# --- разбор файла ---------------------------------------------------------


def extract_blocks(markdown: str) -> list[str]:
    """Те же блоки, что заберёт send_drafts.py. Логика намеренно совпадает."""
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", markdown, re.DOTALL)
    return [b.strip() for b in blocks if b.strip()]


def count_headers(markdown: str) -> int:
    return len(re.findall(r"^##\s+Пост\b", markdown, re.MULTILINE))


def drop_urls(text: str) -> str:
    """Убирает адреса из href: цифры и тире внутри URL к тексту не относятся."""
    return re.sub(r'<a\s+href="[^"]*"\s*>', "<a>", text)


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def body_paragraphs(text: str) -> list[str]:
    """Абзацы без служебного хвоста: строки источника и подписи."""
    result = []
    for para in paragraphs(text):
        plain = strip_tags(para).strip()
        if plain == SIGNATURE or plain == "Источник":
            continue
        result.append(para)
    return result


def is_emoji(char: str) -> bool:
    code = ord(char)
    return any(low <= code <= high for low, high in EMOJI_RANGES)


def is_list_line(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if re.match(r"^(•|[-–—]\s|\d+[.)]\s)", line):
        return True
    return is_emoji(line[0])


def sentences(paragraph: str) -> list[str]:
    plain = strip_tags(paragraph)
    parts = re.split(r"(?<=[.!?…])\s+", plain)
    return [p for p in (part.strip() for part in parts) if p]


# --- отдельные правила ----------------------------------------------------
# Каждая функция возвращает (ok, деталь). ok=None означает «ПРОВЕРЬ».


def x04_paragraph_length(text):
    problems = []
    for number, para in enumerate(body_paragraphs(text), start=1):
        lines = [line for line in para.split("\n") if line.strip()]
        if lines and all(is_list_line(line) for line in lines):
            continue
        count = len(sentences(para))
        if count > MAX_SENTENCES:
            problems.append(f"абзац {number}: {count} предложений")
    if problems:
        return False, "; ".join(problems)
    return True, "все абзацы не длиннее 3 предложений"


def x08_length(text):
    length = len(strip_tags(drop_urls(text)))
    if length < MIN_CHARS:
        return False, f"{length} знаков, меньше {MIN_CHARS}"
    if length > MAX_CHARS:
        return False, f"{length} знаков, больше {MAX_CHARS}"
    return True, f"{length} знаков"


def x12_first_line(text):
    first_line = strip_tags(text.split("\n")[0]).strip()
    if len(first_line) > MAX_FIRST_LINE:
        return False, f"{len(first_line)} знаков, больше {MAX_FIRST_LINE}"
    return True, f"{len(first_line)} знаков"


def x13_address_reader(text):
    plain = strip_tags(drop_urls(text))
    if re.search(r"\b(вы|вам|вас|вами|ваш\w*)\b", plain, re.IGNORECASE):
        return True, "обращение на «вы» есть"
    return False, "в тексте поста нет обращения на «вы»"


def m01_first_line_is_sentence(text):
    first_line = text.split("\n")[0].strip()
    plain = strip_tags(first_line).strip()
    if re.fullmatch(r"<b>.*</b>", first_line):
        return False, "первая строка целиком в <b> — это заголовок-ярлык"
    if not plain:
        return False, "первая строка пуста"
    if not is_emoji(plain[-1]):
        return False, f"первая строка не кончается эмодзи: «…{plain[-30:]}»"
    return True, "обычное предложение с эмодзи в конце"


def m02_bold(text):
    bolds = re.findall(r"<b>(.*?)</b>", text, re.DOTALL)
    if not bolds:
        return False, "нет ни одного <b>"
    for para in paragraphs(text):
        if len(re.findall(r"<b>", para)) > 1:
            return False, f"больше одного <b> в абзаце: «{strip_tags(para)[:60]}…»"
    for bold in bolds:
        # Точка внутри номера версии («GPT-5.6») концом предложения не считается.
        if re.search(r"(?<!\d)[.!?](?=\s|$)", bold):
            return False, f"<b> содержит целое предложение: «{bold[:60]}»"
    first_line = text.split("\n")[0].strip()
    if re.fullmatch(r"<b>.*</b>", first_line):
        return False, "вся первая строка в <b>"
    return True, f"{len(bolds)} выделения, по одному на абзац"


def m03_no_labels(text):
    pattern = r"(?:<[bi]>\s*)?\b(Нюанс|Проверить просто|Важно)\b(?:\s*</[bi]>)?\s*[:：]"
    hit = re.search(pattern, text)
    if hit:
        return False, f"метка-ярлык «{hit.group(1)}»"
    return True, "меток-ярлыков нет"


def m04_source_link(text):
    without_href = re.sub(r'href="[^"]*"', "", text)
    bare = re.search(r"https?://", without_href)
    if bare:
        return False, "в тексте есть сырой URL"
    anchors = re.findall(r"<a\s+href=\"[^\"]*\"\s*>(.*?)</a>", text)
    if not anchors:
        return False, "нет ссылки <a href=\"…\">Источник</a>"
    wrong = [a for a in anchors if a.strip() != "Источник"]
    if wrong:
        return False, f"текст ссылки не «Источник»: «{wrong[0][:60]}»"
    return True, "ссылка оформлена как Источник"


def m05_signature(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if lines and strip_tags(lines[-1]).strip() == SIGNATURE:
        return True, "подпись на месте"
    last = strip_tags(lines[-1]) if lines else ""
    return False, f"последняя строка не подпись: «{last[:60]}»"


def m08_no_source_line(text):
    if re.search(r"^\s*Источник:\s*http", text, re.MULTILINE):
        return False, "строка «Источник: URL» попала внутрь блока"
    return True, "внутри блока только текст поста"


def z01_dash(text):
    plain = strip_tags(drop_urls(text))
    for hit in re.finditer(r"(?<!\d)\s[—–-]\s(?!\d)", plain):
        start = max(0, hit.start() - 40)
        return False, f"тире-связка: «…{plain[start:hit.end() + 40]}…»"
    return True, "тире-связки нет"


def make_phrase_rule(phrases, label):
    def rule(text):
        plain = strip_tags(drop_urls(text))
        for phrase in phrases:
            hit = re.search(r"\b" + phrase + r"\b", plain, re.IGNORECASE)
            if hit:
                start = max(0, hit.start() - 30)
                return False, f"{label}: «…{plain[start:hit.end() + 30]}…»"
        return True, f"{label} не найдено"

    return rule


z02 = make_phrase_rule(
    ["именно", "таким образом", "в итоге", "итак", "подводя итог"],
    "запрещённое слово",
)
z05 = make_phrase_rule(
    ["а что если", "задумывались ли вы", "знакомо\\?"],
    "вопрос-клише",
)
z06 = make_phrase_rule(
    [
        "давайте разб[её]р[её]мся",
        "сегодня хочу поделиться",
        "это изменит ваш бизнес",
        "мало кто понимает",
        "секрет успеха",
        "невероятный инсайт",
        "все должны использовать ИИ",
    ],
    "инфобизнес-язык",
)
z08 = make_phrase_rule(
    ["эксперты считают", "аналитики называют", "исследования показывают", "как известно"],
    "безымянная группа",
)
z09 = make_phrase_rule(
    [
        "знаменует",
        "переломный момент",
        "новая эра",
        "меняет правила игры",
        "беспрецедентн\\w*",
        "настоящий прорыв",
        "революция в",
        "нельзя недооценивать",
    ],
    "раздувание значимости",
)


def z03_not_x_but_y(text):
    plain = strip_tags(drop_urls(text))
    hit = re.search(r"\bне\s+[^,.!?]{2,60},\s+а\s+", plain, re.IGNORECASE)
    if hit:
        return False, f"конструкция «не X, а Y»: «{hit.group(0).strip()}…»"
    return True, "конструкции «не X, а Y» нет"


def z04_poetomu(text):
    paras = body_paragraphs(text)
    if paras and re.match(r"^\s*Поэтому\b", strip_tags(paras[-1]), re.IGNORECASE):
        return False, "финальный абзац открывается словом «Поэтому»"
    return True, "финальный абзац не с «Поэтому»"


def z10_range(text):
    plain = strip_tags(drop_urls(text))
    hit = re.search(r"\bот\s+([^\d\s][^,]{0,30}?)\s+до\s+([^\d\s][^,.]{0,30})", plain)
    if hit:
        return False, f"диапазон с категориями: «{hit.group(0)[:60]}»"
    return True, "диапазонов «от … до …» с категориями нет"


def f04_numbers_verified(text, verified):
    """ПРОВЕРЬ: числа из поста, которых нет в verified.md дословно."""
    if verified is None:
        return None, "pipeline/verified.md не найден, сверить числа не с чем"
    plain = strip_tags(drop_urls(text))
    numbers = set(re.findall(r"\d+(?:[.,]\d+)?", plain))
    missing = sorted(n for n in numbers if n not in verified)
    if missing:
        return None, f"нет в verified.md: {', '.join(missing)}"
    return True, "все числа поста есть в verified.md"


CHECKS = [
    ("X-04", x04_paragraph_length),
    ("X-08", x08_length),
    ("X-12", x12_first_line),
    ("X-13", x13_address_reader),
    ("M-01", m01_first_line_is_sentence),
    ("M-02", m02_bold),
    ("M-03", m03_no_labels),
    ("M-04", m04_source_link),
    ("M-05", m05_signature),
    ("M-08", m08_no_source_line),
    ("Z-01", z01_dash),
    ("Z-02", z02),
    ("Z-03", z03_not_x_but_y),
    ("Z-04", z04_poetomu),
    ("Z-05", z05),
    ("Z-06", z06),
    ("Z-08", z08),
    ("Z-09", z09),
    ("Z-10", z10_range),
]


# --- прогон ---------------------------------------------------------------


def check_post(text: str, verified: str | None) -> list[tuple[str, object, str]]:
    results = []
    for rule_id, rule in CHECKS:
        try:
            ok, detail = rule(text)
        except Exception as error:  # noqa: BLE001 — сбой правила не должен ронять прогон
            ok, detail = None, f"правило не отработало: {error}"
        results.append((rule_id, ok, detail))
    ok, detail = f04_numbers_verified(text, verified)
    results.append(("F-04", ok, detail))
    return results


def analyse(path: str = DRAFTS_FILE) -> tuple[int, list[str]]:
    """Проверяет файл и возвращает (число нарушений, строки отчёта).

    Отдельно от main(), потому что тем же гейтом пользуется send_drafts.py:
    он вызывает analyse() и отказывается публиковать, если нарушения есть.
    """
    if not os.path.exists(path):
        return 1, [f"ОШИБКА: {path} не найден"]

    with open(path, encoding="utf-8") as f:
        markdown = f.read()

    posts = extract_blocks(markdown)
    headers = count_headers(markdown)

    report = [f"# Проверка скриптом: {path}", ""]

    if not posts:
        report.append(f"ОШИБКА: в {path} нет ни одного блока с постом")
        return 1, report

    errors = 0
    if headers != len(posts):
        errors += 1
        report.append(f"M-07: нет — заголовков «## Пост» {headers}, блоков {len(posts)}")
    else:
        report.append(f"M-07: да — {len(posts)} заголовков, {len(posts)} блоков")
    report.append("")

    verified = None
    if os.path.exists(VERIFIED_FILE):
        with open(VERIFIED_FILE, encoding="utf-8") as f:
            verified = f.read()

    for number, post in enumerate(posts, start=1):
        report.append(f"## Пост {number}")
        for rule_id, ok, detail in check_post(post, verified):
            if ok is True:
                mark = "да"
            elif ok is False:
                mark = "нет"
                errors += 1
            else:
                mark = "ПРОВЕРЬ"
            report.append(f"{rule_id}: {mark} — {detail}")
        report.append("")

    return errors, report


def failures(report: list[str]) -> list[str]:
    """Только то, что требует внимания. Заголовок поста без находок не печатается."""
    keep: list[str] = []
    pending: str | None = None
    for line in report:
        if line.startswith("## Пост"):
            pending = line
        elif line.startswith("ОШИБКА") or ": нет — " in line or ": ПРОВЕРЬ — " in line:
            if pending:
                keep.append(pending)
                pending = None
            keep.append(line)
    return keep


def main() -> int:
    # Windows-консоль по умолчанию cp1252 и падает на кириллице с эмодзи.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    path = sys.argv[1] if len(sys.argv) > 1 else DRAFTS_FILE
    errors, report = analyse(path)

    if len(report) > 1:
        write_report(report)

    for line in failures(report):
        print(line)

    if errors:
        print(f"\nНарушено правил: {errors}. Публиковать нельзя, отчёт в {REPORT_FILE}")
        return 1

    print(f"\nВсе механические правила пройдены. Отчёт в {REPORT_FILE}")
    return 0


def write_report(lines: list[str]) -> None:
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


if __name__ == "__main__":
    sys.exit(main())
