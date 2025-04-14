import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("tk")
#entities
principle = tk.Label(window, text = "Principle")
intr = tk.Label(window, text = "Interest Rate")
Ys = tk.Label(window, text = "Years")
Pentry = tk.Entry(window)
inentry = tk.Entry(window)
def list():
    numbers = []
    for i in range(1000):
        numbers.append(i)
    return numbers
Yselect = ttk.Combobox(window, state = "readonly", values = list())
dash = tk.Label(window, text = "-")
a = tk.Label(window, text = "Amount")
aentry = tk.Entry(window)
#properties
principle.grid(row = 1, column = 1)
intr.grid(row = 1, column = 2)
Ys.grid(row = 1 , column = 3)
Pentry.grid(row = 2, column = 1)
inentry.grid(row = 2, column = 2)
Yselect.grid(row =2, column = 3)
dash.grid(row=3, column = 1)
a.grid(row = 4, column = 1, sticky = E)
aentry.grid(row = 4, column = 2)
window.mainloop()
