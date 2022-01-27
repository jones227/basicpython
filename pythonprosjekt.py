import calendar
from tkinter import simpledialog

yy = simpledialog.askinteger("year", "type a year")
mm = simpledialog.askinteger("month", "type a month")
day = simpledialog.askinteger("day", "type a day")

print(calendar.day_name[calendar.weekday(yy, mm, day)].upper())
