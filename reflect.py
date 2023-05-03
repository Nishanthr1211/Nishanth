import cv2
import datetime
import numpy as np

rgb_img=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\photo.jpg",1)

gray_img=cv2.cvtColor(rgb_img,cv2.COLOR_BGR2GRAY)

template=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\photo1.png",0)

w, h = template.shape[::1]

res=cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)

threshold=0.9

m=0

a=("C:\\Users\\Nishanth\\Downloads\\photo.jpg")
    
loc=np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(gray_img,pt,(pt[0]+w,pt[1]+h),(255,255,255),2)
    cv2.imshow("Original",rgb_img)
    cv2.imshow("Detected",gray_img)
    
for i in range(m<=10):
    c=open("C:\\Users\\Nishanth\\Desktop\\reflect.txt","a")
    b=datetime.datetime.now()
    c.write(str(a)+str(b))
    count=+1

    c.close()
    
              




