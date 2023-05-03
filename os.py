from tkinter import*
import datetime
from time import strftime

wd=Tk()
wd.title("OS")
wd.geometry("1400x1400")

def time():
    string=strftime('%H:%M:%S %p \n %d-%b-%G')
    a.configure(text= string )
    a.after(1000,time)

img4=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\desktop.png")
label9=Label(wd,image=img4)
label9.place(x=0,y=0)

img9=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\Bike1.png")

img8=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\Bike2.png")

img=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\This Pc.png")
button=Button(wd,image=img).place(x=8,y=2)

img1=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\Recycle.png")
button1=Button(wd,image=img1).place(x=8,y=100)

img2=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\folder.png")
button1=Button(wd,image=img2).place(x=8,y=210)

label=Label(wd,text=" ThisPc ",bg='white').place(x=8,y=65)

label1=Label(wd,text="Recycle",bg='white').place(x=8,y=170)

label=Label(wd,text=" Folder ",bg='white').place(x=8,y=270)

img3=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\Start.png")
button1=Button(wd,image=img3).place(x=3,y=670)

i=Entry(wd,text=" ").place(x=50,y=675)

def changebg():
    label9.config(image=img9)
def changebg1():
    label9.config(image=img8)
m = Menu(wd, tearoff = 0) 
m.add_command(label ="change_bg",command=changebg) 
m.add_command(label ="change_bg1",command=changebg1) 
m.add_separator() 

def do_popup(event): 
    try:
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 

label9.bind("<Button-3>", do_popup)
a=Label(wd,fg="red")
a.place(x=1250,y=670)
time()
