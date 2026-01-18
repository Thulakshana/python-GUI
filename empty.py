import tkinter as tk 

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

root.geometry (f'(400)x(400)+100+200') #width x height + x_offset + y_offset

root.minsize(False,False) #minimum size

width,height=400,400 #screen eka madin open wenna 
display_width=root.winfo_screenwidth()
display_height=root.winfo_screenheight()
left=int(display_width/2-width/2)
top=int(display_height/2-height/2)






#run the window
root.mainloop()