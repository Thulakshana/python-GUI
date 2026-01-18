import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

def button_click():
    entry_value=entry.get()
    label.configure(text=entry_value)

    





entry=ttk.Entry(root)
entry.pack()

button =ttk.Button(root,text='click me',command=button_click) #create button
button.pack()

label=ttk.Label(root)
label.pack()
    













#run the window
root.mainloop()