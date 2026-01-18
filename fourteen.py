import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

notebk=ttk.Notebook(root)
frame1=ttk.Frame(notebk,width=200,height=100,relief=tk.GROOVE)
frame1.pack_propagate(False)
notebk.add(frame1,text='input')
notebk.pack()

root.mainloop()