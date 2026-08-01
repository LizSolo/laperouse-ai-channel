# Проверенные факты — черновики за 2026-08-01

## Ограничение окружения (важно для редактора)

В этой сессии инструмент WebFetch и прямой curl к любым внешним хостам (включая anthropic.com, openai.com, example.com, google.com) возвращают 403 от прокси окружения — `curl -sS "$HTTPS_PROXY/__agentproxy/status"` показывает `recentRelayFailures` с `"gateway answered 403 to CONNECT (policy denial or upstream failure)"` для всех проверенных хостов без исключения. Это сетевая политика окружения (см. `/root/.ccr/README.md`: "403/407 from the proxy... do not retry or route around it"), не сбой конкретного сайта. WebSearch при этом работает нормально.

Из-за этого факты ниже проверены НЕ прямым открытием первоисточника через WebFetch (как требует обычный процесс), а перекрёстной проверкой через WebSearch по 8+ независимым публикациям одной и той же новости (включая пресс-релиз компании через BusinessWire/PR Newswire, TechCrunch, Yahoo Finance, citybiz, SiliconANGLE, TheAIInsider, DealStreetAsia, Whalesbook) — цифры совпадают дословно во всех источниках, расхождений не найдено.

## Новость: Emergent — раунд Series C, $130 млн, оценка $1,5 млрд

Основной источник (официальный пресс-релиз компании через BusinessWire):
https://www.businesswire.com/news/home/20260715082819/en/Emergent-Raises-Series-C-at-$1.5B-Valuation-to-Help-Entrepreneurs-and-SMBs-Build-the-Software-Their-Businesses-Run-On

Подтверждающие независимые источники:
- https://techcrunch.com/2026/07/15/indian-ai-coding-startup-emergent-becomes-a-unicorn-just-over-a-year-after-launch/
- https://www.citybiz.co/article/874754/emergent-raises-130-million-series-c-at-1-5-billion-valuation/
- https://theaiinsider.tech/2026/07/28/emergent-closes-series-c-at-1-5b-valuation-becomes-unicorn-in-a-year-of-launch/
- https://siliconangle.com/2026/07/15/emergent-emerges-latest-ai-unicorn-raising-130m-funding/
- https://finance.yahoo.com/technology/ai/articles/emergent-raises-series-c-1-140800576.html
- https://www.dealstreetasia.com/stories/emergent-unicorn-489228

Проверенные факты (совпадают во всех источниках):
- Компания: Emergent (emergent.sh) — платформа "vibe coding": строит рабочие приложения по текстовому описанию, без написания кода.
- Раунд Series C: $130 млн, оценка $1,5 млрд.
- Раунд объявлен ~15 июля 2026, примерно через год после публичного запуска сервиса.
- Лид раунда: фонд Creaegis. Также участвовали Claypond, Sentinel Global и действующие инвесторы Khosla Ventures, SoftBank Vision Fund 2, Lightspeed, Y Combinator.
- Общая сумма привлечённых инвестиций компании (с учётом всех раундов): $230 млн.
- Больше 200 000 платящих клиентов.
- Месячная активная аудитория: 1,5–2 млн пользователей (используется как справочный факт, в пост не включён).
- ARR (годовой регулярный доход): $120 млн (используется как справочный факт, в пост не включён).
- За год на платформе создано больше 12 млн приложений.
- Основная аудитория: предприниматели и владельцы малого бизнеса без технического опыта (по данным источников — большинство пользователей).
- Типичные приложения, которые строят пользователи: CRM, ERP/складской учёт, логистические инструменты, маркетплейсы.
- Платформа автоматически разворачивает весь стек: фронтенд, бэкенд, сервер, авторизацию пользователей, приём платежей.

## Дополнительно проверено: доступ к Emergent из России

Источники (WebSearch, независимые):
- https://dtf.ru/howto/4119430-kak-oplatit-emergent-v-rossii-i-belarusi-cherez-payholder
- https://foreignpay.ru/products/business/Emergent

Факт: Emergent принимает оплату через Stripe (международные карты). Прямая оплата российской картой недоступна из-за санкционных ограничений — используются посредники/иностранные карты, как и у большинства подобных зарубежных сервисов.

## Названия/цифры, использованные в посте — все присутствуют выше

Emergent, Creaegis, Khosla Ventures, SoftBank Vision Fund 2, Lightspeed, Y Combinator, $130 млн, $1,5 млрд, ~1 год с запуска, 200 000 клиентов, 12 млн приложений, оплата из России через иностранную карту/посредника.
