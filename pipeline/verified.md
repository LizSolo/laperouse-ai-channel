# Проверенные факты за 2026-08-27

По каждой теме: первоисточник, подтверждение, факты. Числа отсюда сверяет `pipeline/lint.py`
(F-04) — каждое число в посте должно быть здесь.

---

## 1. Slack Code

Первоисточник: https://venturebeat.com/orchestration/slack-wants-to-drag-ai-coding-out-of-the-terminal-and-into-the-group-chat (403 для WebFetch, подтверждён через WebSearch).
Подтверждение: https://www.theregister.com/saas/2026/08/20/slack-code-taps-into-collective-vibe-puts-ai-agents-into-the-group-chat/5290413, unite.ai, dataconomy.com — совпадают дословно.

Факты: продукт Slack Code запущен 20 августа 2026, доступен на любом тарифе Slack сразу с запуска.
Пользователь тегает агента (Claude Code, Devin, GitHub Copilot, ChatGPT, агент Vercel) в чате —
агент открывает отдельный код-канал с дифами кода, живыми превью и планом работы. Участники
оставляют фидбэк, агент его учитывает. После завершения задачи канал автоархивируется, остаётся
аудиторский лог. Цены отдельно не объявлены — фича идёт в комплекте с существующим тарифом Slack.

## 2. Serval Catalyst

Первоисточник: https://venturebeat.com/infrastructure/servals-super-agent-catalyst-creates-roving-background-agents-to-identify-and-fix-it-issues-before-theyre-ticketed (403, подтверждён через WebSearch).
Подтверждение: https://www.citybiz.co/article/892200/serval-launches-catalyst-ai-agent-to-build-and-manage-enterprise-automations/, dealroom.co.

Факты: Catalyst от Serval вышел в общий доступ 20 августа 2026 поверх AI-native платформы Serval
для service management. Анализирует историю тикетов, SOP и инструкции на естественном языке, сам
строит workflow, скиллы, формы, политики доступа и дашборды. Фоновые агенты работают по расписанию
по подключённым системам и предлагают ремедиацию до того, как заведён тикет (пример: сопоставил
инциденты в двух офисах по switch-телеметрии, DHCP-данным и истории тикетов, нашёл configuration
drift, сгенерировал workflow на утверждение). Цены отдельно не публиковались.

## 3. Writer, экономия токенов через харнесс

Первоисточник: https://techcrunch.com/2026/08/13/writer-introduces-new-ai-model-and-upgraded-harness-to-contain-token-costs/ (открыт целиком).
Подтверждение: VentureBeat, «Writer says its new Palmyra X6 model cuts AI agent costs by 52%…».

Факты: Writer выпустил модель Palmyra X6 (на базе GLM-5.2) вместе с апгрейдом «харнесса» —
инфраструктурного слоя оркестрации агента, 13 августа 2026. По собственному исследованию Writer
(«The Harness Effect»): изменения только в харнессе, без смены модели, снижают расходы в среднем
на 41%, для базовых задач — до 50%, ускоряют выполнение задач на 44%. Эффект проявляется на любой
модели, включая сторонние (Anthropic, OpenAI). Комбинация новой модели и харнесса вместе даёт
снижение costs на 52%, ускорение на 48%.

## 4. Claude, текстовый водяной знак для EU AI Act

Первоисточник: https://www.anthropic.com/news/claude-text-watermark (открыт целиком).
Подтверждение: https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/, плюс CNN, Gizmodo, Euronews — все датируют 11 августа 2026.

Факты: Anthropic с 11 августа 2026 встраивает машиночитаемый водяной знак в текстовые ответы
будущих моделей Claude, начиная с моделей, выпущенных с 2 августа 2026 — в контексте требований
статьи 50 EU AI Act. В июле 2026 Anthropic вместе с около 190 другими компаниями подписала
добровольный EU Code of Practice on Transparency of AI-Generated Content. Метка невидима, не меняет
качество вывода, не добавляет стоимости, сохраняется при копировании текста, слабее на коротких
фактических текстах и коде. Работает глобально, не только в ЕС, через API, приложения, Claude Code
и Cowork. Для изображений — отдельно, через метаданные C2PA.

## 5. OpenAI, плагины для обучения в ChatGPT Work и Codex

Первоисточник: https://openai.com/index/learn-teach-chatgpt-work-codex/ (403, подтверждён через WebSearch).
Подтверждение: https://www.techrepublic.com/article/news-openai-chatgpt-education-plugins/, edtechinnovationhub.com.

Факты: OpenAI выпустила 4 августа 2026 три плагина-роли — учитель К-12 (планирование уроков),
студент колледжа (конспекты в квизы, флеш-карты, гид-тьютор), преподаватель колледжа
(административные workflow вузов). Доступны через ChatGPT Edu и ChatGPT for Teachers
(district-развёртывания), а не через обычный ChatGPT Work/Business.

## 6. ChatGPT Business, конец бесплатного периода агентных функций

Первоисточник: https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes (403, подтверждён через WebSearch по нескольким агрегаторам, дословно повторяющим текст release notes).

