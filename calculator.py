from tkinter import*
wd=Tk()
wd.title('Calculator')
wd.geometry('300x300')



input_text=StringVar()
input_Frame=Frame(wd,height=50,width=250,bg='White',border=1)
input_Frame.pack()

input_text=Entry(input_Frame, text=input_text, fg="Red")
input_text.pack()


input_text=StringVar()
input_Frame1=Frame(wd,height=50,width=250,bg='White',border=1)
input_Frame1.pack()

a=Frame(wd,height=20,width=15,border=1).pack()
button=Button(a,text='0',bg='white',height=3,width=5).pack(side=BOTTOM)


b=Frame(wd,height=20,width=15,border=1).pack()
button1=Button(b,text='1',bg='white',height=3,width=5).pack(side=LEFT)

c=Frame(wd,height=20,width=15).pack()
button2=Button(c,text='2',bg='white',height=3,width=2).pack(side=LEFT)

d=Frame(wd,height=20,width=15).pack()
button3=Button(d,text='3',bg='white',height=3,width=5).pack(side=LEFT)

e=Frame(wd,height=20,width=15).pack()
button4=Button(e,text='4',bg='white',height=3,width=5).pack(side=TOP)

f=Frame(wd,height=20,width=15).pack()
button5=Button(f,text='5',bg='white',height=3,width=5).pack(side=TOP)

g=Frame(wd,height=20,width=15).pack()
button6=Button(g,text='6',bg='white',height=3,width=5).pack(side=TOP)

h=Frame(wd,height=20,width=15).pack()
button7=Button(h,text='7',bg='white',height=3,width=5).pack(side=TOP)

i=Frame(wd,height=20,width=15).pack()
button8=Button(i,text='8',bg='white').pack(side=TOP)

j=Frame(wd,height=20,width=15).pack()
button9=Button(j,text='9',bg='white',height=3,width=5).pack(side=LEFT)

k=Frame(wd,height=20,width=15).pack()
button10=Button(k,text='+',bg='white',height=3,width=5).pack(side=RIGHT)

l=Frame(wd,height=20,width=15).pack()
button11=Button(l,text='-',bg='white',height=3,width=5).pack(side=RIGHT)

m=Frame(wd,height=20,width=15).pack()
button12=Button(m,text='*',bg='white',height=3,width=5).pack(side=RIGHT)

n=Frame(wd,height=20,width=15).pack()
button13=Button(n,text='/',bg='white',height=3,width=5).pack(side=RIGHT)





wd.mainloop()
