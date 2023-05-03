from tkinter import *

wd=Tk()
wd.title('Nishanth')
wd.geometry('500x600')

a =Frame(wd,width=300, height=100)
a.pack(side=TOP)
label =Label(a,width=100,height=150,bd=0,text="I'm Nishanth")
label.pack()

a.pack(side=TOP)

wd.mainloop()
