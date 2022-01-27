import calendar
from tkinter import simpledialog

yy = simpledialog.askinteger("Input", "type a year")
mm = simpledialog.askinteger("Input", "type a month")
day = simpledialog.askinteger("Input", "type a day")

print((calendar.day_name[calendar.weekday(yy, mm, day)].upper()))
