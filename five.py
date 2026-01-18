import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

variable_value=tk.StringVar(value="welcome") #variable create 


label=ttk.Label(root,textvariable=variable_value)
label.pack()

entry=ttk.Entry(root,textvariable=variable_value)
entry.pack()

button=ttk.Button(root,text="click me",command=lambda:print(entry.get()))




root.mainloop()