Факты: использование агентных функций ChatGPT Business — Workspace Agents, ChatGPT for
Excel/PowerPoint — было бесплатным до 6 августа 2026 включительно. С 7 августа расход списывается
из общего пула кредитов воркспейса по flexible-pricing модели. Сама подписка ChatGPT Business (не
агентные функции) как была платной, $20-25 за место в месяц, так и осталась — бесплатным был именно
расход агентных функций, а не тариф целиком. У Enterprise/Edu аналогичный бесплатный период
закончился раньше, 6 июля 2026 — это другая, более ранняя дата.

## 7. Claude, Opus 4.1 отключён от API

Первоисточник: https://platform.claude.com/docs/en/release-notes/overview (открыт целиком).
Подтверждение: https://therouter.ai/news/anthropic-deprecates-claude-opus-4-1-august-5-migration-guide/, totalum.app/blog/claude-4-deprecation-migration-2026.

Факты: 5 августа 2026 Anthropic отключила Claude Opus 4.1 (`claude-opus-4-1-20250805`) от API — все
запросы к этой модели теперь возвращают ошибку. Официальная рекомендация — переходить на Claude
Opus 5 (в июне 2026, при анонсе будущего отключения, рекомендовали Opus 4.8 — но с тех пор вышла
более новая модель, и итоговая рекомендация сменилась).

## 8-9. Google Docs, Gemini резюмирует комментарии + рисует диаграммы

Первоисточник: https://workspaceupdates.googleblog.com/2026/07/ (открыт целиком, обе записи датированы 28 июля 2026).
Подтверждение: https://tech.yahoo.com/ai/gemini/articles/overwhelmed-comments-google-docs-ask-210554481.html, https://chromeunboxed.com/gemini-can-now-generate-diagrams-and-infographics-directly-inside-google-docs/.

Факты (комментарии): Gemini читает и суммирует треды комментариев в Google Docs, выделяет ключевые
темы, находит нерешённые блокирующие вопросы, может сгенерировать ответ или черновик реплики от
имени пользователя. Пример запроса: «Summarize all comments from Sarah».

Факты (визуалы): Gemini создаёт изображения, диаграммы и инфографику прямо в документе с учётом
его контекста, редактирует их по запросу на естественном языке.

Раскатка обеих функций — с 28 июля 2026, на Rapid Release и Scheduled Release доменах одновременно,
полная видимость — в течение до 15 дней.

## 10. Google Forms, Gemini собирает квиз по файлам Drive

Первоисточник: https://workspaceupdates.googleblog.com/2026/07/ (запись от 30 июля 2026, открыт целиком).
Подтверждение: https://chromeunboxed.com/how-google-forms-auto-generated-custom-quizzes-will-help-my-kids-study-better-this-year/, teachercast.net.

Факты: функция «Help me create» в Google Forms генерирует квизы по файлам, прикреплённым из Google
Drive (Docs, Slides, PDF) — Gemini анализирует контент и сам предлагает вопросы, типы вопросов и
варианты ответов с готовыми правильными ответами. Раскатка с 24 июля 2026 для Rapid Release, с
5 августа 2026 — для Scheduled Release. Требуется Google Workspace Business Standard, Business Plus
или Enterprise плюс платная надстройка Google AI Pro или Google AI Ultra.

## 11. Google Workspace, Gemini Admin Assist

Первоисточник: https://workspaceupdates.googleblog.com/2026/08/ (запись от 17 августа 2026, открыт целиком).
Подтверждение: https://knowledge.workspace.google.com/admin/getting-started/side-panel-in-the-admin-console (официальная справка Google, независимая страница).

Факты: две функции в консоли администратора — Sidepanel (доступен через One Google Bar почти на
всех страницах консоли, супер-админы получают пошаговые инструкции и best practices) и Search
Overviews (Gemini синтезирует статьи Справочного центра в связный ответ с рекомендованными
следующими шагами). Доступно только для редакций Business (Starter, Standard, Plus), только
супер-админам, не делегированным. Включено по умолчанию для подходящих редакций.

## 12. Perplexity Portable Computer

Первоисточник: https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs (EGRESS_BLOCKED, подтверждён через WebSearch).
Подтверждение: siliconangle.com, thenewstack.io, root-nation.com, biggo.com, slashdot.org — согласованные детали в 5+ изданиях.

Факты: Perplexity вместе с Nvidia выпустила Portable Computer — агент, который теперь может
работать полностью локально на Nvidia DGX Spark и на Linux-машинах с видеокартой Nvidia RTX (от
24 ГБ видеопамяти, ориентир — RTX 3090 и новее). Использует локальные модели (Qwen и
дообученную Perplexity модель PPLX). «Нулевая стоимость токенов» — только для шагов, выполненных
локально; если задача уходит в облачную модель, система спрашивает разрешение и списывает обычные
кредиты подписки. Сейчас доступно на Linux, на Windows — с сентября 2026, для Mac поддержка не
анонсирована. Нужна подписка Perplexity Pro, Max, Enterprise Pro или Enterprise Max.

## 13. Radar, поиск по подкастам для ИИ-агентов

