#euler19

from datetime import date

print sum([1 for month in range(1,13) for year in range(1901,2001) if date(year,month,1).weekday()==6])
