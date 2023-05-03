from tkinter import *
import random
wd=Tk()
wd.title("DATA")
wd.geometry("500x500")
a=Frame(wd,height=400,width=300,bg="black")
a.place(x=75,y=20)
b=Frame(a,height=380,width=280,bg="white")
b.place(x=10,y=10)
name=Label(b,text="RN",font=("Times New Roman",40,"bold"),fg="red",bg="white")
name.place(x=90,y=150)
d=Frame(a,height=50,width=280,bg="black")
d.place(x=10,y=360)
l=StringVar()
l1=StringVar()
def profile():
    c=Frame(b,height=350,width=280,bg="white")
    c.place(x=0,y=0)
    p = "Name : Nishanth \n Date of birth : 12 - 11 - 2001"
    a1=Label(c,text=p,bg="white",fg="black")
    a1.place(x=70,y=150)
def contact():
    c=Frame(b,height=350,width=280,bg="white")
    c.place(x=0,y=0)
    p="Nishanth : 9543822820 \n daddy : 9600571603"
    # create the word docs and then save the contacts to read and write the data in this window
    a2=Label(c,text=p,bg="white",fg="black")
    a2.place(x=80,y=150)
def home():
    c=Frame(b,height=350,width=280,bg="white")
    name=Label(b,text="RN",font=("Times New Roman",40,"bold"),fg="red",bg="white")
    name.place(x=90,y=150)
    c.place(x=0,y=0)
def game():
    #game frame
    bb=Frame(b,width=280,height=350,bg="white")
    bb.pack()
    name1=Label(bb,text="Let's Play",font=("Times New Roman", 20 , "bold","underline"),fg="green",bg="white")
    name1.place(x=80,y=20)
    game1=Label(bb,text="Result",font=("Times New Roman", 20 , "bold","underline"),fg="black",bg="white")
    game1.place(x=100,y=200)
    vs1=Label(bb,text="User        Vs        Computer",font=("Times New Roman", 15 , "bold","underline"),fg="gray",bg="white")
    vs1.place(x=25,y=100)
    def rock():
        value=random.choice(["     Rock     ","   Paper   ","   Scissor  "])
        if value== "     Rock     ":
            result="        Tie        "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="     Rock     ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="orange")
            cc.place(x=80,y=242)
        elif value=="   Paper   ":
            result="    You Lost  "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="     Rock     ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="red")
            cc.place(x=80,y=242)
        elif value =="   Scissor  ":
            result="    You Won "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="     Rock     ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="green")
            cc.place(x=80,y=242)
    def paper():
        value=random.choice(["     Rock     ","   Paper   ","   Scissor  "])
        if value== "     Rock     ":
            result="    You Won "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Paper   ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="green")
            cc.place(x=80,y=242)
        elif value=="   Paper   ":
            result="        Tie        "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Paper   ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="orange")
            cc.place(x=80,y=242)
        elif value=="   Scissor  ":
            result="    you Lost  "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Paper   ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="red")
            cc.place(x=80,y=242)
        
    def scissor():
        value=random.choice(["     Rock     ","   Paper   ","   Scissor  "])
        if value== "     Rock     ":
            result="    You Lost  "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Scissor  ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="red")
            cc.place(x=80,y=242)
        elif value=="   Paper   ":
            result="    You Won "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Scissor  ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="green")
            cc.place(x=80,y=242)
        elif value=="   Scissor  ":
            result="        Tie        "
            cc1=Label(bb,text=value,font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc1.place(x=175,y=125)
            cc2=Label(bb,text="   Scissor  ",font=("Times New Roman", 13 , "bold"),fg="blue",bg="white")
            cc2.place(x=15,y=125)
            cc=Label(bb,text=result,bg="white",font=("Times New Roman", 15 , "bold"),fg="orange")
            cc.place(x=80,y=242)
    #user interface button for game  
    
    btn1=Button(bb,text="Rock",command=rock)
    btn1.place(x=80,y=300)
    btn2=Button(bb,text="Paper",command=paper)
    btn2.place(x=130,y=300)
    btn3=Button(bb,text="Scissor",command=scissor)
    btn3.place(x=180,y=300)
#camera
lab=Label(a,text="O",bg="black",fg="white")
lab.place(x=145,y=8)
#mobile buttom frame buttons
home=Button(d,text="HOME",command=home)
home.place(x=20,y=6)
profile=Button(d,text="Profile",command=profile)
profile.place(x=80,y=6)
contact=Button(d,text="CONTACT",command=contact)
contact.place(x=145,y=6)
game=Button(d,text="Game",command=game)
game.place(x=230,y=6)
wd.mainloop()
