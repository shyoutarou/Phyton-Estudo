import datetime

from datetime import datetime as dt

print(dt.now())  # 2020-03-04 11:48:51.058566

hoje = datetime.datetime.today()

print(hoje)  # 2020-03-04 11:32:31.113566
print(datetime.date.today())  # 2020-03-04
print(datetime.date(2018, 11, 1))  # 2018-11-01
print(datetime.datetime.now())  # 2020-03-04 11:36:23.811566

# 2018-11-01 13:45:11.877875
print(datetime.datetime(2018, 11, 1, 13, 45, 11, 877875))

print(hoje.year)  # 2020
print(hoje.month)  # 3
print(hoje.day)  # 4

hoje = datetime.datetime.today()

print(datetime.datetime.now().time())  # 11:36:23.812561
print(datetime.time(13, 45, 26, 437575))  # 13:45:26.437575

print(hoje.hour)  # 11
print(hoje.minute)  # 42
print(hoje.second)  # 46
print(hoje.microsecond)  # 355561
print(hoje.weekday())  # 2
print(hoje.isoweekday())  # 3

print(hoje.isoformat())  # 2020-03-04T11:50:36.512566

data = datetime.date(year=2019, month=9, day=7)
print(data)  # 2019-09-07
data = datetime.date(2020, 11, 3)
print(data)  # 2020-11-03

daqui_a_90_dias = hoje + datetime.timedelta(days=90)
print(daqui_a_90_dias)  # 2020-06-02 11:55:51.779566
calc_data = hoje - datetime.timedelta(minutes=30)
print(calc_data)  # 2020-03-04 11:25:51.779566
calc_data = hoje - datetime.datetime(2018, 11, 1, 13, 16, 17, 94101)
print(calc_data)  # 488 days, 22:39:34.685465
