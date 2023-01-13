from tkinter import *
import math

WORK_MIN = 25
SHORT_BT = 5
LONG_BT = 20
reps = 0
BGC="#A0C3D2"
TXTC="#EAE0DA"
Gtimer = None
# ================================================= #
# ======================TIMER RESET=========================== #
def reset_timer():
    window.after_cancel(Gtimer)             #stop timer
    canvas.itemconfig(timer, text="00:00")    #timer_text 00:00
    title.config(text="Timer",fg="#EAE0DA")    #title "Timer"
    check.config(text="")    #reset checks
    global reps
    reps = 0

# ==================TIMER MECHANISM :START BTN============================ #
def start_timer():
    global reps
    reps += 1
    # 1,3,5,7 rep: work
    if reps % 2 == 1:
        title.config(text="WORK", fg="RED")
        count_down(WORK_MIN * 60)
    # 8 rep: long_bt
    elif reps % 8:
        title.config(text="REST", fg="#0081C9")
        count_down(LONG_BT * 60)
    # 2,4,6 rep: short_bt
    else:
        title.config(text="REST", fg="#0081C9")
        count_down(SHORT_BT * 60)


# ==================COUNT DOWN MECHANISM========================= #
def count_down(count): #count: total seconds

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec) #or f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global Gtimer
        Gtimer = window.after(1000, count_down, count-1)
    else: #reach zero, start timer again
        start_timer()
        marks = "" # add check marks every two sessions
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text= marks)

# ==================UI=============================== #

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
