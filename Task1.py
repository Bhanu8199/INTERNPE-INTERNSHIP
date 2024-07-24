from tkinter import *
from time import *

def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000,update)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime("%d-%m-%Y")
    date_label.config(text=date_string)

root = Tk()
root.title("CLOCK")

time_label = Label(root,font=("Arial",50),fg="red",bg="black")
time_label.pack()

date_label = Label(root,font=("Arial",30,"bold"))
date_label.pack()

day_label = Label(root,font=("Arial",30,"bold"))
day_label.pack()

update()

root.mainloop()