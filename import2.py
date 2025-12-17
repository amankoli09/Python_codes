import datetime
now=datetime.datetime.now()
print(now)
today=datetime.date.today()
print(today)

d=datetime.date(2025,12,1)
print(d)
print(d.strftime('%m/%d/%Y'))