import tkinter as tk 
from tkinter import ttk
from calendar import month_name
#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 


scale_v=tk.DoubleVar()

scale=ttk.Scale(root,command=lambda value:print(value))
scale.pack()




root.mainloop()