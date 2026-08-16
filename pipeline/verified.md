# Проверка фактов за 2026-08-16

## Пост 1. ChatGPT Business — Computer History

Первоисточник (закрыт для автоматических запросов, egress-прокси возвращает блокировку на
help.openai.com): https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes
Подтверждение (независимо друг от друга): https://www.digitaltrends.com/computing/chatgpt-can-now-remember-what-users-do-on-their-mac/
и https://9to5mac.com/2026/08/13/chatgpt-for-mac-adds-opt-in-computer-history-feature-replacing-chronicle/
Путь по F-01: дословное совпадение фактов в двух независимых публикациях (прямой источник не открылся).

Факты:
- Функция Computer History в приложении ChatGPT для Mac, раскатка началась 13 августа 2026.
- Заменяет прежнюю функцию Chronicle.
- Доступна пользователям Pro, Business и Enterprise.
- На Business и Enterprise сначала администратор воркспейса должен выдать доступ, только
  после этого сотрудник может включить функцию себе — по умолчанию выключена везде.
- Включается в Settings → Integrations.
- Записывает клики, набор текста, переключение между приложениями через macOS accessibility
  API; превращает это в текстовые саммари по дням и времени. Не делает скриншотов, не пишет
  экран и звук, приватный режим браузера не отслеживается.
- Можно выбрать, какие приложения и сайты разрешены, поставить сбор на паузу, удалить историю.
- Недоступна в ЕЭЗ, Швейцарии и Великобритании.

## Пост 2. Anthropic — сканирование скиллов и плагинов (бета)

Первоисточник (открыт напрямую): https://support.claude.com/en/articles/15927065-get-started-with-skill-and-plugin-scanning
Подтверждение даты: https://support.claude.com/en/articles/12138966-release-notes (запись от
6 августа 2026 — «Skill and plugin security scanning (beta)»)
Путь по F-01: первоисточник открыт целиком.

Факты:
- Бета-функция «Skill and plugin security scanning», доступна на Enterprise-планах Claude,
  Claude Cowork и в Enterprise plugin marketplace.
- Включают владелец организации или Primary Owner: Organization settings → Skills → «Skill
  and plugin security scanning».
- Работает бесплатно.
- Проверяет сторонние скиллы и плагины на признаки вредоносного поведения при загрузке или
  редактировании.
- Три исхода: pass (проблем не найдено), warn (вредоносное содержимое не до конца
  верифицировано — скилл остаётся включённым, но с баннером предупреждения), fail
  (вредоносное содержимое обнаружено — скилл блокируется, блокировку нельзя переопределить).
- Дата выхода: 6 августа 2026 (по записи в release notes).

## Пост 3. Notion — шаринг контекста с Custom Agent из меню Share

Первоисточник (открыт напрямую): https://www.notion.com/releases/2026-08-07
Путь по F-01: первоисточник открыт целиком, второй источник не понадобился.

Факты:
- Релиз от 7 августа 2026.
- Документами и базами данных теперь можно делиться с Custom Agent прямо из стандартного
  меню Share.
- Раньше для этого требовалось переходить в настройки конкретного агента.

## Пост 4. Google — Gemini 3.7 Flash

Первоисточник (открыт напрямую): https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
Подтверждение: https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut
Путь по F-01: первоисточник открыт целиком, дополнительно сверено с независимой публикацией.

Факты:
- Вышла 13 августа 2026, через три недели после Gemini 3.6 Flash.
- Улучшения в кодинге (точнее с первой попытки, лучше отладка), веб-разработке, агентных
  многошаговых задачах, обработке сложных документов (в т.ч. финансы, право).
- Вводная цена до 31 декабря 2026: $0.75 (0,75 доллара) за 1 млн входных токенов, $3.75
  (3,75 доллара) за 1 млн выходных — вдвое дешевле цены запуска предыдущей модели. С 1 января
  2027 цена вырастет до $1.50 (1,50 доллара) / $7.50 (7,50 доллара).
- Доступна разработчикам через Google AI Studio, Android Studio, Google Antigravity.
- Для бизнеса — через Gemini Enterprise Agent Platform и приложение Gemini Enterprise.
- Также обновила Gemini Spark — агента для подписчиков Google AI Pro и Ultra (доступен в
  160+ странах), с улучшенной работой с инструментами Google Workspace.

## Пост 5. OpenAI — программа для малого бизнеса вокруг ChatGPT Work

Первоисточник (закрыт для автоматических запросов, egress-прокси возвращает блокировку на
openai.com): https://openai.com/index/small-business-ai-jam/
Подтверждение (независимо друг от друга): https://www.inc.com/chloe-aiello/openai-just-unveiled-a-massive-push-to-turn-small-business-owners-into-ai-power-users/91377329
и https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-program-to-accelerate-small-business-ai-adoption/
Путь по F-01: дословное совпадение фактов в двух независимых публикациях (прямой источник не
открылся, Inc.com тоже заблокирован прокси, но найден и процитирован поиском).

Факты:
- Программа объявлена 21 июля 2026.
- Четыре компонента: вебинары под конкретные сценарии малого бизнеса; очные мероприятия
  AI Academy в США; библиотека гайдов, историй клиентов и коротких видео; набор партнёрских
  интеграций и плагинов под рабочие процессы малого бизнеса (партнёры — Dropbox, Shopify,
  Intuit, Slack, Atlassian).
- В основе программы — ChatGPT Work, агент внутри ChatGPT, запущенный 9 июля вместе с
  моделью GPT-5.6: помогает с многошаговыми задачами вроде анализа бюджета, подготовки
  маркетинговых материалов, подготовки к встречам.
- На момент объявления у ChatGPT Work и Codex вместе 10 млн пользователей.
