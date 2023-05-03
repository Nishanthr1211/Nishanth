import cv2

#img=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\logo.png")
#print(img.shape[::2])
#a=img.shape[0]*(10/100)
#b=img.shape[1]*(10/100)
'''
#cv2.resize(img
cv2.imshow("pic",img)
pixel=img[100,100]
print(pixel)
cv2.imshow("new",img)

#b=cv2.imwrite("C:\\Users\\Nishanth\\Downloads\\Pc.png")
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])
print(img.size)

bgr=cv2.split(img)
print('\n',"******************BGR*******************",'\n')
print(bgr)
'''


h1=400
w1=400
dim=(h1,w1)
p=cv2.resize(cv2.imread("C:\\Users\\Nishanth\\Downloads\\rock.png"),(h1,w1))
cv2.imshow("Resized window1",p)



h1=350
w1=350
dim=(h1,w1)
p1=cv2.resize(cv2.imread("C:\\Users\\Nishanth\\Downloads\\Paper.png"),(h1,w1))
cv2.imshow("Resized window",p1)

h1=650
w1=650
dim=(h1,w1)
p2=cv2.resize(cv2.imread("C:\\Users\\Nishanth\\Downloads\\Paper.png"),(h1,w1))
cv2.imshow("Resized window2",p2)

img=cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\Paper.png")
a,b=img.shape[:2]
print(a)
print(b)
dim=(a,b)
center=((a/2),(b/2))
scale=1.0
i=cv2.getRotationMatrix2D(center,90,scale)
v=cv2.warpAffine(img,i,dim)
cv2.imshow("ooo",v)
