import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

def openm():
    result=messagebox.showerror("error title","this is an error")
    print(result)

button =ttk.Button(root,text='click me',command=openm)
button.pack()

root.mainloop()
