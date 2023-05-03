from tkinter import*
from tkinter.ttk import *
import time
wd=Tk()
wd.title('Progress bar')
wd.geometry('300x500')

def start():
    if (z['value']<100):
        z['value']+=20
        z.update_idletasks()
        time.sleep(1)
        start()
        
z=Progressbar(wd,orient='horizontal',length=500,mode='determinate')
z.pack()
a=Button(wd,text='Start',command=start)
a.pack(padx=5,pady=5)

def stop():
    z.stop()


b=Button(wd,text='stop',command=stop)
b.pack()


wd.mainloop()
