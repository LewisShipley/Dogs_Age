
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("400x400")

# Text box code
age_var = tkinter.StringVar()
age_lab = tkinter.Label(window, text = "Dog's Age :")
age_entry = tkinter.Entry(window, textvariable = age_var)

def calc():
    human_age = int(age_var.get())
    tkinter.messagebox.showinfo("Calculation", f"your dog is {human_age} in human years")

calc_button = tkinter.Button(window, text = "Calculate", command = calc)
calc_button.grid(row = 5, column = 1)

window.mainloop()