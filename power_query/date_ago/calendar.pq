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
    to_date = Table.TransformColumnTypes(to_table,{{"date", type date}}),
    days_ago = Table.AddColumn(to_date, "days_ago", each date_ago([date], "days")),
    weeks_ago = Table.AddColumn(days_ago, "weeks_ago", each date_ago([date], "week")),
    months_ago = Table.AddColumn(weeks_ago, "months_ago", each date_ago([date], "month")),
    quarters_ago = Table.AddColumn(months_ago, "quarters_ago", each date_ago([date], "quarter")),
    years_ago = Table.AddColumn(quarters_ago, "years_ago", each date_ago([date], "year"))
in
    years_ago