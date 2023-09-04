(check_date as date) =>
let
    //check_date = #date(2021,9,4),
    next_day = Date.AddDays(check_date,1),
    result = (
        if holyday_date(check_date) = "рабочий" then check_date
        else if holyday_date(next_day) = "рабочий" then next_day
        else @next_work_date(next_day)
    ),
    date_result = Date.From(result)
in
    date_result