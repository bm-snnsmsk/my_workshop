# import datetime
from datetime import datetime
from datetime import timedelta ## ileri tarihler için 

result = dir(datetime)

result = datetime.today()

result = datetime.now()
result = datetime.now().year
result = datetime.now().month
result = datetime.now().day
result = datetime.now().hour
result = datetime.now().minute
result = datetime.now().second

result = datetime.ctime(datetime.now())

result = datetime.strftime(datetime.now(), "%Y")
result = datetime.strftime(datetime.now(), "%X")
result = datetime.strftime(datetime.now(), "%d")
result = datetime.strftime(datetime.now(), "%A")
result = datetime.strftime(datetime.now(), "%B")
result = datetime.strftime(datetime.now(), "%H")
result = datetime.strftime(datetime.now(), "%I")
result = datetime.strftime(datetime.now(), "%S")
result = datetime.strftime(datetime.now(), "%M")


t = "17 november 2022 saat 17:13:58"
result = datetime.strptime(t, "%d %B %Y saat %H:%M:%S")

result = datetime(1983,5,9,12,30,10)
result = datetime.timestamp(datetime(1983,5,9,12,30,10))
result = datetime.fromtimestamp(datetime.timestamp(datetime(1983,5,9,12,30,10)))
result = datetime.fromtimestamp(0) # 1970-01-01 03:00:00

birthday = datetime(1983,5,9,12,30,10)
result = datetime.now() - birthday

# result = result.days
# result = result.seconds
# result = result.microseconds

result = datetime.now() + timedelta(days = 10)

print(result)

