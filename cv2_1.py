import cv2
from tkinter import*
wd=Tk()
wd.title("Rotate Screen")
wd.geometry("500x600")


img=cv2.imread("C:\\Users\\Nishanth\\Downloads\\Photo.png")


(h, w) = img.shape[::2]


center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0


M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

button=Button(wd,text='   90   ').place(x=10,y=500)


M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w, h))

button1=Button(wd,text='   180   ').place(x=75,y=850)

# 270 degrees
M = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M, (h, w))

button2=Button(wd,text='   270   ').place(x=120,y=1200)

cv2.imshow('Original Image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

cv2.imshow('Image rotated by 90 degrees',rotated90)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

cv2.imshow('Image rotated by 180 degrees',rotated180)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

cv2.imshow('Image rotated by 270 degrees',rotated270)
cv2.waitKey(0) 
cv2.destroyAllWindows() 



