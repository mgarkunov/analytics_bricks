#%%
import datetime as dt
import random as rnd


class date_utils:

    def __init__(self) -> None:
        """
        Класс с функциями для работы с датами
        """
        pass
    
    def date_random(self, start_dt:dt.date, end_dt:dt.date) -> dt.date:
        """
        Генерации случайной даты в указанном диапозоне

        Аргументы:
            - start_dt: стартовая дата
            - end_dt: конечная дата
        """
        if not isinstance(start_dt,dt.date) or not isinstance(end_dt,dt.date):
            raise ValueError("Incorrect params format")
        
        return dt.date.fromordinal(
            rnd.randint(start_dt.toordinal(), end_dt.toordinal())
        )
    
    def date_add(self, cur_dt:dt.date,  years:int = 0, quarters:int = 0, months:int = 0, weeks:int = 0, days:int = 0 ) -> dt.date:
        """
            Изменение даты с учетом указанного периода. Отрицательное число уменьшает на соответствующий период.

            Аргументы:
                - cur_dt - расчетная дата
                - years - дельта в года
                - quarters - дельта в кварталах
                - months - дельта в месяцах
                - weeks - дельта в неделя
                - days - дельта в днях
        """
        if not isinstance(cur_dt,dt.date) or not isinstance(years,int) or not isinstance(years,int) or not isinstance(years,int) or not isinstance(years,int) or not isinstance(years,int):
           raise ValueError("Incorrect params format")
        
        def month_add(cur_dt:dt.date, months:int) -> dt.date:
            """
            Добавляем указанное количество месяцев к указанной дате

            Аргументы:
                - cur_dt: дата для вычисления
            """
            if not isinstance(cur_dt,dt.date) or not isinstance(months,int):
                raise ValueError("Incorrect params format")
            
            total_mount_int = cur_dt.month + months
            print(total_mount_int)
            year_int = cur_dt.year + total_mount_int // 12
            month_int = total_mount_int % 12
            month_int = 12 if month_int == 0 else month_int        
            mlast_dt = ((dt.date(year_int, month_int, 1) + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)).day
            day_int = (
                cur_dt.day if cur_dt.day <= mlast_dt else mlast_dt
            )
            return dt.date(year_int, month_int, day_int) 
            
        if days:
            cur_dt = cur_dt + dt.timedelta(days=days)
        if weeks:
            print('week_in', cur_dt, weeks)
            cur_dt = cur_dt + dt.timedelta(weeks=weeks)
            print('week_out', cur_dt, weeks)
        if months:
            cur_dt = month_add(cur_dt, months)
        if quarters:            
            cur_dt = month_add(cur_dt, quarters * 3)
        if years:
            cur_dt = cur_dt.replace(year=cur_dt.year + years)
        
        return cur_dt            

    def date_diff(self, start_dt:dt.date, end_dt:dt.date) -> dt.date:
        """
        Возвращение разницы в периодах

        Аргументы:
            - start_dt: стартовая дата
            - end_dt: конечная дата
        """
        if not isinstance(start_dt,dt.date) or not isinstance(end_dt,dt.date):
            raise ValueError("Incorrect params format")
        def diff_days(sdt:dt.date, edt:dt.date) -> int:
            return (edt - sdt).days
        def diff_weeks(sdt:dt.date, edt:dt.date) -> int:
            return (diff_days(sdt, edt)) / 7
        def diff_months(sdt:dt.date, edt:dt.date) -> int:
            result = (edt.year - sdt.year) * 12 + (edt.month - sdt.month)
            return result if edt.day >= sdt.day else result - 1
        def diff_quarters(sdt:dt.date, edt:dt.date) -> int:
            result = diff_months(sdt, edt)  // 3
            return result
        def diff_years(sdt:dt.date, edt:dt.date) -> int:
            return diff_months(sdt, edt) // 12
        
        total_years = diff_years(start_dt, end_dt)
        total_quarters = diff_quarters(start_dt, end_dt)
        total_months = diff_months(start_dt, end_dt)
        total_weeks = diff_weeks(start_dt, end_dt)
        total_days = diff_days(start_dt, end_dt)
        int_dt = end_dt
        years = diff_years(start_dt, int_dt)
        int_dt = self.date_add(int_dt, years=-years)
        quarters = diff_quarters(start_dt, int_dt)
        int_dt = self.date_add(int_dt, quarters=-quarters)
        months = diff_months(start_dt, int_dt)
        int_dt = self.date_add(int_dt, months=-months)
        weeks = diff_weeks(start_dt, int_dt)
        int_dt = self.date_add(int_dt, weeks=-weeks)
        days = (int_dt - start_dt).days
        return {
            'start_dt':start_dt,
            'end_dt':end_dt,
            'total_year':total_years,
            'total_quarters':total_quarters,
            'total_months': total_months,
            'total_weeks': total_weeks,
            'total_days': total_days,          
            'years':years,
            'quarters':quarters,
            'months':months,
            'weeks':weeks,
            'days':days           
        }

    def day_of_week(self, cur_dt:dt.date) -> int:
        """
        Возвращается номер дня недели

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")
        
        return cur_dt.weekday() + 1

    def day_of_month(self, cur_dt:dt.date) -> int:
        """
        Возвращается номер дня месяца

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")
        
        return cur_dt.day
    
    def day_of_year(self, cur_dt:dt.date) -> int:
        """
        Возвращается номер дня месяца

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")
        
        return (cur_dt - cur_dt.replace(month=1, day=1)).days + 1
     
    def start_of_week(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты недели

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return cur_dt - dt.timedelta(days=cur_dt.weekday())        
        
    def end_of_week(self, cur_dt:dt.date) -> dt.date:
        """
        Получене конечно даты недели

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return self.start_of_week(cur_dt) + dt.timedelta(days=6)

    def start_of_month(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты месяца

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")
        
        return cur_dt.replace(day=1)

    def end_of_month(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты месяца

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return (cur_dt.replace(day=1) + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)
    
    def month_of_year(self, cur_dt:dt.date) -> int:
        """
        Возращается номер месяца в году

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return cur_dt.month

    def start_of_quarter(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты квартала

        Аргументы:
            - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")  
          
        return cur_dt.replace(
            year=cur_dt.year,
            month=self.quarter_of_year(cur_dt) * 3 - 2,
            day=1
        )

    def quarter_of_year(self, cur_dt:dt.date) -> int:
        """
        Возращается номер квартала

        Аргументы:
             - cur_dt - расчетная дата
        """
        if not isinstance(cur_dt, dt.date):
            raise ValueError("Incorrect params format")  
        
        if 1 <= cur_dt.month <= 3:
            quarter_mnt = 1
        elif 4 <= cur_dt.month <= 6:
            quarter_mnt = 2
        elif 7 <= cur_dt.month <= 9:
            quarter_mnt = 3
        elif 10 <= cur_dt.month <= 12:
            quarter_mnt = 4
        else:
            quarter_mnt = 1

        return quarter_mnt

    def end_of_quarter(self, cur_dt:dt.date) -> dt.date:
        """
        Получене конечной даты квартала

        Аргументы:
            - cur_dt - дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")   
        return self.date_add(self.start_of_quarter(cur_dt), quarters=1) - dt.timedelta(days=1)

    def start_of_year(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты года

        Аргументы:
            - cur_dt - дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return cur_dt.replace(month=1, day=1)
    
    def end_of_year(self, cur_dt:dt.date) -> dt.date:
        """
        Получене начальной даты года
        
        Аргументы:
            - cur_dt - дата
        """
        if not isinstance(cur_dt,dt.date):
            raise ValueError("Incorrect params format")

        return cur_dt.replace(year=cur_dt.year, month=1, day=1) - dt.timedelta(days=1)

