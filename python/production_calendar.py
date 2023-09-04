#%%
import datetime as dt
import random as rnd
import math

class production_calendar():
    def __init__(self, cur_dt:dt.date) -> None:
        """
        Производственный календарь для определения параметров даты

        Аргументы:
            - cur_dt - проверочная дата
        """
        if not isinstance(cur_dt, dt.date):
            raise Exception("Неверное значение. Нужна дата.")
                    
        self.days_dict  = {
            2015:{
                'day_off':[
                        dt.date(2015,1,1),
                        dt.date(2015,1,2),
                        dt.date(2015,1,5),
                        dt.date(2015,1,6),
                        dt.date(2015,1,7),
                        dt.date(2015,1,8),
                        dt.date(2015,1,9),
                        dt.date(2015,2,23),
                        dt.date(2015,3,9),
                        dt.date(2015,5,1),
                        dt.date(2015,5,4),
                        dt.date(2015,5,11),
                        dt.date(2015,6,12),
                        dt.date(2015,11,4),
                ],
                'day_on': []
            },
            2016:{
                'day_off':[
                        dt.date(2016,1,1),
                        dt.date(2016,1,4),
                        dt.date(2016,1,5),
                        dt.date(2016,1,6),
                        dt.date(2016,1,7),
                        dt.date(2016,1,8),
                        dt.date(2016,2,22),
                        dt.date(2016,2,23),
                        dt.date(2016,3,7),
                        dt.date(2016,3,8),
                        dt.date(2016,5,2),
                        dt.date(2016,5,3),
                        dt.date(2016,5,9),
                        dt.date(2016,6,13),
                        dt.date(2016,11,4),
                ],
                'day_on':[
                    dt.date(2016,2,20),
                ]
            },
            2017:{
                'day_off':[
                    dt.date(2017,1,2),
                    dt.date(2017,1,3),
                    dt.date(2017,1,4),
                    dt.date(2017,1,5),
                    dt.date(2017,1,6),
                    dt.date(2017,2,23),
                    dt.date(2017,2,24),
                    dt.date(2017,3,8),
                    dt.date(2017,5,1),
                    dt.date(2017,5,8),
                    dt.date(2017,5,9),
                    dt.date(2017,6,12),
                    dt.date(2017,11,6),
                ],
                'day_on':[]
            },
            2018:{
                'day_off':[
                    dt.date(2018,1,1),
                    dt.date(2018,1,2),
                    dt.date(2018,1,3),
                    dt.date(2018,1,4),
                    dt.date(2018,1,5),
                    dt.date(2018,1,8),
                    dt.date(2018,2,23),
                    dt.date(2018,3,8),
                    dt.date(2018,3,9),
                    dt.date(2018,4,30),
                    dt.date(2018,5,1),
                    dt.date(2018,5,2),
                    dt.date(2018,5,9),
                    dt.date(2018,6,11),
                    dt.date(2018,6,12),
                    dt.date(2018,11,5),
                ],
                'day_on':[
                    dt.date(2018,4,28),
                    dt.date(2018,6,9),
                    dt.date(2018,12,29),
                ]
            },
            2019:{
                'day_off':[
                    dt.date(2019,1,1),
                    dt.date(2019,1,2),
                    dt.date(2019,1,3),
                    dt.date(2019,1,4),
                    dt.date(2019,1,7),
                    dt.date(2019,1,8),
                    dt.date(2019,3,8),
                    dt.date(2019,5,1),
                    dt.date(2019,5,2),
                    dt.date(2019,5,3),
                    dt.date(2019,5,9),
                    dt.date(2019,5,10),
                    dt.date(2019,6,12),
                    dt.date(2019,11,4),
                ],
                'day_n':[]
            },
            2020:{
                'day_off':[
                    dt.date(2020,1,1),
                    dt.date(2020,1,2),
                    dt.date(2020,1,3),
                    dt.date(2020,1,6),
                    dt.date(2020,1,7),
                    dt.date(2020,1,8),
                    dt.date(2020,2,24),
                    dt.date(2020,3,9),
                    dt.date(2020,5,1),
                    dt.date(2020,5,4),
                    dt.date(2020,5,5),
                    dt.date(2020,5,11),
                    dt.date(2020,6,12),
                    dt.date(2020,11,4),
                ],
                'day_on':[]
            },
            2021:{
                'day_off':[
                    dt.date(2021,1,1),
                    dt.date(2021,1,4),
                    dt.date(2021,1,5),
                    dt.date(2021,1,6),
                    dt.date(2021,1,7),
                    dt.date(2021,1,8),
                    dt.date(2021,2,22),
                    dt.date(2021,2,23),
                    dt.date(2021,3,8),
                    dt.date(2021,5,3),
                    dt.date(2021,5,10),
                    dt.date(2021,6,14),
                    dt.date(2021,11,4),
                    dt.date(2021,11,5),
                    dt.date(2021,12,31),
                ],
                'day_on':[
                    dt.date(2021,2,20),
                ]
            },
            2022:{
                'day_off':[
                    dt.date(2022,1,3),
                    dt.date(2022,1,4),
                    dt.date(2022,1,5),
                    dt.date(2022,1,6),
                    dt.date(2022,1,7),
                    dt.date(2022,2,23),
                    dt.date(2022,3,7),
                    dt.date(2022,3,8),
                    dt.date(2022,5,2),
                    dt.date(2022,5,3),
                    dt.date(2022,5,9),
                    dt.date(2022,5,10),
                    dt.date(2022,6,13),
                    dt.date(2022,11,4),
                    dt.date(2022,12,31),
                ],
                'day_on':[
                    dt.date(2022,3,5)
                ]
            },
            2023:{
                'day_off':[
                    dt.date(2023,1,2),
                    dt.date(2023,1,3),
                    dt.date(2023,1,4),
                    dt.date(2023,1,5),
                    dt.date(2023,1,6),
                    dt.date(2023,2,23),
                    dt.date(2023,2,24),
                    dt.date(2023,3,8),
                    dt.date(2023,5,1),
                    dt.date(2023,5,8),
                    dt.date(2023,5,9),
                    dt.date(2023,6,12),
                    dt.date(2023,11,6),
                ],
                'day_on':[]
            },
            2024:{
                'day_off':[
                    dt.date(2024,1,1),
                    dt.date(2024,1,2),
                    dt.date(2024,1,3),
                    dt.date(2024,1,4),
                    dt.date(2024,1,5),
                    dt.date(2024,1,8),
                    dt.date(2024,2,23),
                    dt.date(2024,3,8),
                    dt.date(2024,4,29),
                    dt.date(2024,4,30),
                    dt.date(2024,5,1),
                    dt.date(2024,5,9),
                    dt.date(2024,5,10),
                    dt.date(2024,6,12),
                    dt.date(2024,11,4),
                    dt.date(2024,12,30),
                    dt.date(2024,12,31),
                ],
                'day_on':[
                    dt.date(2024,4,27),
                    dt.date(2024,11,2),
                    dt.date(2024,12,28),
                ]
            }, 
        }
        self.dayname_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'восресенье']
        self.day_date = cur_dt
        self.day_weekday_name = self.dayname_list[cur_dt.weekday()]
        if cur_dt.weekday() < 5:
            if cur_dt in self.days_dict[cur_dt.year]['day_off']:
                self.day_type_name = "выходной"
            else:
                self.day_type_name = "рабочий"
        else:
            if cur_dt in self.days_dict[cur_dt.year]['day_on']:
                self.day_type_name = "рабочий"
            else:
                self.day_type_name = "выходной"
        new_dt = cur_dt
        new_dt += dt.timedelta(days=1)
        while new_dt.isoweekday() in [6, 7] or new_dt in self.days_dict[new_dt.year]['day_off']:
            new_dt += dt.timedelta(days=1)
        self.day_next_work = new_dt
        self.day_of_week = cur_dt.isoweekday()
        self.day_of_month = cur_dt.day
        self.day_of_year = (cur_dt - cur_dt.replace(month=1, day=1)).days + 1
        self.week_start = cur_dt - dt.timedelta(days=cur_dt.weekday())     
        self.week_end = self.week_start + dt.timedelta(days=6)
        self.week_num_of_year = math.ceil((cur_dt - cur_dt.replace(month=1, day=1)).days / 7)
        self.month_start = cur_dt.replace(day=1)
        self.month_end = (cur_dt.replace(day=1) + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)
        self.month_num_of_year = cur_dt.month
        self.month_days = (self.month_end - self.month_start).days + 1
        if 1 <= cur_dt.month <= 3:
            self.quarter_of_year = 1
        elif 4 <= cur_dt.month <= 6:
            self.quarter_of_year = 2
        elif 7 <= cur_dt.month <= 9:
            self.quarter_of_year = 3
        elif 10 <= cur_dt.month <= 12:
            self.quarter_of_year = 4
        else:
            self.quarter_of_year = 1
        self.quarter_start = cur_dt.replace(month=self.quarter_of_year * 3 - 2, day=1)
        self.quarter_end = (self.quarter_start + dt.timedelta(days=94)).replace(day=1) - dt.timedelta(days=1)
        self.quarter_days = (self.quarter_end - self.quarter_start).days + 1
        self.year_start = cur_dt.replace(month=1, day=1)
        self.year_end = cur_dt.replace(year=cur_dt.year + 1, month=1, day=1) - dt.timedelta(days=1)
        self.year_num = cur_dt.year
        self.year_days = (self.year_end - self.year_start).days + 1

    def get_all_params(self) -> dict:
        """
        Получение всех параметров даты
        """
        return {
            'day_date': self.day_date,
            'day_weekday_name': self.day_weekday_name,
            'day_type_name': self.day_type_name,
            'day_next_work':self.day_next_work,
            'day_of_week': self.day_of_week,
            'day_of_month': self.day_of_month,
            'day_of_year': self.day_of_year,
            'week_start': self.week_start,
            'week_end': self.week_end,
            'week_num_of_year': self.week_num_of_year,
            'month_start': self.month_start,
            'month_end': self.month_end,
            'month_num_of_year': self.month_num_of_year,
            'month_days': self.month_days,
            'quarter_start': self.quarter_start,
            'quarter_end': self.quarter_end,
            'quarter_of_year': self.quarter_of_year,
            'quarter_days': self.quarter_days,
            'year_start': self.year_start,
            'year_end': self.year_end,
            'year_num': self.year_num,
            'year_days': self.year_days
        }

pclnd = production_calendar(dt.date.today())
pclnd.get_all_params()