Первоисточник: https://techcrunch.com/2026/08/26/radar-makes-podcasts-searchable-and-usable-by-ai-agents/ (открыт целиком).
Подтверждение: myustimes.com, плюс независимый поиск по цене и биографии CEO (Crunchbase/LinkedIn).

Факты: продукт Radar от компании Particle, статья от 26 августа 2026. Индексирует более 130 000
подкастов, включая весь Apple Top 200, добавляет 20 000 новых эпизодов ежедневно. Поиск по
содержанию с атрибуцией спикеров, отслеживание упоминаний брендов/людей/продуктов, алерты через
email/Slack/webhook, извлечение цитат с таймкодами. Бизнес-тариф — $399 в месяц за 20 мест, личный
тариф — $29 в месяц. Есть API и MCP-сервер для AI-агентов.

## 14. Gemini 3.5 Transcribe

Первоисточник: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/ (открыт целиком, 26 августа 2026).
Подтверждение: 9to5google.com, androidauthority.com — совпадающие цифры WER и число языков.

Факты: две версии — потоковая и для записи. Убирает слова-паразиты, автоматически форматирует
текст, сглаживает самокоррекции. Определяет до трёх спикеров с таймкодами в записанном аудио.
Поддерживает пользовательский словарь терминов. Автоматически определяет и транскрибирует более
85 языков. WER (доля ошибок распознавания): 4,0% в потоковом режиме, 2,6% в режиме записи.

## 15. Gemini Live, Spark и Daily Brief

Первоисточник: https://blog.google/innovation-and-ai/products/gemini-app/productivity-features-gemini-live/ (открыт целиком, 26 августа 2026).
Подтверждение: 9to5google.com, androidauthority.com.

Факты: Spark — функция Gemini Live, по голосовой команде запускает многошаговые задачи в
Google Docs, Sheets, Drive и вебе, которые выполняются самостоятельно, без участия пользователя, в
течение дней и недель. Например: голосом надиктовать сырые мысли — Spark оформит их в
структурированный документ Docs. Daily Brief — отдельный агент, ночью готовит голосовую сводку по
почте и календарю с рекомендованными следующими шагами. Spark требует подписку Google AI Pro или
выше, Daily Brief — Google AI Plus или выше.

## 16. OpenAI, Admin plugin для ChatGPT Work и Codex

Первоисточник: https://openai.com/index/introducing-admin-plugin/ (403, подтверждён через WebSearch).
Подтверждение: 9to5mac.com, investing.com, itbrief.com — согласованные формулировки в 4+ изданиях.

Факты: анонс от 25 августа 2026. Плагин Admin для ChatGPT Work и Codex в одном диалоге: смотрит
активность и расход кредитов, выявляет, кто близок к лимиту, добавляет/удаляет участников,
онбординг/офбординг, управляет доступом и правами по ролям/группам, корректирует лимиты трат,
одобряет или отклоняет запросы на трату. ChatGPT Work — агентская функция ChatGPT (не отдельный
тариф), доступная в рамках платных тарифов Business/Enterprise/Edu — именно для их админов и
предназначен плагин.

## 17. GPT-5.6 Sol, снижение цены

Первоисточник: https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/ (заблокирован для WebFetch, подтверждён через WebSearch).
Подтверждение: https://winbuzzer.com/2026/08/23/openai-cuts-gpt-5-6-sol-api-prices-by-up-to-33-percent-through-november-21-xcxwbn/, citybiz.co, aol.com.

Факты: анонс от 21 августа 2026. Вход: $5 → $4 за млн токенов (−20%). Выход: $30 → $20 за млн
токенов (−33%). Кэшированный вход: $0,50 → $0,40 за млн токенов (−20%). Акция действует минимум до
21 ноября 2026. Распространяется на API, кредиты Codex, часть тарифов ChatGPT Work. Подписки Pro,
Plus, Business цену не меняют.

## 18. MIT Technology Review, AI Observatory

Первоисточник: https://www.technologyreview.com/2026/08/18/1142226/how-people-use-ai/ (заблокирован для WebFetch, подтверждён через WebSearch и препринт).
Подтверждение: https://www.washingtonpost.com/business/2026/08/18/ai-observatory-tries-reveal-how-people-really-use-technology/ (независимая редакция, та же дата), https://www.dataprovenance.org/ai_observatory.pdf.

Факты: проект AI Observatory — команда исследователей MIT, Stanford и University of Maryland
(со-первые авторы Shayne Longpre, Anka Reuel, Dayeon Ki), публикация 18 августа 2026. Агрегировал
85 633 диалоговых реплики в 24 521 переписке от 5000 пользователей, охватывающих 52 модели (ChatGPT,
Gemini, Claude, Grok и другие) из 7 существующих датасетов за 2023-2025. Показывает значительно
больше «непрофильных», личных сценариев использования, чем отражено в публичных отчётах
Anthropic/OpenAI, которые фокусируются на рабочем использовании. Около 47,9% диалогов
классифицированы как не связанные с профессиональной деятельностью. Различия по провайдерам:
Anthropic чаще используют для кода, Gemini — для социальных сценариев, ChatGPT — для домашних
заданий.
