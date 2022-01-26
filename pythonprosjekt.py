import calendar
from Tkinter import Tk, Entry

# declare the window
window = Tk()
# set window title
window.title("Python GUI App")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='lightgray')
window.mainloop()

tk = Tk()
inputBox = Entry(tk, bd=5)

#to read your box
inputBox.get()
yy = int(input('write year'))
mm = int(input('write month'))
day = int(input('write day'))




print(calendar.weekday(yy, mm, day))
