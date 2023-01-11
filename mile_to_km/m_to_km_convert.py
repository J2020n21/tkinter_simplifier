from tkinter import *
from math import ceil

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=30,pady=50) #padding

#Entry (input box)
input = Entry()
input.config(width=15)
input.grid(row=0,column=1)

#Label
M_txt = Label(text="Miles", font=("Arial",16,"bold"))
M_txt.grid(row=0,column=2)

Km_txt = Label(text="Km", font=("Arial",16,"bold"))
Km_txt.grid(row=1,column=2)

Km_result = Label(text="0", font=("Arial",16,"normal"))
Km_result.grid(row=1,column=1)

eql_txt = Label(text="equals", font=("Arial",16,"bold"))
eql_txt.grid(row=1,column=0)

def button_clicked_cal():
    cal_result = float(input.get()) * 1.609
    Km_result.config(text="{:.2f}".format(cal_result))
    #convert mile to km and round the result

button = Button(text="Calculate", command=button_clicked_cal)
button.grid(row=2,column=1)

window.mainloop() #listening