import tkinter as tk #conda install -c anaconda tk
import time
from datetime import date

#Github: https://github.com/sujitmandal

#This programe is create by Sujit Mandal

"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
"""

def clock():           
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    current_time = time.strftime("%I:%M:%S")
    lable_1 ["text"] = current_date
    lable_2 ["text"] = current_time
    root.after(1000, clock)


root = tk.Tk()
root.title("Digital Clock")
lable_1 = tk.Label(root, font = "article 120", bg = "black", fg = "green")
lable_2 = tk.Label(root, font = "article 150", bg = "black", fg = "red")
lable_1.grid(row = 0, column = 0)
lable_2.grid(row = 1, column = 0)
clock()

root.mainloop()