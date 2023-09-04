let
    start_dt = #date(2015,1,1),
    end_dt = #date(2030,12,31),
    date_duration = Duration.Days(end_dt - start_dt) + 1,
    date_list = List.Generate(
        () => 0,
        each _ < date_duration,
        each _ + 1,
        each Date.AddDays(start_dt, _)
    ),
    to_table = Table.FromList(date_list, Splitter.SplitByNothing(), {"date"}, null, ExtraValues.Error),
    get_weekday = Table.AddColumn(to_table, "weekday", each Date.DayOfWeekName([date])),
    get_typeday = Table.AddColumn(get_weekday, "type_day", each holyday_date([date])),
    get_next_work_date = Table.AddColumn(get_typeday, "next_work_date", each next_work_date([date])),
    todate_next_work_date = Table.TransformColumnTypes(get_next_work_date,{{"next_work_date", type date}}),
    get_start_month_date = Table.AddColumn(todate_next_work_date, "start_month", each Date.StartOfMonth([date]), type date),
    get_start_week_date = Table.AddColumn(get_start_month_date, "start_week", each Date.StartOfWeek([date]), type date)
in
    get_start_week_date