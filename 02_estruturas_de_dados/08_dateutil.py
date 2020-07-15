from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

d = date(2016, 1, 31)
print(d)  # 2016-01-31

d = d + relativedelta(months=1)
print(d)  # somar 1 mês = 2016-02-29

d = d + relativedelta(years=1)
print(d)  # somar 1 ano = 2017-02-28

now = parse("Sat Oct 11 17:13:46 UTC 2003")
print(now) # 2003-10-11 17:13:46+00:00

today = now.date()
print("Today is: %s" % today) # Today is: 2003-10-11

year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
# Year with next Aug 13th on a Friday is: 2004
print("Year with next Aug 13th on a Friday is: %s" % year)

rdelta = relativedelta(easter(year), today)
# How far is the Easter of that year: relativedelta(months=+6)
print("How far is the Easter of that year: %s" % rdelta)
# And the Easter of that year is: 2004-04-11
print("And the Easter of that year is: %s" % (today+rdelta))



