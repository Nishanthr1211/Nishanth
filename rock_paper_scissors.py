from tkinter import*
import random

window=Tk()
window.title("Rock paper Scissor")
window.geometry("600x600")
frame=Frame(window,width=450,height=450)
frame.grid(row=0,column=0)
a=PhotoImage(file="white.png")
c=PhotoImage(file="angel.png")
label5=Label(frame, image=a)
label5.grid(row=1, column=0)
label6=Label(frame, image=c,)
label6.grid(row=1, column=2)
v=PhotoImage(file="stone1.png")
w=PhotoImage(file="paper1.png")
x=PhotoImage(file="scissor1.png")
label4=Label(frame, text="YOU",font=('Georgia 25'))
label4.grid(row=0, column=0)
label3=Label(frame, text="ANGEL",font=('Georgia 25'))
label3.grid(row=0, column=2)
l=StringVar()

def func(d):
    global l
    a=["Rock","Paper","Scissor"]
    b=random.choice(a)
    #label1=Label(frame, text=b)
    #label1.grid(row=0, column=2)
    if d=="Rock":
        if b=="Rock":
            #l.set("Match Draw")
            label1=Label(frame,image=v)
            label1.grid(row=1,column=0)
            label2=Label(frame,image=v)
            label2.grid(row=1,column=2)
            mylabel=Label(text=" MatchDraw ",font=('Georgia 25')).grid(row=4,column=0)
           
        elif(b=="Paper"):
            #l.set("You  lost")
            label1=Label(frame,image=v)
            label1.grid(row=1,column=0)
            label2=Label(frame,image=w)
            label2.grid(row=1,column=2)
            mylabel=Label(text="   You  Lost  ",font=('Georgia 25')).grid(row=4,column=0)
        else:
            #l.set("You   won")
            label1=Label(frame,image=v)
            label1.grid(row=1,column=0)
            label2=Label(frame,image=x)
            label2.grid(row=1,column=2)
            mylabel=Label(text="   You   Won   ",font=('Georgia 25')).grid(row=4,column=0)
    elif d=="Paper":
        if b=="Paper":
            #l.set("Match Draw")
            label1=Label(frame,image=w)
            label1.grid(row=1,column=2)
            label2=Label(frame,image=w)
            label2.grid(row=1,column=0)
            mylabel=Label(text="   MatchDraw  ",font=('Georgia 25')).grid(row=4,column=0)
        elif(d=="Rock"):
            #l.set("You won")
            label1=Label(frame,image=v)
            label1.grid(row=1,column=0)
            label2=Label(frame,image=w)
            label2.grid(row=1,column=2)
            mylabel=Label(text="   You   Won  ",font=('Georgia 25')).grid(row=4,column=0)
        else:
            #l.set("You  lost")
            label1=Label(frame,image=x)
            label1.grid(row=1,column=2)
            label2=Label(frame,image=w)
            label2.grid(row=1,column=0)
            mylabel=Label(text="  You  Lost  ",font=('Georgia 25')).grid(row=4,column=0)
    elif d=="Scissor":
        if b=="Scissor":
            #l.set("Match Draw")
            label1=Label(frame,image=x)
            label1.grid(row=1,column=2)
            label2=Label(frame,image=x)
            label2.grid(row=1,column=0)
            mylabel=Label(text=" MatchDraw ",font=('Georgia 25')).grid(row=4,column=0)
        elif(d=="Rock"):
            #l.set("You  lost")
            label1=Label(frame,image=v)
            label1.grid(row=1,column=0)
            label2=Label(frame,image=x)
            label2.grid(row=1,column=2)
            mylabel=Label(text="  You   lost  ",font=('Georgia 25')).grid(row=4,column=0)
        else:
            #l.set("You   won")
            label1=Label(frame,image=w)
            label1.grid(row=1,column=2)
            label2=Label(frame,image=x)
            label2.grid(row=1,column=0)
            mylabel=Label(text="  You   Won  ",font=('Georgia 25')).grid(row=4,column=0)
label1=Label(frame, text="Vs",font=('Georgia 40'))
label1.grid(row=1, column=1)       
#entry=Entry(window,text=l,font=('Georgia', 20),bg="red")
#entry.grid(row=5,column=0)


btn1=Button(frame,text="Rock",image=v,padx=10,pady=10,command = lambda:func("Rock") ).grid(row=2,column=0)
btn2=Button(frame,text="Paper",padx=10,pady=10,image=w,command = lambda:func("Paper")).grid(row=2,column=1)
btn3=Button(frame,text="Scissor",padx=10,pady=10,image=x,command = lambda:func("Scissor")).grid(row=2,column=2)
window.mainloop()



 
