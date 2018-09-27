from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

h=0
m=0
s=0
t="AM"

def current_time(h,m,s,t):
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes %60
    hours = minutes //60
    current_hour = hours %24
    #set the time zone
    current_hour = current_hour - 6
    if current_hour >=12:
        tag="PM"
    else:
        tag="AM"
    timex = str(current_hour)+":"+str(current_minutes)+":"+str(current_seconds)+tag
    a = str(h)+":"+str(m)+":"+str(s)+t
    
    if timex == a:
        beep()
    return timex

#winspund.Beep(540.8000)

def quit(*args):
    root.destroy()
def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)
def beep():
    winsound.Beep(540,8000)
def get_alarm(*args):
    global h
    h= input("set hour")
    global m
    m= input("set minutes")
    global s
    s= input("set seconds")
    global t
    t= input("am or pm").upper()


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Green')
root.bind("x", quit)
root.bind("a", get_alarm)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=60)
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="Yellow", background="red")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
