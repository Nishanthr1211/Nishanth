'''
from tkinter import *  
  
win= Tk()  
sbb = Scrollbar(win)  
sbb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(win, yscrollcommand = sbb.set)  
  
for line in range(45):  
    mylist.insert(END, "Value " + str(line))

ls=["Nishanth",
    "Sarath",
    "Praba",
    "Sabarish",
    "Nithish"]
for i in ls:
       mylist.insert(END,""+str(i))
    
mylist.pack(side = LEFT)
sbb.config(command = mylist.yview)
  
win.mainloop()
'''

from tkinter import *  
 
win= Tk()
win.geometry("200x200")
h = Scrollbar(win,orient="horizontal")  
h.pack(side = BOTTOM, fill = 'x')
text=Text(win, font=("Calibri, 16"), wrap=NONE, xscrollcommand=h.set)
text.pack()

for i in range(5):
   text.insert(END, "Welcome to TNSDC Program..")
h.config(command = text.xview)
 
win.mainloop()

