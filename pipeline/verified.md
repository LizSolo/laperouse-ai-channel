# Проверка фактов за 2026-09-15

## Тема 1. Microsoft 365 Copilot: администратор видит веб-поиск сотрудника

Первоисточник: https://habr.com/ru/articles/1080960/ (открыт целиком через WebFetch, разбор
официального анонса Microsoft). Подтверждение: официальная документация Microsoft Learn
«Data, privacy, and security for web search in Microsoft Copilot and Microsoft Copilot Chat»
(learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access) и запись в блоге
techcommunity.microsoft.com «Introducing greater transparency and control for web search
queries in Microsoft 365 Copilot and Microsoft 365 Copilot Chat» — оба домена штатно закрыты
egress-прокси (EGRESS_BLOCKED), факты собраны перекрёстно через WebSearch и дословно совпадают
с habr.

Факты:
- В Microsoft Purview Activity Explorer (Data Security Posture Management for AI) администратор
  теперь видит точную поисковую фразу, которую Copilot отправил в Bing, рядом с исходным
  промптом пользователя и ответом.
- Добавлен отдельный фильтр в Activity Explorer для поиска именно тех обращений, где Copilot
  использовал веб-поиск.
- Веб-поиск в Copilot включён по умолчанию и остаётся включённым, пока администратор явно не
  отключит его политикой Cloud Policy «Allow web search in Copilot».
- Сотрудник видит источники и точный поисковый запрос только в Microsoft Copilot Chat, и только
  в течение 24 часов после ответа.
- В панели Copilot внутри приложений Microsoft 365 (Word, PowerPoint и так далее) ссылки на
  источники веб-поиска не показываются вовсе.
- Официальные лицензии Microsoft 365 (в том числе с Copilot) новым клиентам в России не
  продаются.

## Тема 2. Higgsfield: плагин ChatGPT для анимации в Adobe After Effects

Первоисточник: https://vc.ru/ai/3137227-animatsiya-v-after-effects-s-pomoshchyu-chatgpt-ot-higgsfield
(открыт целиком через WebFetch). Подтверждение: официальный блог higgsfield.ai
(higgsfield.ai/blog/ai-motion-designer-after-effects-gpt, higgsfield.ai/blog/higgsfield-after-effects)
и независимое издание startupfortune.com (оба найдены через WebSearch, детали совпадают).

Факты:
- Higgsfield выпустила плагин AI Motion Designer, который работает внутри ChatGPT и напрямую в
  Adobe After Effects и Premiere Pro.
- Пользователь устанавливает плагин Higgsfield в ChatGPT и текстовой командой (например,
  «сделай анимацию логотипа») запускает построение анимации прямо в открытом проекте.
- Агент сам создаёт слои, тайминг и ключевые кадры в композиции.
- Результат остаётся обычными редактируемыми элементами After Effects: текст, цвет, слои,
  тайминг и кривые анимации можно поправить вручную, как в любом другом проекте.
- Для работы нужны подписка на ChatGPT (плагин Higgsfield) и лицензия Adobe After Effects или
  Premiere Pro.
- Прямая оплата подписок ChatGPT и Adobe банковской картой из России не проходит.

## Тема 3. Claudeforce: Salesforce внутри Claude

Первоисточник: пресс-релиз Salesforce и Anthropic от 26 августа 2026
(https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/)
— домен штатно закрыт egress-прокси (EGRESS_BLOCKED). Факты собраны перекрёстно через WebSearch
по трём независимым публикациям: ppc.land («Salesforce puts 37 prebuilt sales skills inside
Claude for pilot customers»), salesforceben.com («Salesforce and Anthropic Announce Claudeforce
in Q2 '27 Earnings») и vantagepoint.io («Claudeforce: What the Salesforce-Anthropic Partnership
Means») — цифры и даты совпадают дословно во всех трёх.

Факты:
- Salesforce и Anthropic объявили партнёрство Claudeforce 26 августа 2026 года.
- Первый продукт партнёрства — плагин «Salesforce in Claude» с 37 готовыми навыками продавца:
  подготовка к встрече, разбор здоровья сделки, обзор воронки, черновик письма клиенту и
  обновление карточки CRM.
- Продавец работает с живыми данными CRM прямо в диалоге с Claude, без захода в само приложение
  Salesforce; права доступа и правила governance Salesforce при этом сохраняются.
- Плагин уже доступен отдельным пилотным клиентам, открытая бета запускается в сентябре 2026
  года.
- Дополнительные навыки для сервиса, маркетинга и коммерции запланированы на конец 2026 года.
- Партнёрство включает четыре направления: плагин Salesforce внутри Claude, Claude внутри
  продуктов Salesforce, Claude как модель по умолчанию в Slack и встречное коммерческое
  соглашение между компаниями.
- Прямой доступ к Salesforce для российских компаний закрыт: сервис не работает с российскими
  юрлицами из-за санкционных ограничений.

## Тема 4. Как классифицировать отзывы клиентов через нейросеть с цитатами

Первоисточник: https://vc.ru/ai/3130637-analiz-otzyvov-klientov-s-pomoshchyu-ii (открыт целиком
через WebFetch; это авторская методика, а не пересказ чужой новости, независимое второе
подтверждение не требуется — факты не о внешнем событии, а об изложенном в самой статье методе,
проверены цитированием оригинала).

Факты:
- Метод: собрать все отзывы в один файл с датой, оценкой и полным текстом, убрать дубликаты и
  пронумеровать каждый отзыв.
- На обучающей партии отзывов нейросети дают задачу самой выделить повторяющиеся категории
  проблем, а не подгонять их под заранее заданный список.
- Для каждой найденной проблемы модель обязана привести точную цитату из отзыва, чтобы вывод
  можно было проверить по исходному тексту.
- Автор демонстрирует метод на 6 учебных отзывах (обозначены R01–R06): жалоба на задержку
  доставки нашлась в 2 из них.
- Итоговый подсчёт ведётся по количеству уникальных отзывов в каждой категории, а не по общему
  впечатлению вроде «плохой сервис».
