from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")
root.geometry("500x300+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

Label(root,text="login form", font="ar 15 bold").grid(row=0,column=3)



checkbtn=Checkbutton(text="remeber me?").grid(row=1,column=2)

root.mainloop()