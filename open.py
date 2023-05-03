import cv2
import numpy as np
'''
img=cv2.imread(f"C:\\Users\\Nishanth\\Downloads\\bike2.png")
#a=cv2.imwrite(image=img)
a=cv2.Canny(img,100,200,L2gradient=True)
cv2.imshow("Hi",a)
'''


a=cv2.VideoCapture(0)
while(1):
    ret,frame=a.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([30,150,50])
    upper_red=np.array([255,255,180])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("orignal",frame)
    i=cv2.Canny(frame,100,200)
    cv2.imshow("Original",i)
    

    b=cv2.waitKey(5)&0xFF
    if(b==27):
        break

a.release()
