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
