from tkinter import *
from tkinter import filedialog
import qrcode

root = Tk()
root.title("NSDC Attendance")
root.geometry("450x600")
frame_1 = Frame(root,width=450,height=600, bg = "White").place(x=0,y=0)
l=StringVar()

def new_register():
    frame_2 = Frame(frame_1,width=450,height=600,bg = "Red").place(x=0,y=0)
    label = Label(frame_2, text="Enter new Name :").place(x=50, y=70)
    entry = Entry(frame_2,text=l).place(x=150,y=70)
    label = Label(frame_2, text="Enter Number :").place(x=50, y=100)
    entry2 = Entry(frame_2).place(x=150,y=100)
    label = Label(frame_2, text="Enter E-mail Id :").place(x=50, y=130)
    entry3 = Entry(frame_2).place(x=150,y=130)
    generate_button = Button(frame_2, text="Generate QR code",command=generate_qr).place(x=110,y=160)
    return()
def generate_qr():
    Text =l.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(Text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(Text+".png")
    #label.config(text="QR code saved!")


register_btn = Button(frame_1, text="Register", command=new_register).place(x=225,y=300)
#entry_btn = Button(frame_1, text = "Entry", command = entry).place(x=225,y=370)
root.mainloop()
