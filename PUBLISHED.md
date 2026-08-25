# Лог отправленного

Все темы, которые дошли до тестовой группы. По этому файлу работает дедупликация: правило
T-02 в `RULES.md` сверяется со **всеми** строками, независимо от статуса.

Два статуса:

- `одобрено` — Лиза взяла пост в канал или переписала его как финальный;
- `отправлено` — черновик ушёл в группу, но одобрения не получил.

**Почему считаются оба.** До 08.08 файл хранил только одобренное, а отправленные черновики
нигде не фиксировались. 07.08 агент выдал два поста подряд по темам, которые уходили в группу
05.08, и редактор их не поймал: в файле их не было. Тема, которую читатель уже видел, занята
вне зависимости от того, понравился пост или нет. Почему тема не понравилась — в `FEEDBACK.md`,
здесь только факт отправки.

**Формат строки:** `дата — статус — тема — первоисточник`.

**Агент дописывает строки, а не перезаписывает файл.** Одна строка на каждый пост из
`DRAFTS.md`, статус `отправлено`, в том же push, что и черновики. Статус на `одобрено` меняет
Лиза руками.

---

- 2026-07-31 — одобрено — Claude Opus 5: цена не изменилась + контекст вырос до 1M токенов (для длинных документов/договоров) — https://www.anthropic.com/news/claude-opus-5
- 2026-07-31 — одобрено — Google AI Overviews: доля ответов прямо в поиске выросла до 43%, влияние на органический трафик сайтов — https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/
- 2026-08-02 — одобрено — Shadow AI: 78% сотрудников используют ИИ с личных аккаунтов, о чём договориться с командой — https://techcrunch.com/2026/07/30/inforcer-raises-50m-to-help-prepare-smbs-for-a-new-world-of-ai-and-security-risks/
- 2026-08-03 — одобрено — Настройка Effort в Claude: какой режим под какие задачи, экономия лимитов — https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
- 2026-08-04 — одобрено — Где ИИ-агенты реально окупаются в малом бизнесе: четыре направления и вопрос про пять часов в неделю — https://vc.ru/biznesiinnovacii/3017901-ii-agenty-v-malom-biznese-chto-realno-rabotayet
- 2026-08-05 — одобрено — ИИ-ресепшионист вместо администратора: Zoom как повод, разбор Mango Office, МТС Бизнес и МегаФона — https://news.zoom.com/standalone-zoom-virtual-agent-receptionist/
- 2026-08-05 — отправлено — Бизнес-помощник в СберБизнесе: наём сотрудника через интернет-банк, вакансия и подбор резюме на Работа.ру — https://bankinform.ru/news/142639
- 2026-08-05 — отправлено — ChatGPT for PowerPoint: бесплатный период заканчивается, дальше расход кредитов — https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes
- 2026-08-06 — отправлено — Авито: ИИ составляет объявление по фотографии товара — https://www.comnews.ru/digital-economy/content/246043/2026-06-26/2026-w26/1012/avito-nauchil-ii-sozdavat-obyavleniya-fotografii
- 2026-08-06 — одобрено — Record a Skill в Cowork: рутину можно показать Claude записью экрана вместо текстовой инструкции; Pro/Max/Team, только Mac — https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- 2026-08-06 — отправлено — Notion: Custom Agent запускается после протокола встречи в AI Meeting Notes — https://www.notion.com/releases/2026-07-31
- 2026-08-07 — отправлено — ПОВТОР темы от 05.08: Бизнес-помощник в СберБизнесе, наём сотрудника — https://www.ng.ru/news/844512.html
- 2026-08-07 — отправлено — ПОВТОР темы от 05.08: ChatGPT for PowerPoint, бесплатный период закончился — https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint
- 2026-08-08 — отправлено — Ozon: пилотный ИИ-ассистент для покупателей, что это значит для карточки товара — https://www.cnews.ru/news/line/2026-08-04_ozon_zapustil_pilotnuyu_versiyu
- 2026-08-08 — отправлено — Google Meet: визуальные скриншоты в автозаметках встречи, настройка админа перед включением — https://workspaceupdates.googleblog.com/2026/08/visual-screenshots-now-included-in-Google-Meet-meeting-notes.html
- 2026-08-08 — отправлено — Yandex AI Studio: агент-исследователь для рутинного поиска информации, кому пригодится — https://www.cnews.ru/news/line/2026-07-14_yandex_b2b_tech_otkryla_biznesu
- 2026-08-08 — отправлено — Битрикс24: голосовой ИИ-агент Марта и модель BitrixGPT 5 сами вводят задачи и заполняют CRM — https://www.bitrix24.ru/journal/novinki-bitriks24-kosmos-agent-marta-ai-bitrixgpt-5-audio-zadachi-ai-i-raspoznavanie-emotsiy/
- 2026-08-08 — одобрено — GPT-5.6 Luna: бесплатный ChatGPT теряет лимит на текстовые сообщения, добавлена кнопка Think — https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/
- 2026-08-08 — одобрено — Claude Cowork на web и mobile: задачу можно начать на компьютере и довести до конца с телефона — https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/
- 2026-08-09 — отправлено — Точка Банк: ИИ-Ассистент селлера собирает отчёт о прибылях для продавцов Wildberries вместо ручного Excel — https://www.cnews.ru/news/line/2026-01-23_tochka_bank_zapustil_ii-assistenta
- 2026-08-09 — отправлено — Контур.Фокус: ИИ-ассистент проверяет контрагента и оценивает риски сделки в диалоге — https://www.cnews.ru/news/line/2025-11-12_konturfokus_sozdal_ii-assistenta
- 2026-08-10 — отправлено — МТС Линк: ИИ-ассистент подбирает шаблон резюме встречи под тип события (планёрка, собеседование, ретроспектива) — https://www.comnews.ru/digital-economy/content/246698/2026-08-03/2026-w32/1012/ii-assistent-mts-link-adaptiruet-rezyume-pod-format-vstrechi
- 2026-08-10 — одобрено — Claude for Small Business: готовые сценарии и навыки для рутины малого бизнеса в Claude Cowork — https://www.anthropic.com/news/claude-for-small-business
- 2026-08-11 — отправлено — amoCRM: тарифы дорожают с 1 сентября, как зафиксировать текущую цену — https://www.amocrm.ru/buy/
- 2026-08-11 — отправлено — ATI.SU: ИИ-ассистент на GigaChat оформляет счета и закрывающие документы для перевозчиков в диалоге — https://www.cnews.ru/news/line/2026-07-06_logisticheskaya_platforma
- 2026-08-12 — одобрено — Anthropic: невидимые водяные знаки в тексте и файлах Claude, что это значит для бизнеса, отдающего клиентам ИИ-контент под своим именем — https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- 2026-08-13 — отправлено — ChatGPT Business: платные Premium-места (5x лимит, без потолка в 5 часов), кому в команде их покупать — https://openai.com/index/premium-seats-chatgpt-business/
- 2026-08-14 — отправлено — Пять личных подписок на нейросети (ChatGPT, Claude, Gemini, Perplexity, Grok) стоят $109,99 в месяц, какой вопрос задать перед оплатой каждой — https://habr.com/ru/companies/syntx_ai/articles/1070110/
- 2026-08-14 — отправлено — Google Meet: «Take notes for me» теперь и для очных встреч, транскрипт и задачи автоматически в Docs — https://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html
- 2026-08-14 — отправлено — Google Таблицы: Sheets canvas превращает данные в канбан-доску или дашборд по текстовому запросу — https://workspaceupdates.googleblog.com/2026/08/use-google-sheets-canvas-to-visualize-data.html
- 2026-08-14 — отправлено — Microsoft объединяет Copilot и M365 Copilot, отключает групповые чаты, подкасты, Copilot Labs и Deep Research до 18 августа — https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/
- 2026-08-14 — отправлено — Mesh (Automattic): бесплатная CRM для контактов на 1000 записей вышла на Android — https://techcrunch.com/2026/08/12/mesh-automattics-crm-for-everyone-comes-to-android/
- 2026-08-15 — отправлено — Битрикс24 Коворк/Код: AI-агент вместо разработчика для внутренних задач и приложений в CRM — https://www.bitrix24.ru/journal/vaybkod-bitrix24-gayd-novichkov/
- 2026-08-15 — отправлено — Циан: интервью ИТ-директора про GPT Gateway и почему 95% внедрений ИИ не окупаются без расчёта ROI — https://www.cnews.ru/reviews/tehnologii_iskusstvennogo_intellekta_1/interviews/maksim_radyukov
- 2026-08-15 — отправлено — Claude Sonnet 5: цена по API $2/$10 за MTok остаётся постоянной, повышения до $3/$15 с 1 сентября не будет — https://platform.claude.com/docs/en/about-claude/pricing
- 2026-08-15 — отправлено — Notion: карточка сравнения моделей ИИ по скорости, качеству и цене вместо списка названий — https://www.notion.com/releases/2026-08-14
- 2026-08-15 — отправлено — Google: можно отключить видимый watermark на AI-изображениях, видео и музыке в Gemini — https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/
- 2026-08-16 — отправлено — ChatGPT Business: функция Computer History запоминает, чем занимался сотрудник на Mac, включает администратор — https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes
- 2026-08-16 — отправлено — Anthropic: сканирование скиллов и плагинов на угрозы в Claude Cowork (бета, Enterprise) — https://support.claude.com/en/articles/15927065-get-started-with-skill-and-plugin-scanning
- 2026-08-16 — отправлено — Notion: документами можно делиться с Custom Agent прямо из меню Share, без настроек агента — https://www.notion.com/releases/2026-08-07
- 2026-08-16 — отправлено — Gemini 3.7 Flash: агентные сценарии в API вдвое дешевле по вводной цене до конца 2026 года — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
- 2026-08-16 — отправлено — OpenAI: программа для малого бизнеса вокруг агента ChatGPT Work, который берёт многошаговые задачи целиком — https://www.inc.com/chloe-aiello/openai-just-unveiled-a-massive-push-to-turn-small-business-owners-into-ai-power-users/91377329
- 2026-08-17 — отправлено — Контур.Фокус: ИИ-анализ договоров с контрагентами за 10 минут вместо ручного изучения — https://www.cnews.ru/news/line/2026-08-11_konturfokus_predstavil
- 2026-08-17 — отправлено — Vibecraft от Яндекса: вайб-кодинг сайтов, который на деле требует Git и SSH-ключи — https://habr.com/ru/articles/1070724/
- 2026-08-18 — отправлено — Китайские LLM (Qwen, GLM, Kimi) в российском бизнесе: потребление выросло в 11,3 раза — https://www.cnews.ru/news/line/2026-08-13_potreblenie_kitajskih_llm
- 2026-08-18 — отправлено — AI Guard: расширение для Chrome маскирует чувствительные данные перед отправкой в ИИ-чат — https://habr.com/ru/articles/1071398/
- 2026-08-18 — отправлено — Google Workspace: Admin Assist приносит Gemini-подсказки прямо в Admin console — http://workspaceupdates.googleblog.com/2026/08/use-gemini-to-help-manage-google-Workspace-for-your-organization.html
- 2026-08-18 — отправлено — Wispr Flow: голосовой ИИ выходит за пределы диктовки, заметки со встреч и модель Canto — https://techcrunch.com/2026/08/17/wispr-raises-280m-at-2b-valuation-as-it-looks-beyond-dictation/
- 2026-08-18 — отправлено — Grok Bot от SpaceXAI: постоянные ИИ-агенты, которые работают в ваших приложениях за $120/мес — https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month
- 2026-08-19 — отправлено — Claude-агент вместо ручных договоров, счетов и актов: skill сокращает сборку комплекта с получаса до минуты — https://vc.ru/ai/3083094-avtomatizatsiya-sozdaniya-dogovorov-i-schetov-s-pomoshchyu-ai-agenta
- 2026-08-19 — отправлено — Навык /design в Claude Code: холст с макетом интерфейса прямо в CLI и десктопе, Pro/Max/Team/Enterprise — https://vc.ru/ai/3084886-anthropic-dobavila-navyk-design-v-claude-code
- 2026-08-19 — отправлено — Google Calendar: блокировка пользователей избавляет от спам-приглашений на встречи насовсем — https://workspaceupdates.googleblog.com/2026/08/managing-unsolicited-event-invitations-with-user-blocking-in-Google-Calendar.html
- 2026-08-20 — отправлено — OpenAI: три деприкации в ChatGPT — браузер Atlas (закрыт 9 августа), модель o3 (уходит 26 августа), DALL·E GPT (удаляется 30 августа) — https://www.notebookcheck.net/ChatGPT-Atlas-ends-on-August-9-Here-s-how-to-save-your-data.1358764.0.html
- 2026-08-20 — отправлено — «Серверное сияние» и СёрчИнформ: ИБ-аутсорсинг для бизнеса Сибири блокирует передачу документов сотрудников во внешние нейросети — https://safe.cnews.ru/news/line/2026-08-13_biznes_sibiri_zashchityat_ot
- 2026-08-20 — отправлено — Google Chat: единый интерфейс «Ask Gemini» с 26 августа заменяет боковую панель Gemini — http://workspaceupdates.googleblog.com/2026/08/ask-gemini-in-chat.html
- 2026-08-20 — отправлено — Calendly: AI-конспектор Notetaker и ассистент Callie вместо отдельной подписки на запись встреч — https://techcrunch.com/2026/08/19/calendly-throws-its-hat-into-meeting-note-taker-circus/
- 2026-08-20 — отправлено — OpenAI: ChatGPT Ads расширяется на 31 европейскую страну с 24 августа — https://dataconomy.com/2026/08/19/openai-chatgpt-ads-launch-european-markets-august-24/
- 2026-08-21 — отправлено — Диасофт: ИИ-агенты в Digital Q.PM автоматизируют планирование, мониторинг и отчётность по проектам — https://www.cnews.ru/news/line/2026-08-20_diasoft_integrirovala
- 2026-08-21 — отправлено — ZeBrains: AI-платформа Artiroute ищет документы по смыслу и создаёт их по шаблону — https://www.cnews.ru/news/line/2026-08-20_zebrains_predstavila_ii-platformu
- 2026-08-21 — отправлено — Скорозвон (Naumen Contact Center): ИИ-тренер переговоров получил женский голос — https://www.cnews.ru/news/line/2026-08-20_v_ii-trenere_skorozvona
- 2026-08-21 — отправлено — Экзон: ИИ находит нужный материал среди 25 тысяч накладных на стройплощадке — https://www.cnews.ru/news/line/2026-08-20_ii_v_ekzon_nahodit_igolku
- 2026-08-21 — отправлено — Anthropic: коннектор к Economic Index отвечает на вопросы об использовании ИИ по профессиям — https://www.anthropic.com/news/anthropic-economic-index-connector
- 2026-08-21 — отправлено — Anthropic: Inference hooks для Claude Enterprise проверяют промпты сотрудников до выполнения — https://platform.claude.com/docs/en/manage-claude/inference-hooks
- 2026-08-21 — отправлено — Anthropic: Compliance API выгружает транскрипты сессий Cowork и Claude Code для аудита — https://platform.claude.com/docs/en/manage-claude/compliance-sessions
- 2026-08-21 — отправлено — Notion: ИИ-заметки со встреч автоматически запускают кастомных агентов — https://www.notion.com/releases/2026-07-31
- 2026-08-21 — отправлено — Notion: расход AI-агентов Workers виден в общем дашборде кредитов — https://www.notion.com/releases/2026-07-24
- 2026-08-21 — отправлено — Google Chat: отчёты по использованию Gemini показывают администратору реальную вовлечённость команды — http://workspaceupdates.googleblog.com/2026/08/view-google-chat-usage-metrics-in-Gemini-reports-dashboard.html
- 2026-08-21 — отправлено — Google Slides: запись презентаций с автоозвучкой через интеграцию с Google Vids — http://workspaceupdates.googleblog.com/2026/08/record-presentations-in-Google-Slides-with-Google-Vids.html
- 2026-08-21 — отправлено — Google Workspace Studio: новые контролы ограничивают доступ Gemini к данным Drive для no-code агентов — http://workspaceupdates.googleblog.com/2026/08/new-enterprise-security-controls-for-Workspace-Studio-enable-expanded-collaboration-use-cases.html
- 2026-08-21 — отправлено — Meta: AI-приложение для Mac объединяет аналитику рекламы, почту и документы для малого бизнеса — https://techcrunch.com/2026/08/20/meta-ais-new-mac-app-wants-you-to-talk-to-your-apps/
- 2026-08-21 — отправлено — Ramp: AI-роутер Router переключает модели разных провайдеров с единым дашбордом трат — https://techcrunch.com/2026/08/20/ramp-launches-its-own-ai-model-router-called-router/
- 2026-08-21 — отправлено — Cursor: платформа хостинга кода Origin как альтернатива GitHub — https://techcrunch.com/2026/08/18/cursor-capitalizes-on-github-frustration-launches-rival-hosting-platform/
- 2026-08-21 — отправлено — OpenAI: Private Safety Processing защищает корпоративных клиентов API без хранения переписки — https://techcrunch.com/2026/08/19/openai-seeks-to-one-up-anthropic-with-new-customer-privacy-protections/
- 2026-08-21 — отправлено — Google: кнопка «Preferred Sources» помогает издателям вернуть видимость в ИИ-поиске — https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/
- 2026-08-21 — отправлено — Snowflake: Cortex AI Gateway контролирует расходы на ИИ-агентов по командам — https://siliconangle.com/2026/07/28/snowflake-debuts-cortex-ai-gateway-govern-monitor-enterprise-ai-agents/
- 2026-08-21 — отправлено — Google DeepMind: открытые модели Gemma преодолели 1 млрд загрузок — https://blog.google/innovation-and-ai/technology/developers-tools/gemma-one-billion-downloads/
- 2026-08-21 — отправлено — Google DeepMind: модель SL2T переводит жестовый язык в текст на Pixel 11 — https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/
- 2026-08-21 — отправлено — Google DeepMind: WeatherNext предупреждает о циклоне на день раньше — https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/
- 2026-08-21 — отправлено — Google Labs: Lyria 3.5 в Flow Music улучшает генерацию музыки для рекламы — https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/
- 2026-08-21 — отправлено — OpenAI: Ultrafast mode для GPT-5.6 Sol на чипах Cerebras ускоряет ответы до 14 раз — https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai
- 2026-08-22 — отправлено — Wildberries: «Анализ внимания» показывает тепловую карту и заметность элементов фото карточки товара — https://www.cnews.ru/news/line/2026-08-21_wildberries_zapustila_ii-servis
- 2026-08-22 — отправлено — Wildberries: ИИ-сравнение товаров теперь строится на отзывах и вопросах покупателей, а не только на характеристиках — https://www.cnews.ru/news/line/2026-08-21_wildberries_vypustila_krupnoe
- 2026-08-22 — отправлено — Яндекс: продавцы без сайта получают заказы из Поиска и чата с Алисой через Yandex Commerce Protocol — https://www.cnews.ru/news/line/2026-08-21_prodavtsy_bez_sajtov_teper
- 2026-08-22 — отправлено — Anthropic: в Claude Managed Agents появился жёсткий денежный лимит на сессию ИИ-агента — https://platform.claude.com/docs/en/managed-agents/budgets
- 2026-08-22 — отправлено — Google Workspace: Gemini Notebook можно скопировать целиком, источники можно добавлять автоматически — https://workspaceupdates.googleblog.com/2026/08/make-copy-of-notebook-in-gemini-notebook.html
- 2026-08-22 — отправлено — Google: Environment Hooks в Gemini API позволяют проверять действия ИИ-агента до и после выполнения — https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/
- 2026-08-22 — отправлено — OpenAI: модели кибербезопасности Daybreak Red и Daybreak Blue доступны на Amazon Bedrock — https://aws.amazon.com/about-aws/whats-new/2026/08/openai-daybreak-red-and-blue-on-amazon-bedrock/
- 2026-08-23 — отправлено — МТС Web Services (MWS Cloud): средняя стоимость внедрения ИИ в России выросла почти втрое, с 13,7 до 38,8 млн рублей — https://www.cnews.ru/news/top/2026-08-19_eksperty_zafiksirovali_pochti
- 2026-08-23 — отправлено — ИИ окупается там, где есть свои данные и прямая связь с прибылью: разбор на примере Сбера, Т-Банка и Bank of America — https://vc.ru/ai/3091233-ii-v-bankah-prinosit-pribyl
- 2026-08-23 — отправлено — Свой MCP-сервер за двадцать минут: как подключить Claude и Cursor к своей базе данных без REST-бэкенда — https://vc.ru/ai/3090104-kak-podklyuchit-claude-i-cursor-k-mcp-serveru
- 2026-08-23 — отправлено — Google Workspace: Allowlisted Domains API управляет списком доверенных доменов программно вместо ручной консоли — https://workspaceupdates.googleblog.com/2026/08/allowlisted-domains-api-now-generally-available.html
- 2026-08-23 — отправлено — Anthropic: Claude Managed Agents подгружает skills прямо из GitHub-репозитория команды — https://platform.claude.com/docs/en/managed-agents/skills#load-skills-from-a-github-repository
- 2026-08-24 — отправлено — Т2: ИИ-витрина «Элюмента» даёт единое окно доступа к 50+ нейросетям с оплатой с баланса телефона — https://www.cnews.ru/news/line/2026-08-13_t2_zapuskaet_edinoe_okno
- 2026-08-24 — отправлено — BSS: «Речевая аналитика» 2.15 — встроенный ИИ стал автономным агентом, сам разбирает звонки по расписанию — https://www.cnews.ru/news/line/2026-08-10_bss_perevela_rechevuyu_analitiku
- 2026-08-25 — отправлено — GigaChat Ultra: голосовой диалог в приложении вместо ввода текста — https://giga.chat/help/articles/voice-input
- 2026-08-25 — отправлено — Habr (alpinadigital): успех ИИ-трансформации держится на одном мотивированном человеке в команде, а не на бюджете — https://habr.com/ru/companies/alpinadigital/articles/1066708/
- 2026-08-25 — отправлено — ChatGPT Business: доплата за новое место теперь списывается сразу, а не в следующем счёте — https://help.openai.com/en/articles/8792536-managing-billing-and-seats-in-chatgpt-business
- 2026-08-25 — отправлено — Instinct: персональный ИИ-ассистент с широким доступом к данным и риском для приватности — https://techcrunch.com/2026/08/24/instincts-powerful-ai-assistant-is-raising-privacy-and-security-concerns/
- 2026-08-25 — отправлено — Inc.com: 55% руководителей жалеют об увольнениях под предлогом замены ИИ, волна тихого возврата к найму — https://www.inc.com/bruce-crumley/55-percent-of-leaders-regret-ai-layoffs-and-a-major-hiring-reversal-has-begun/91380901
- 2026-08-25 — отправлено — Axios: роль AI enablement lead для точечного внедрения ИИ по одному отделу за раз — https://www.axios.com/2026/07/27/ai-enablement-plan-companies-ceos
- 2026-08-25 — отправлено — Notion: раздел Developer в сайдбаре объединяет управление Workers, подключениями и токенами — https://www.notion.com/releases/2026-08-19
- 2026-08-25 — отправлено — Google Gemini: интерактивные 3D-визуализации и симуляции по текстовому запросу — http://workspaceupdates.googleblog.com/2026/08/generate-interactive-simulations-and-models-in-the-Gemini-app.html
- 2026-08-25 — отправлено — Anthropic: safety-классификаторы Claude Fable 5 по биологии стали реже отказывать на легитимные вопросы — https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards
- 2026-08-25 — отправлено — Anthropic × Cognizant: расширенное партнёрство, автоматизация проверки договоров сократила обработку на 40% — https://www.anthropic.com/news/cognizant-anthropic
