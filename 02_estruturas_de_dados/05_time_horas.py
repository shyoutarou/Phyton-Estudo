import datetime
import time;

localtime = time.localtime(time.time())
print("Local current time :", localtime)
"""
Local current time : time.struct_time(tm_year=2020,
tm_mon=2, tm_mday=29, tm_hour=20, tm_min=52,
tm_sec=12, tm_wday=5, tm_yday=60, tm_isdst=0)
"""

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)
# Local current time : Sat Feb 29 20:54:00 2020

print(time.altzone)  # 7200

dateToday = datetime.datetime.today()
hora_tupla = dateToday.timetuple()
print(time.asctime(hora_tupla))  # Tue Mar  3 23:31:53 2020

clock = time.process_time()

print(clock)  # 0.046875
print(time.time())  # 1583289699.0583897

print(time.ctime(time.time()))  # Wed Mar  4 11:02:18 2020
print(time.ctime())       # Wed Mar  4 10:59:30 2020

# time.struct_time(tm_year=2286, tm_mon=11, tm_mday=20, tm_hour=14,
# tm_min=46, tm_sec=40, tm_wday=5, tm_yday=324, tm_isdst=0)
print(time.localtime(10000000000))
print(time.mktime(hora_tupla)) # 1583290216.0
print(time.sleep(1)) # None
print(time.strftime(localtime)) # Tue Mar  3 23:50:16 2020
# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=3, tm_hour=23, tm_min=50, tm_sec=16, tm_wday=1, tm_yday=63, tm_isdst=-1)
print(time.strptime(localtime))

# print(time.strptime(localtime, fmt = '% a% b% d% H:% M:% S% Y'))

print(time.timezone)  # 10800
print(time.tzname)  # ('Hora oficial do Brasil', 'Horário brasileiro de verão')

