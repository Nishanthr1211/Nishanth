#Mouse Event
import cv2
import numpy as np
def draw_circle(a,x,y,flags,param):
    if(a==cv2.EVENT_LBUTTONDBLCLK):
        cv2.rectangle(m,(x,y),(10,12),(255,255,255),-1)
        



m=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\photo.jpg")
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)
while(1):
    cv2.imshow("image",m)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()

#cv2.circle(m,(x,y),100,(255,255,0),-1)
