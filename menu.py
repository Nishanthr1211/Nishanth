from tkinter import *

root = Tk()

def profile():
    print("My Name is Nishanth \n My Age is 22 \n I am Coming from Vandalur")
    

menubar = Menu(root)
menubar.add_command(label="Profile", command=profile)

def menu():
    print("I am using Whatsapp \n Gmail \n and other social media")
menubar=Menu(root)
menubar.add_command(label="Menu", command=root.menu)

root.config(menu=menubar)

root.mainloop()
