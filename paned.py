from tkinter import*
a=Tk()
a.title("Window")
a.geometry('500x500')
def add():
    x=int(e1.get())
    y=int(e2.get())
    u=x+y
    n1.insert(1,str(u))

def sub():
    x=int(e1.get())
    y=int(e2.get())
    u=x-y
    n1.insert(1,str(u))

def mul():
    x=int(e1.get())
    y=int(e2.get())
    u=x*y
    n1.insert(1,str(u))

def div():
    x=int(e1.get())
    y=int(e2.get())
    u=x/y
    n1.insert(1,str(u))


    
o=PanedWindow(a)
o.pack(expand=1)

p=PanedWindow(o,bd=2,bg='blue')
o.add(p)
n1=Entry(o,bd=2,bg='yellow')

o.add(n1)

e1=Entry(p)
p.add(e1)
e2=Entry(p)
p.add(e2)

b=Button(p,text="add",command=add)
p.add(b)

b1=Button(p,text="sub",command=sub)
p.add(b1)

b2=Button(p,text="mul",command=mul)
p.add(b2)

b3=Button(p,text="div",command=div)
p.add(b3)


