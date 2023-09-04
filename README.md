# Analytics Bricks
Repository for universal recipes with code examples

## Python

### [Production Сalendar](https://github.com/mgarkunov/analytics_bricks/tree/main/python)
Functions for the formation of a production calendar with the determination of the parameters of the day and determine the nearest working day.

## SQL

### Production Calendar
Production calendar for Russia for 2015 - 2030
 - [Implementation in PostgreSQL](https://github.com/mgarkunov/analytics_bricks/blob/main/sql/postgresql/production_calendar.sql)
 - [Implementation in ClickHouse](https://github.com/mgarkunov/analytics_bricks/blob/main/sql/clickhouse/production_calendar.sql)

## Power Query

### [Date Ago](https://github.com/mgarkunov/analytics_bricks/tree/main/power_query/date_ago)
Calculation of the prescription of the period from the current date in days, weeks, months, quarters and years. 
 - date_ago.xlsx - An example of a work file
 - calendar.pq - The source code of the calendar generation
 - date_ago.pq - The source code of the function to determine the period from the current date

### [Production Calendar](https://github.com/mgarkunov/analytics_bricks/tree/main/power_query/production_calendar)
The production calendar for Russia for 2015 - 2030.

 - production_calendar.xlsb - An example of a work file
 - production_calendar.pq - The source code of the calendar generation
 - holyday_date.pq - The source code of the function to determine the weekend, taking into account the holidays.
 - next_work_date.pq - The source code of the function to determine the next working day, taking into account weekends and holidays

## JavaScript

### [ru_translit.js](https://github.com/mgarkunov/analytics_bricks/tree/main/javascript)
The function of transliterating the Russian text in the Latin.