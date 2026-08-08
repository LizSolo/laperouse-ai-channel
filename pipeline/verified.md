# Проверенные факты — черновики за 2026-08-08 (второй прогон)

WebFetch в этой сессии заблокирован на всех проверенных внешних доменах, включая
`workspaceupdates.googleblog.com`, `www.forbes.ru`, `www.content-review.com` (везде
`EGRESS_BLOCKED`). Факты ниже собраны кросс-проверкой через WebSearch по нескольким
независимым публикациям на разных доменах, как предписывает `prompts/author.md`, ШАГ 3.

---

## Тема 1. Google Meet: визуальные скриншоты в автозаметках встречи

Первоисточник (официальный анонс Google Workspace): «Google Workspace Updates: Visual
screenshots now included in Google Meet meeting notes»,
https://workspaceupdates.googleblog.com/2026/08/visual-screenshots-now-included-in-Google-Meet-meeting-notes.html
(содержание получено через сниппет WebSearch, сам домен блокирован для WebFetch).

Второй независимый источник: Android Authority,
https://www.androidauthority.com/google-meet-notes-screenshots-3691613/

Дополнительно сверено (совпадает): Neowin
(https://www.neowin.net/news/google-meets-ai-note-taker-will-soon-start-including-presentation-screenshots/),
Chrome Unboxed
(https://chromeunboxed.com/google-meet-is-adding-visual-screenshots-to-gemini-meeting-notes/).

Факты (совпадают во всех источниках, расхождений нет):
- Функция «Вести заметки за меня» (Gemini-заметки) в Google Meet теперь автоматически
  добавляет в документ заметок скриншоты того, что показывали на экране во время созвона
  (слайды, графики, диаграммы), рядом с текстовым пересказом и расшифровкой.
- Постепенный раскат начался 3 августа 2026 года, для Rapid Release и Scheduled Release
  доменов, и займёт до 15 дней до появления у всех пользователей.
- Доступно на тарифах Google Workspace Business Standard, Business Plus, Enterprise
  Standard, Enterprise Plus и Google AI Pro for Education.
- На тарифе Business Starter (и в бесплатных личных аккаунтах) функции «Вести заметки за
  меня» в принципе нет, поэтому и скриншотов там нет — подтверждено отдельным поиском
  специально по Business Starter.
- Администратор домена может настроить режим по умолчанию: разрешить скриншоты презентаций
  всегда, когда идут заметки (стандартная настройка), либо только для встреч с включённой
  записью.
- Докладчик и другие участники видят уведомление о том, что Gemini может делать скриншоты
  показанного контента, и могут отключить это прямо в панели заметок во время встречи.
- Цены за тарифы Workspace в материалах об этой функции не упоминаются — цифр цены в пост
  не включалось, F-05 неприменимо к этой теме.

Дополнительно проверено для T-05 (доступность сервиса из России): Google Workspace
регистрируется и работает из России, прямая оплата российской картой недоступна, но
официальный реселлер Softline оформляет подписку в рублях (подтверждено официальной справкой
Google, https://support.google.com/a/answer/3138662, и независимо — Softline,
https://docs.softline.com/ru-ru/subscriptions/google-workspace). Это указано в посте прямым
текстом.

## Тема 2. Yandex AI Studio: агент-исследователь для бизнеса

Первоисточник: CNews, https://www.cnews.ru/news/line/2026-07-14_yandex_b2b_tech_otkryla_biznesu
(содержание получено через сниппет WebSearch, домен ранее отмечен как блокируемый для
WebFetch в этой среде).

Второй независимый источник: TAdviser,
https://www.tadviser.ru/index.php/%D0%9F%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82:Yandex_AI_Studio

Дополнительно сверено (совпадает дословно по цифрам): Forbes.ru
(https://www.forbes.ru/tekhnologii/551024-izvne-i-vnutri-andeks-predlozil-biznesu-delat-ii-agentov-dla-poiska-v-internete),
Content-Review (https://www.content-review.com/articles/75481/), Rambler
(https://news.rambler.ru/tech/56751970-yandeks-pozvolit-biznesu-sozdavat-ii-agentov-dlya-issledovaniy-i-analiza/).

Факты (совпадают во всех источниках, расхождений в цифрах нет):
- Yandex B2B Tech открыла бизнесу доступ к созданию собственных ИИ-агентов для исследований
  на платформе Yandex AI Studio. Дата открытия доступа — 14 июля 2026 года (тема старше
  недели на момент публикации поста, T-07: в пост дата и слова «вышло»/«на днях»/«недавно» не
  включены, подача сделана вне привязки ко времени, как разбор существующего инструмента).
- Агент собирается через обновлённый инструмент Web Search в AI Studio: сам формулирует
  поисковые запросы, ищет информацию в открытом интернете и во внутренних источниках
  компании, анализирует и присылает структурированный ответ — текстом или в виде
  презентации.
- Web Search в AI Studio уже используют более 11 тысяч компаний, которые вместе отправляют
  около 400 тысяч запросов в месяц.
- Указанные в источниках сценарии применения: маркетологам — для конкурентного анализа и
  мониторинга репутации бренда; HR-специалистам — для исследования рынка кандидатов и
  подготовки портрета соискателя.
- Цены на использование Web Search/AI Studio в найденных материалах не названы конкретной
  суммой — цифр цены в пост не включалось, F-05 неприменимо.

## Что не пошло в пост

Кандидаты, отсеянные до этого шага (Wildberries, Sonnet 5 промо-цена, self-hosted runners,
универсальный агент Yandex B2B Tech, раунды инвестиций, Mango Office) — с указанием ID и
причины в `pipeline/funnel.md`.
