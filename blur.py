import cv2
'''
i=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\Bike1.png")
a=cv2.blur(i,(5,5))
cv2.imshow("blur",a)
'''
#Video Blur
'''
a=cv2.VideoCapture(0)

while True:
    ret,frame=a.read()
    c=cv2.blur(frame,(10,10))
    cv2.imshow("original",frame)
    cv2.imshow("blur",c)
    v=cv2.waitKey(5) & 0xFF
    if v==27:
        break

    
cap.release()
cv2.destroyAllWindows()
'''
'''
#Median Blur
i=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\Bike1.png")
c=cv2.medianBlur(i,51)
cv2.imshow("blur",c)
''''''

#GaussianBlur
i=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\Bike1.png")
c=cv2.GaussianBlur(i,(11,11),cv2.BORDER_REFLECT)
cv2.imshow("blur",c)
'''
#Bilateral Filter
i=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\bike2.png")
m=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\bike2.png")
cv2.imshow("original",m)
c=cv2.bilateralFilter(i,5,125,125)


cv2.imshow("blur",c)

