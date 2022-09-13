import datetime as dt

now=dt.datetime.now()
print("The time now is ",now)

today_date=dt.datetime.date(now)
print(today_date)

# using print fstring

print(f'the timestamp now is {now} and date is \n {today_date}')



