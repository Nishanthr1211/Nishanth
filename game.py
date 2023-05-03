from tkinter import*
import random

wd=Tk()
wd.title('Game')
wd.geometry('300x500')

l=StringVar()

oo=StringVar()


def func(i):
    n=['Rock','Paper','Scissors']
    m=random.choice(n)
    l.set(m)
    if i=='Rock':
        if m=="Rock":
            g=("Match Draw")
        elif m=="Paper":
            g=("You Won")
        else:
            g=("Match Lost")    
    elif i=='Scissors':
        if m=="Scissors":
            g=("Match Draw")
        elif m=='Rock':
            g=("You Won")
        else:
            g=("Match Lost")
            
    elif i=='Paper':
        if m=="Paper":
            g.place("Match Draw")
        elif m=='Rock':
            g=("You Won")
        else:
            g=("Match Lost")

    n=Label(wd,text=g,border=1,bg='White')
    n.place(x=75,y=200)
            
label=Label(wd,text = "Rock Paper Scissor",
	font = "normal 20 bold",
	fg = "blue").pack()

o=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\rock.png")
a=Button(wd,text='Rock',command=lambda:func("Rock"),bg='Blue',image=o)
a.place(x=75,y=75)

o1=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\paper.png")
b=Button(wd,text='Paper',command=lambda:func("Paper"),bg='yellow',image=o1)
b.place(x=230,y=75)

o2=PhotoImage(file="C:\\Users\\Nishanth\\Downloads\\scissors.png")
c=Button(wd,text='scissors',command=lambda:func("Scissors"),bg='cyan',image=o2)
c.place(x=370,y=75)

h=Entry(wd,text=l,bg='red')
h.place(x=80,y=250)

wd.mainloop()        
