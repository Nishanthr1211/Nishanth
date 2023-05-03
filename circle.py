import cv2

img=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\Bike1.png")

#(h,b)=img.shape[::2]

center=(int(150),int(90))

cv2.circle(img,(150,150),10,(8,8,18),(40))
cv2.imshow('img',img)

cv2.rectangle(img,(150,150),(0,0),(8,8,18),(40))
cv2.imshow('img',img)

cv2.line(img,(80,80),center,(0,0,255),5)
cv2.imshow('img',img)

cv2.putText(img,'Nishanth',(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),5)
cv2.imshow('img',img)

