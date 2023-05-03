from tkinter import*
window=Tk()
window.title("webpage")
menubar=Menu(window)
def name():
    win=Tk()
    win.title("NAME")
    label=Label(win,text="NISHANTH")
    label.pack()
    win.mainloop()
def cont():
    wi=Tk()
    wi.title("contact")
    label=Label(wi,text="8940417306")
    label.pack()
    wi.mainloop()
def quit():
    return
btn=Button(window,text="home",command=name)  
menubar.add_command(label="NAME",command=name)
menubar.add_command(label="Contact",command=cont)
window.config(menu=menubar)

window.mainloop()
