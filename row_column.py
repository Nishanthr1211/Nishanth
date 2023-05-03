import tkinter as tk
a=tk.Tk()
a.title("Row Column")
for i in range(5):
    for j in range(4):
        frame=tk.Frame(
            master=a,
            relief=tk.RAISED,
            borderwidth=1
            )
        frame.grid(row=i,column=j)
        label=tk.Label(master=frame,text=f"Row{i}\nColumn{j}")
        label.pack()

import tkinter as tk
b=tk.Tk()
b.title("Row Column")
for i1 in range(5):
    for j1 in range(3):
        frame1=tk.Frame(
            master=b,
            relief=tk.RAISED,
            borderwidth=1
            )
        frame1.grid(row=i1,column=j1,ipadx=4,ipady=4)
        label=tk.Label(master=frame1,text=f"Row{i1}\nColumn{j1}")
        label.pack()


import tkinter as tk
c=tk.Tk()
c.title("Row Column")
for i2 in range(5):
    for j2 in range(3):
        frame2=tk.Frame(
            master=c,
            relief=tk.RAISED,
            borderwidth=1
            )
        frame2.grid(row=i2,column=j2,padx=4,pady=4)
        label=tk.Label(master=frame2,text=f"Row{i2}\nColumn{j2}")
        label.pack()
c.mainloop()
b.mainloop()
a.mainloop()
