import calendar
year=int(input("Year :\t"))
month=1
for i in range(12):
    print(calendar.month(year,month+i))
    