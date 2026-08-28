# Проверенные факты за 2026-08-28

По каждой теме: первоисточник, подтверждение, факты. Числа отсюда сверяет `pipeline/lint.py`
(F-04) — каждое число в посте должно быть здесь.

---

## 1. Альфа-Банк, «Лаборатория роботизации»

Первоисточник: https://www.vedomosti.ru/finance/articles/2026/08/27/1224002-alfa-bank-pomozhet-biznesu-vnedryat-robotov (EGRESS_BLOCKED для WebFetch, подтверждён через WebSearch, путь два).
Подтверждение: https://bosfera.ru/press-release/alfa-bank-pomozhet-biznesu-vnedryat-robototehnicheskie-resheniya, https://togliatti24.ru/technologies/view/laboratoria-robotizacii-alfa-banka-pomozet-vnedrat-tehniceskie-resenia — совпадают дословно.

Факты: Альфа-Банк создаёт «Лабораторию роботизации» — площадку, которая будет диагностировать
бизнес-процессы клиентов и подбирать готовые робототехнические решения под них, а также
разрабатывать механизмы финансирования таких проектов. Комментарий дал Владимир Воейков, первый
заместитель председателя правления банка, директор по крупному и среднему бизнесу — то есть
инициатива нацелена на этот сегмент, не на малый бизнес. Начало работы лаборатории — IV квартал
2026 года, точной даты нет. Дата публикации источника — 27 августа 2026.

## 2. Claude, встроенный браузер в Cowork

Первоисточник: https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork (открыт целиком через WebFetch).
Подтверждение (второй путь для контекста рынка): https://www.thenextweb.com/news/anthropic-claude-cowork-built-in-browser-dma-choice-screen, https://www.macstories.net/news/anthropic-introduces-an-in-app-browser-for-claude-cowork/ — совпадают по сути.

Факты: в Claude Desktop появился встроенный браузер для режима Cowork — открывается в боковой
панели, когда задаче нужен сайт: Claude загружает страницы, читает их, кликает и заполняет формы
без переключения окон. Доступен на macOS, Windows и Linux (бета) на планах Pro, Max и Team, а
также на Enterprise там, где владелец аккаунта включил функцию. Разворачивается постепенно в
течение недели публикации, точной даты завершения раскатки нет. Можно импортировать cookies из
Chrome, Edge и Firefox на macOS и из Firefox на Windows и Linux (бета) — так браузер сохраняет
вход на сайты пользователя. Банковские, почтовые и SSO-сайты не выделяются под импорт кук по
умолчанию. Встроенный браузер использует те же защиты, что Claude in Chrome: проверку прав перед
действием, блокировку высокорисковых сайтов и анализ действий; разработчики не рекомендуют
использовать его для управления финансовыми счетами.

## 3. OpenAI, ChatGPT Work: webhook-задачи и расшаренные scheduled tasks

Первоисточник: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt (403 для WebFetch, подтверждён через WebSearch, путь два).
Подтверждение: https://www.techtimes.com/articles/325576/20260826/chatgpt-work-adds-gmail-webhooks-inbox-login-new-automation-new-attack-route.htm (26 августа 2026) — совпадает по сути.

Факты: в ChatGPT Work появились задачи по вебхукам — они реагируют на событие в подключённом
приложении, а не только по расписанию. Поддержаны Gmail (новое письмо, с фильтром по отправителю
или теме), Slack (новое сообщение в канале, куда добавлен @ChatGPT) и GitHub (активность в pull
request в авторизованном репозитории). Отдельно доступна функция расшаренных задач: пользователь
делится готовой облачной scheduled task с коллегой, а тот создаёт у себя отдельную копию с той же
настройкой вместо того, чтобы собирать её заново; расшарить можно и вебхук-задачи. Доступно
пользователям на тарифах Plus, Pro, Business, Enterprise и Edu, а также в ChatGPT for Healthcare.
Пользователям Free и Go создавать вебхук-задачи нельзя.

## 4. Salesforce и Anthropic, «Claudeforce» / Salesforce in Claude

Первоисточник: https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/ (EGRESS_BLOCKED для WebFetch, подтверждён через WebSearch, путь два).
Подтверждение: https://investor.salesforce.com/news/news-details/2026/Salesforce-and-Anthropic-Announce-Claudeforce-The-1-AI-Meets-the-1-AI-CRM/default.aspx (официальный канал Salesforce), https://it-online.co.za/2026/08/27/claudeforce-merges-salesforce-and-claude-capabilities/, https://thenextweb.com/news/salesforce-anthropic-claudeforce-partnership — совпадают дословно.

Факты: Salesforce и Anthropic объявили расширенное партнёрство «Claudeforce» 26 августа 2026.
В его рамках вышел плагин «Salesforce in Claude» для Claude Cowork с 37 готовыми скиллами продаж:
подготовка к встрече, оценка здоровья сделки, анализ воронки. Продавец может запрашивать,
обновлять и выполнять действия с данными CRM прямо в Claude, не открывая интерфейс Salesforce.
Доступен пилотным клиентам сейчас, открытая бета запланирована на сентябрь 2026, дополнительные
скиллы для других функций бизнеса начнут выходить позже в 2026 году. Плагин работает через
AIforce — корпоративный слой Salesforce, который подключает данные и workflow к любому агенту
через MCP-серверы и API. Отдельно: Salesforce официально не работает в России с марта 2022 года —
компания присоединилась к санкциям, не принимает платежи российскими картами и не заключает
договоры с российскими юрлицами (подтверждено независимо: okocrm.com, admetric.pro, две
публикации о переходе с Salesforce на российские CRM).
