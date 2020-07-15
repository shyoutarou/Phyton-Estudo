import datetime
import time

dateToday = datetime.datetime.today()
print(dateToday)  # 2020-03-04 10:46:28.640046
attributesInTuple = dateToday.timetuple()

# 2020 3 3 23 9 10 1 63 -1
for attribute in attributesInTuple:
    print(attribute, end=' ')

print("")
# time.struct_time(tm_year=2015, tm_mon=7, tm_mday=29, tm_hour=0,
# tm_min=0, tm_sec=0, tm_wday=2, tm_yday=210, tm_isdst=-1)
print(time.strptime("29 Jul 2015", "%d %b %Y"))
estrutura = time.strptime("Monday July 29 2015", "%A %B %d %Y")
timetup = time.gmtime()
print(estrutura)

# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=4, tm_hour=13,
# tm_min=37,  tm_sec=39, tm_wday=2, tm_yday=64, tm_isdst=0)
print(timetup)
print(time.strftime('%Y-%m-%dT%H:%M:%SZ', timetup)) # 2020-03-04T13:37:39Z
print(time.strftime('%Y-%m-%dT%H:%M:%SZ', estrutura)) # 2015-07-29T00:00:00Z



