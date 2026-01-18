import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

frame1=ttk.Frame(root,width=200,height=100,relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack(side='left')

entry=ttk.Entry(frame1)
entry.pack()







root.mainloop()