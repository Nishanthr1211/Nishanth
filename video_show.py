import cv2
from tkinter import*                             
wd=Tk()
wd.title("Video Play")
wd.geometry('600x660')

def videoplay():
    cap=cv2.VideoCapture("C:\\Users\\Nishanth\\Desktop\\Voice of Unity Lyric Video - Maanaadu - Silambarasan TR - Yuvan Shankar Raja - Arivu - Venkat Prabhu.mp4")

    while True:
        ret,frame=cap.read()
        cv2.imshow("original",frame)
    cap.release()
    
button=Button(wd,text="Video Play",bg='Blue',command=videoplay).pack() 
    
cv2.destroyAllWindows()
