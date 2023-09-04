(check_dt as date, period as text) =>
let
    current_dt = Date.From(DateTime.LocalNow()),
    days_ago = Duration.Days(current_dt - check_dt),
    weeks_ago =  Duration.Days(Date.StartOfWeek(current_dt) - Date.StartOfWeek(check_dt)) / 7,
    months_ago = ((Date.Year(current_dt) - Date.Year(check_dt)) * 12) + Date.Month(current_dt) - Date.Month(check_dt),
    current_quarter = Date.StartOfQuarter(current_dt),
    check_quarter = Date.StartOfQuarter(check_dt),
    quarters_ago = (((Date.Year(current_quarter) - Date.Year(check_quarter)) * 12) + Date.Month(current_quarter) - Date.Month(check_quarter))/ 3,
    years_ago = Date.Year(current_dt) - Date.Year(check_dt),
    result = (
        if period = "days" then days_ago
        else if period = "week" then weeks_ago 
        else if period = "month" then months_ago 
        else if period = "quarter" then quarters_ago 
        else if period = "year" then years_ago 
        else  days_ago
    )
in
    result