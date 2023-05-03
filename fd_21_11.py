import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade.xml')
a=cv2.VideoCapture(0)
while(1):
    ret,img=a.read()
    # Read the input image
    #img = cv2.imread(r"C:\\Users\\Nishanth\\Downloads\\photo.jpg")
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    i=0
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        i=i+1
        cv2.putText(img,"Person "+str(i),(10,100),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0),5)
        
    # Display the output
    cv2.imshow('img', img)
    x=cv2.waitKey(5) & 0xFF
    if (x==27):
        break
a.release()
cv2.destroyAllWindows()

