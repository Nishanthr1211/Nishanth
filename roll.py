from tkinter import *
import random
wd=Tk()
wd.title("Dice_Game")
wd.geometry('600x600')
a=Frame(wd,bg='Yellow',height=550,width=450)
a.pack(side=TOP)


pc_info=[1,2,3,4,5,6]


l5=Label(a,text='')

   
a1=StringVar()

a2=StringVar()

a3=StringVar()

score=0
score1=0

def play1():
    global score
    roll=random.choice(pc_info)
    if roll==1:
       
        l5.config(text="Player1 OUT")
        l5.place(x=170,y=150,width=105)
        b2.configure(state=ACTIVE)
        b1.configure(state=DISABLED)
        restart.configure(state=DISABLED)
        a1.set(score)
       
       
    else:
        score=score+roll
        l5.config(text=roll)
        l5.place(x=190,y=150,width=34,height=35)
        a1.set(score)
        e1=Entry(a,text=a1,font=('times',15))
        e1.place(x=220,y=80,width=64,height=35)

def play2():
    global score1
    roll=random.choice(pc_info)
    if roll==1:
        l5.config(text="player2 OUT")
        l5.place(x=170,y=150,width=105)
        b2.configure(state=DISABLED)
        b1.configure(state=DISABLED)
        restart.configure(state=ACTIVE)
        a2.set(score1)
        if(score1>score):
            l8.configure(text="Player 2 Win")

            l9.place(x=160,y=300,width=100)
            g=max(score1,score)
            l9.config(text=('HIGH SCORE:', g))
           
        else:
           
            l8.configure(text="Player 1 Win")
           
            l9.place(x=160,y=300,width=100)
            g=max(score1,score)
            l9.config(text=('HIGH SCORE:', g))
       
       

       
    else:
        score1=score1+roll
        l5.config(text=roll)
        l5.place(x=190,y=150,width=34,height=35)
        a2.set(score1)
        e1=Entry(a,text=a2,font=('times',15))
        e1.place(x=220,y=80,width=64,height=35)
p=''
l9=Label(a,text=" ")

def restart():
    global score1,score,p,g
    b1.configure(state=ACTIVE)
    score=0
    score1=0
    p=''
 
    a2.set(score)
    a1.set(score1)
    l5.config(text=p)
    l8.config(text=p)
    l9.config(text=p)
   
   
   


#scoreboard
l6=Label(a,text="player1 score")
l6.place(x=40,y=80)

e2=Entry(a,text=a1)
e2.place(x=40,y=120,width=44,height=35)


l7=Label(a,text="player2 score")
l7.place(x=320,y=80)

e3=Entry(a,text=a2)
e3.place(x=320,y=120,width=44,height=35)


#labels
l1=Label(a,text="player 1")
l1.place(x=30,y=10,width=64,height=35)


l2=Label(a,text="vs")
l2.place(x=210,y=10,width=44,height=35)


l3=Label(a,text="player 2")
l3.place(x=350,y=10,width=64,height=35)

l4=Label(a,text='SCORE')
l4.place(x=150,y=80,width=64,height=35)

l8=Label(a,text=" ",bg="white",fg="red")
l8.place(x=150, y=230,width=105,height=35)

#button

b1=Button(a,text='Roll player1',command=play1,state=ACTIVE)
b1.place(x=30,y=290,width=80,height=35)


b2=Button(a,text='Roll player2',command=play2,state=DISABLED)
b2.place(x=290,y=290,width=80,height=35)

restart=Button(a,text='Restart',command=restart,state=DISABLED,bg='red',font=('times',14,'bold'))
restart.place(x=160,y=420,width=80,height=35)

wd.mainloop()
