# Проверка фактов за 2026-09-16

## Пост 1. Хакеры маскируют атаки под ChatGPT, DeepSeek, Claude, Perplexity и Grok

- Первоисточник: https://www.cnews.ru/news/top/2026-09-15_chatgptdeepseek_i_claude_stali_prikrytiem
  (открыт целиком через WebFetch, второй источник не требуется по F-01)
- Факты:
  - 417 млн кибератак в июле 2026 года — рекорд за весь период наблюдений
  - на 52% больше, чем в июле 2025 года (274 млн атак)
  - 53% атак использовали DNS Rebinding для перенаправления на внутреннюю инфраструктуру
  - 93% июльских инцидентов — сканирование приложений в поиске уязвимостей
  - отраслевое распределение атак: 71% транспорт и логистика, 15% госсектор, 8% ИТ-компании,
    6% торговля и энергетика
  - маску User-Agent «DeepSeekBot» впервые зафиксировали 12 августа 2026 года
  - источник данных — группа компаний «Солар» (подразделение Solar WAF), период наблюдений —
    январь 2024 — август 2026 года
  - маскируются под User-Agent пяти сервисов: ChatGPT, DeepSeek, Claude, Perplexity, Grok

## Пост 2. Первая линия ИТ-поддержки решает заявки, а не сортирует их

- Первоисточник: https://habr.com/ru/companies/simpleone/articles/1082602/
  (открыт целиком через WebFetch)
- Факты:
  - компания SimpleOne, продукт SimpleOne ITSM
  - решение использует RAG (Retrieval-Augmented Generation) поверх базы знаний и объявлений
  - ассистент понимает естественный язык обращения, объединяет дубли одинаковых заявок
    (пример из статьи: «не открывается почта»)
  - не требует перестройки существующей структуры данных компании
  - числовых показателей (процентов, сумм) в источнике не названо — в пост цифры не включаются

## Пост 3. Чем собирать карусели и карточки для соцсетей

- Первоисточник: https://vc.ru/ai/3140429-obzor-servisov-dlya-sozdaniya-karuseley-i-kartochek
  (открыт целиком через WebFetch)
- Факты:
  - сравниваются 5 сервисов: Carousai, связка ChatGPT + Figma, Canva (Magic Studio), Gamma App,
    Photoroom + Clipdrop
  - для россиян доступ к платным функциям Canva затруднён (указано в самой статье)
  - Carousai — самый быстрый вариант получить готовый пост за несколько кликов
  - связка ChatGPT + Figma — максимальный контроль над дизайном
  - Gamma — вариант для лонгридов и лекций
  - цены сервисов в статье не указаны — в пост цены не включаются

## Пост 4. ElevenLabs выпустила модель Music v2.5

- Первоисточник: https://elevenlabs.io/blog/music-v2-5-model (найден и подтверждён через
  WebSearch; прямой WebFetch отклонён egress-прокси, домен elevenlabs.io не в allowlist)
- Подтверждение (независимые публикации, факты совпадают дословно):
  https://www.musicbusinessworldwide.com/elevenlabs-launched-music-v2-5-shortly-after-announcing-its-umg-licensing-deal/
  и https://tbreak.com/elevenlabs-music-v25-free-downloads-api/
- Факты:
  - модель Music v2.5 стала моделью по умолчанию в ElevenMusic в пятницу, 11 сентября 2026 года
  - слепой тест на 47 885 парах одинаковых промптов: новую модель предпочли в большинстве случаев
  - улучшения сильнее всего заметны в R&B, соуле, хип-хопе, роке, метале, оркестровой и
    кинематографической музыке
  - бесплatный тариф получил 5 lossless-загрузок в день (у платного Pro — 400 в месяц)
  - модель доступна в ElevenMusic, ElevenCreative, Studio, Flows и через API
  - на бесплатном тарифе коммерческое использование требует указания авторства ElevenMusic

## Пост 5. Notion 3.7: общая библиотека навыков ИИ-агентов

- Первоисточник: https://www.notion.com/releases (открыт целиком через WebFetch, запись от
  15 сентября 2026 года)
- Факты:
  - релиз Notion 3.7 датирован 15 сентября 2026 года
  - функция «Agent skills for your whole team» — переиспользуемые инструкции («навыки») для
    агентов, общие для всей команды
  - навыки можно выгружать в Claude Code, Codex, Cursor и другие сервисы
  - вышло приложение Notion Agents для iOS
  - Custom Agents теперь могут вызывать sub-agents для делегирования части задачи
  - доступны модели Opus 5, GPT-5.6 Sol, Kimi K3

## Пост 6. Google Workspace: Gemini подключается к CRM и бухгалтерии через MCP

- Первоисточник: https://workspaceupdates.googleblog.com/ (открыт целиком через WebFetch, запись
  «Connect to more tools with Gemini in Google Workspace» от 15 сентября 2026 года)
- Подтверждение деталей по статусу коннекторов: https://knowledge.hubspot.com/integrations/set-up-and-use-hubspot-connector-for-gemini
- Факты:
  - Gemini подключается напрямую к Salesforce, HubSpot, QuickBooks и Asana через протокол MCP
  - работает прямо внутри Docs, Sheets, Drive и Chat, без переключения вкладок
  - коннектор для HubSpot — в открытом бета-тесте, доступен клиентам HubSpot любого тарифа при
    платном Google Workspace Business Standard, Business Plus или Enterprise

## Пост 7. Gmail: поиск по почте с ИИ-обзором ответов на естественном языке

- Первоисточник: https://workspaceupdates.googleblog.com/ (тот же пост от 15 сентября 2026 года,
  запись «Gmail Search's AI Overviews now available globally»)
- Факты:
  - функция позволяет задавать вопросы на естественном языке прямо в поиске Gmail
  - в ответ приходит краткое резюме без необходимости пролистывать письма вручную
  - функция расширена до глобальной доступности для пользователей платных планов

## Пост 8. Многодневные ИИ-агенты незаметно забывают правила комплаенса

- Первоисточник: https://venturebeat.com/orchestration/long-running-ai-agents-quietly-drop-compliance-rules-and-bigger-context-windows-wont-fix-it
  (найден и подтверждён через WebSearch; прямой WebFetch отклонён egress-прокси, домен
  venturebeat.com не в allowlist)
- Подтверждение (независимые публикации и научная статья, факты совпадают дословно):
  https://www.kucoin.com/news/flash/ai-agents-gradually-ignore-compliance-rules-as-sessions-grow-longer,
  https://cryptobriefing.com/ai-agents-drop-compliance-rules-context-windows/,
  https://arxiv.org/html/2606.22528v2
- Факты:
  - при сжатии истории переписки (context compaction) в длинных сессиях модель может тихо
    отбросить исходные правила-ограничения, продолжая работать без сбоев и оповещений
  - пример из исследования: агент сначала отказывался отправить письмо за пределы домена
    компании, а после сжатия контекста выполнил тот же запрос
  - в тестах падение соблюдения правил по мере роста сессии доходило до 46 процентных пунктов
  - по данным Cloud Security Alliance, 53% организаций фиксировали случаи, когда ИИ-агент выходил
    за пределы разрешённых полномочий регулярно или время от времени
  - публикация VentureBeat датирована 13 сентября 2026 года
