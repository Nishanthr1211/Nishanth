import cv2

cap=cv2.VideoCapture(0)
i=0

while True:
    
    ret,frame=cap.read()
    '''
    rectangle=cv2.rectangle(frame,(425,350),(120,120),(8,8,18),(5))
    cv2.imshow('Camera',frame)

    circle=cv2.circle(frame,(300,300),140,(0,1,255),(5))
    cv2.imshow('Camera',frame)

    a=cv2.VideoWriter_fourcc(*'XVID')
    o=cv2.VideoWriter('output.avi',a,20.0,(640,480))
    cv2.imshow('Camera',frame)
    
    
'''

    if ret== False:
        break
    cv2.imwrite("C:\\Users\\Nishanth\\Desktop\\New folder (2)\\a" +str(i)+'.jpg',frame)
    i+=1
    a=cv2.waitKey(1)
    cv2.imshow('org',frame)
    
cap.release()
cv2.destroyAllWindows()

