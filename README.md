# *Analytics Bricks*

В этом проекте будут мои наработки / примеры коды для Digiral (web / app) аналитиков. / This project will contain my developments / code examples for Digiral (web / app) analysts.

## [JavaScript](https://github.com/mgarkunov/analytics_bricks/tree/main/javascript)

### [ru_translit.js](https://github.com/mgarkunov/analytics_bricks/tree/main/javascript)
Функция транслитерации русского текста в латиницу. / The function of transliterating Russian text into Latin.

## [Power Query](https://github.com/mgarkunov/analytics_bricks/tree/main/power_query)

### [Вычисление давности / Date Ago ](https://github.com/mgarkunov/analytics_bricks/tree/main/power_query/date_ago)
Вычисление давности периода от текущей даты в днях, неделях, месяцах, кварталах и годам. / Calculation of the prescription of the period from the current date in days, weeks, months, quarters and years. 

 - date_ago.xlsx - working file example / пример рабочего файла
 - calendar.pq - calendar generation source code / исходный код генерации календаря
 - date_ago.pq - function source code for determining the period from the current date / исходнй код функции для определения периода от текущей даты

### [Производственный календарь / Production Calendar](https://github.com/mgarkunov/analytics_bricks/tree/main/power_query/production_calendar)
Производственный календарь для России на 2015 - 2030 год. / Production calendar for Russia for 2015 - 2030.

 - production_calendar.xlsb - working file example / пример рабочего файла
 - production_calendar.pq - calendar generation source code / исходный код генерации календаря
 - holyday_date.pq - source code of the function for determining days off taking into account holidays / исходнй код функции для определения выходных дней с учетом праздникв
 - next_work_date.pq - function source code for determining the next working day, taking into account weekends and holidays / исходный код функции для определения следующего рабочего дня с учетом выходных и праздничных дней

## [Python](https://github.com/mgarkunov/analytics_bricks/tree/main/python)

### [Производственный календарь / Production Сalendar ](https://github.com/mgarkunov/analytics_bricks/tree/main/python)
Функции для формирования производстветственного календаря с определением параметров дня и определения ближайшее рабочего дня. / Functions for generating a production calendar with the definition of day parameters and determining the nearest working day.

## [SQL](https://github.com/mgarkunov/analytics_bricks/tree/main/sql)

### Производственный календарь / Production Calendar]
Production calendar for Russia for 2015 - 2030 / производственный календарь для России на 2015 - 2030 год

 - [Implementation in PostgreSQL / Реализация для PostreSQL](https://github.com/mgarkunov/analytics_bricks/blob/main/sql/postgresql/production_calendar.sql)
 - [Implementation in ClickHouse / Реализация для ClickHouse](https://github.com/mgarkunov/analytics_bricks/blob/main/sql/clickhouse/production_calendar.sql)