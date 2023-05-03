import tkinter as tk
import sys
import time
import calendar
import random
import datetime as dt
from tkinter import *


""" DICTIONARY PHRASES """
phrases = ["Phrase1", "Phrase2", "Phrase3"]




class Clock(tk.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tk.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%I:%M:%S %p')
        else:
            self.time     = time.strftime('%I:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S %p')
        else:
            new_time = time.strftime('%I:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)



class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom



root=tk.Tk()


root.configure(bg="blue")


root.wm_attributes('-fullscreen','true')
tk.Button(root, text="Quit", bg="black", fg="black", command=lambda root=root:quit(root)).pack()


clock1 = Clock(root)
clock1.pack()


clock1.configure(bg='black',fg='white',font=("helvetica",125))


date = dt.datetime.now()

format_date = f"{date:%a, %b %d %Y}"


phrase_print = random.choice(phrases)

w = Label(root, text=format_date, fg="white", bg="black", font=("helvetica", 40))
w.pack()


e = Label(root, text=phrase_print, fg="white", bg="black", font=("helvetica", 28))
e.pack()


root.mainloop()
