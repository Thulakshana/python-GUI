import tkinter as tk 
from tkinter import ttk
from calendar import month_name
#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

spinbox_v=tk.StringVar()
#spin box

spinbox=ttk.Spinbox(root,values=[1,2,3,4,5,6],textvariable=spinbox_v)
spinbox.pack()

label=ttk.Label(root,textvariable=spinbox_v)
label.pack()






root.mainloop()