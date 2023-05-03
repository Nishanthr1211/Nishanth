'''
from tkinter import*
import datetime
from time import strftime

def time():
    string=strftime('%H:%M:%S:%p')
    a=config(text=string)
    a.after(1000,time)
    

wd=Tk()
wd.title("Clock")
wd.geometry("500x500")


a = Label(wd, font= ('Times New Roman', 100, 'bold'),
            background='Blue',
            foreground='gray')
a.pack(anchor="center")
time()


wd.mainloop()


from tkinter import*
import datetime
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    a.config(text = string)
    a.after(1000, time)
    



wd=Tk()
wd.title("clock")
wd.geometry("400x500")

a = Label(wd, font = ('TimeNewRoman', 100, 'bold'),
            background = 'red',
            foreground = 'gray')
a.pack(anchor = 'center')
time()
wd.mainloop()
 '''


from tkinter import *
import datetime
def time():

    a.config(text=datetime.datetime.now())
    a.after(1000,time)




wd=Tk()
wd.title('clock')
wd.geometry('500x400')

a=Label(wd,font=('50'))
a.pack()
time()



wd.mainloop()




