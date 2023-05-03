from tkinter import*

wd=Tk()
wd.title('Calculator')
wd.geometry('500x700')

l=StringVar()
frame=Frame(wd,height=500,width=400,border=1)
frame.pack(side=TOP)

a=Entry(frame,text=l,fg='black')
a.place(x=1,y=10,width=350,height=45)

p=" "
def click(item):
    global p
    p=p+str(item)
    l.set(p)

def equal():
    global p
    res=str(eval(p))
    l.set(res)
    p=" "
    

def clear():
    global p
    p=" "
    l.set(p)




button0=Button(frame,text='0',fg='black',bg='red',height=3,width=5,command=lambda:click(0)).place(x=15,y=70)

button1=Button(frame,text='1',fg='black',bg='red',height=3,width=5,command=lambda:click(1)).place(x=75,y=70)

button2=Button(frame,text='2',fg='black',bg='red',height=3,width=5,command=lambda:click(2)).place(x=145,y=70)

button3=Button(frame,text='3',fg='black',bg='red',height=3,width=5,command=lambda:click(3))

button4=Button(frame,text='4',fg='black',bg='red',height=3,width=5,command=lambda:click(4))

button5=Button(frame,text='5',fg='black',bg='red',height=3,width=5,command=lambda:click(5))

button6=Button(frame,text='6',fg='black',bg='red',height=3,width=5,command=lambda:click(6))

button7=Button(frame,text='7',fg='black',bg='red',height=3,width=5,command=lambda:click(7))

button8=Button(frame,text='8',fg='black',bg='red',height=3,width=5,command=lambda:click(8))

butto9=Button(frame,text='9',fg='black',bg='red',height=3,width=5,command=lambda:click(9))

buttonop1=Button(frame,text='+',fg='black',bg='red',height=3,width=5,command=lambda:click('+'))

buttonop2=Button(frame,text='-',fg='black',bg='red',height=3,width=5,command=lambda:click('-'))

buttonop3=Button(frame,text='*',fg='black',bg='red',height=3,width=5,command=lambda:click('*'))

buttonop4=Button(frame,text='/',fg='black',bg='red',height=3,width=5,command=lambda:click('/'))

buttonop5=Button(frame,text='=',fg='black',bg='red',height=3,width=5,command=equal)

buttonop6=Button(frame,text='C',fg='black',bg='red',height=3,width=5,command=clear)

wd.mainloop()
