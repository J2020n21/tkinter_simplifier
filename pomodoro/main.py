from tkinter import *

WORK_MIN = 25
SHORT_BT = 5
LONG_BT = 20
BGC="#A0C3D2"
TXTC="#EAE0DA"
# ================================================= #


window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=40, bg=BGC)

canvas = Canvas(width=150, height=150, bg=BGC)
canvas.grid(row=1,column=1)

title = Label(text="Timer",fg=TXTC, bg=BGC,font=("Sans-Sarif",36))
title.grid(row=0, column=1)

check = Label(text="✔", bg=BGC)
check.grid(row=3, column=1)

time = Label(text="00:00",bg=BGC,font=("Arial",20,"bold"))
time.grid(row=1, column=1)

btn_start= Button(text="Start")
btn_start.grid(row=2,column=0)

btn_reset= Button(text="Reset")
btn_reset.grid(row=2,column=2)


window.mainloop()