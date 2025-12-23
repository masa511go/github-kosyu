from datetime import datetime
import calendar
print("Hello,world!!")
print("We create a develop branch")
print("This branch is masa511go/feat/print-today")
now_date = datetime.now().date()
now_year = datetime.now().year
now_month = datetime.now().month
print(calendar.month(now_year,now_month))
print(now_date)