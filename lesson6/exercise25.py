import datetime as dt

now = dt.datetime.now()
today = dt.date.today()
print("Current date and time : {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
print("Current date : {}".format(today.strftime("%Y-%m-%d")))

print("Directory changed")
