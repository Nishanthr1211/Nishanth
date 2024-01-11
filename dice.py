from tkinter import*
import random

wd=Tk()
wd.title("Tic Tac Game")
wd.geometry('400x500')


l=StringVar()
v=StringVar()
s=StringVar()


def player1():
    global z
    n=[1,2,3,4,5,6]
    m=random.choice(n)
    l.set(m)
    
    if m==1:
        pp.config(text="OUT")
    else:
        global xo
        xo=xo+m
        pp.configure(text=xo)
        l.set(m)

        b1.config(state=ACTIVE)
        b.config(state=DISABLED)
        restart.config(state.DISABLED)

def restart():
    global xo1,xo,p,g
    b1.config(state=ACTIVE)
    xo=0
    x01=0
    p=" "
    v.set(xo1)
    l.set(xo)
    
    
xo=0
b=Button(wd,text="       Player1      ",command=player1,bg="Blue")
b.place(x=50,y=200)

label0=Label(wd,text="    Player1    ",bg="Cyan")
label0.place(x=75,y=100)

label1=Label(wd,text="     Vs    ",bg="Red")
label1.place(x=170,y=100)
       
label2=Label(wd,text="    Player2    ",bg="Cyan")
label2.place(x=240,y=100)

a=Entry(wd,text=l,border=1,bg="Green",)
a.place(x=150,y=250)

pp=Label(wd,text=xo,fg="red")
pp.place(x=50,y=300,width=40,height=50)

restart=Button(wd,text="Restart",command=restart,state=DISABLED,bg='white')
restart.place(x=160,y=420,width=80,height=35)
def player2():
    global z1
    n1=[1,2,3,4,5,6]
    m1=random.choice(n1)
    l.set(m1)
    
    if m1==1:
        ppo.config(text="OUT")
    else:
        global xo1
        xo1=xo1+m1
        ppo.configure(text=xo1)
        l.set(m1)

        b1.config(state=DISABLED)
        b.config(state=DISABLED)
        restart.config(state=ACTIVE)
xo1=0
b1=Button(wd,text="       Player 2      ",command=player2,bg="Blue")
b1.place(x=250,y=200)


ppo=Label(wd,text=xo1,fg="red")
ppo.place(x=250,y=310)


wd.mainloop()
