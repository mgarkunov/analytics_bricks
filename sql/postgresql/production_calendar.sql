with recursive clnd as (
    select
        1 as day_cnt,
        (select sdt from dt) as day_dt
    union
    select 
        day_cnt + 1 as day_cnt,
        day_dt + 1  as day_dt
    from clnd
    where day_cnt  <= (select edt from dt) - (select sdt from dt) 
), dt as (
    select  
        '2023-01-01'::date as sdt, -- указываем первичную дату 
        now()::date as edt -- указываем конечную дату
), 
day_off as (
    select 
        unnest(array['2015-01-01', '2015-01-02', '2015-01-05', '2015-01-06', '2015-01-07', '2015-01-08', '2015-01-09', '2015-02-23', '2015-03-09', '2015-05-01', '2015-05-04', '2015-05-11', '2015-06-12', '2015-11-04', '2016-01-01', '2016-01-04', '2016-01-05', '2016-01-06', '2016-01-07', '2016-01-08', '2016-02-22', '2016-02-23', '2016-03-07', '2016-03-08', '2016-05-02', '2016-05-03', '2016-05-09', '2016-06-13', '2016-11-04', '2017-01-02', '2017-01-03', '2017-01-04', '2017-01-05', '2017-01-06', '2017-02-23', '2017-02-24', '2017-03-08', '2017-05-01', '2017-05-08', '2017-05-09', '2017-06-12', '2017-11-06', '2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-08', '2018-02-23', '2018-03-08', '2018-03-09', '2018-04-30', '2018-05-01', '2018-05-02', '2018-05-09', '2018-06-11', '2018-06-12', '2018-11-05', '2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-07', '2019-01-08', '2019-03-08', '2019-05-01', '2019-05-02', '2019-05-03', '2019-05-09', '2019-05-10', '2019-06-12', '2019-11-04', '2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08', '2020-02-24', '2020-03-09', '2020-05-01', '2020-05-04', '2020-05-05', '2020-05-11', '2020-06-12', '2020-11-04', '2021-01-01', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-02-22', '2021-02-23', '2021-03-08', '2021-05-03', '2021-05-10', '2021-06-14', '2021-11-04', '2021-11-05', '2021-12-31', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-02-23', '2022-03-07', '2022-03-08', '2022-05-02', '2022-05-03', '2022-05-09', '2022-05-10', '2022-06-13', '2022-11-04', '2022-12-31', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-02-23', '2023-02-24', '2023-03-08', '2023-05-01', '2023-05-08', '2023-05-09', '2023-06-12', '2023-11-06', '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-08', '2024-02-23', '2024-03-08', '2024-04-29', '2024-04-30', '2024-05-01', '2024-05-09', '2024-05-10', '2024-06-12', '2024-11-04', '2024-12-30', '2024-12-31'])::date as day_dt
),
day_on as (
    select 
        unnest(array['2016-02-20', '2018-04-28', '2018-06-09', '2018-12-29', '2021-02-20', '2022-03-05', '2024-04-27', '2024-11-02', '2024-12-28'])::date as day_dt
),
calendar as (
    select 
        day_dt, -- дата
        (array['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'])[extract(isodow from day_dt)::int] as day_weekday_name, -- названия дня недели
        case
            when extract(isodow from day_dt)::int in (6,7) and  day_dt in (select * from day_on) then 'рабочий'
            when extract(isodow from day_dt)::int in (1,2,3,4,5) and day_dt in (select * from day_off) then 'выходной'
            when extract(isodow from day_dt)::int in (6,7) and day_dt not in (select * from day_on) then 'выходной'
            when extract(isodow from day_dt)::int in (1,2,3,4,5) and day_dt not in (select * from day_off) then 'рабочий'
        end as day_type_name,
        extract(isodow from day_dt)::int  as day_of_week,
        extract(day from day_dt)::int as  day_of_month,
        day_dt - make_date(extract(year from day_dt)::int, 1, 1) + 1 as day_of_year,
        day_dt - (extract(isodow from day_dt)::int - 1)  as week_start,
        (day_dt - (extract(isodow from day_dt)::int - 1) + interval '6 day')::date as week_end,
        age(day_dt , make_date(extract(year from day_dt)::int, 1, 1)) + interval '1 day' as week_of_year,
        make_date(extract(year from day_dt)::int, extract(month from day_dt)::int, 1) as month_start,
        (make_date(extract(year from day_dt)::int, extract(month from day_dt)::int, 1) + interval '1 month' - interval '1 day')::date as month_end,
        extract(month from day_dt) as  month_of_year,
        (make_date(extract(year from day_dt)::int, extract(month from day_dt)::int, 1) + interval '1 month' - interval '1 day')::date - make_date(extract(year from day_dt)::int, extract(month from day_dt)::int, 1)::date + 1 as month_days,
         make_date(extract(year from day_dt)::int, extract(quarter from day_dt)::int * 3 - 2, 1) as quarter_start,
         (make_date(extract(year from day_dt)::int, extract(quarter from day_dt)::int * 3 - 2, 1) + interval '3 month' - interval '1 day')::date as quarter_end,
        extract(quarter from day_dt) as  quarter_of_year,
        (make_date(extract(year from day_dt)::int, extract(quarter from day_dt)::int * 3 - 2, 1) + interval '3 month' - interval '1 day')::date - make_date(extract(year from day_dt)::int, extract(quarter from day_dt)::int * 3 - 2, 1) as  quarter_days,
        make_date(extract(year from day_dt)::int, 1, 1)  as year_start,
        make_date(extract(year from day_dt)::int, 12, 31)  as year_end,
        extract(year from day_dt)::int as year_num,
        (make_date(extract(year from day_dt)::int, 12, 31)  -  make_date(extract(year from day_dt)::int, 1, 1)) + 1 as year_days
    from clnd
)
select
    day_dt,
    day_weekday_name,
    day_type_name,
    day_of_week,
    day_of_month,
    day_of_year,
    week_start,
    week_end,
    week_of_year,
    month_start,
    month_end,
    month_of_year,
    month_days,
    quarter_start,
    quarter_end,
    quarter_of_year,
    quarter_days,
    year_start,
    year_end,
    year_num,
    year_days
from calendar