from tkinter import *
import random

def gen_color():
    wd.configure(background=random.choice(["red", "green" , "blue" , "orange"]))
        
wd =Tk()
wd.title("Pythontpoint")
wd.geometry('500x800')

button=Button(wd,text='Click Me',command = gen_color).pack()



def gen_color1():
    wd1.configure(background=random.choice(["black", "violet" , "gray" , "purple"]))
        
wd1 =Tk()
wd1.title("Pythontpoint")
wd1.geometry('500x500')

button=Button(wd1,text='Click Me',command = gen_color1).pack()
wd1.mainloop()


