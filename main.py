from tkinter import *
from datetime import *
import time
import re
import os

text_link = ""
text_date = ""
text_time = ""


def submit():
    try:
        global text_link
        text_link = Entry_link.get()
        global text_date
        text_date = Entry_date.get()
        global text_time
        text_time = Entry_time.get()
        get_date_time()
        enter_zoom_link()
    except:
        print("something went worng! try again")
        quit()


def get_date_time():
    year, month, day, hour, minute = map(int, re.findall(r"[\w']+", (text_date+'-'+text_time)))
    time_entered = datetime(year, month, day, hour, minute)
    return time_entered


def enter_zoom_link():
    start = datetime.now()
    delay = (get_date_time() - start).total_seconds()
    delay_t = int(delay)
    time.sleep(delay_t)
    os.system(f"start {text_link}")


window = Tk()
window.title('zoom link opener')
window.geometry("1000x460")
window.configure(bg='#0f3d0f')


link = Label(window, text="enter zoom link: ", bg='#d6f5d6', font=("Comic Sans MS", 20, "bold"))
date = Label(window, text="enter date: ", bg='#d6f5d6', font=("Comic Sans MS", 20, "bold"))
_time = Label(window, text="enter time: ", bg='#d6f5d6', font=("Comic Sans MS", 20, "bold"))

Entry_link = Entry(window, width=80, bg='#d6f5d6', font=("Comic Sans MS", 10, "bold"))
Entry_date = Entry(window, width=12, bg='#d6f5d6', font=("Comic Sans MS", 10, "bold"))
Entry_time = Entry(window, width=12, bg='#d6f5d6', font=("Comic Sans MS", 10, "bold"))
submit_button = Button(text="Submit", bg='#d6f5e6', font=("Comic Sans MS", 14, "bold"), command=submit)


link.place(width=230, x=30, y=30)
date.place(width=230, x=30, y=100)
_time.place(width=230, x=30, y=170)


Entry_link.place(x=264, y=40)
Entry_date.place(x=264, y=110)
Entry_time.place(x=264, y=180)
submit_button.place(width=120, x=420, y=260)

window.mainloop()


