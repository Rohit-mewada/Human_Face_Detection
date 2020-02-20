import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
faces = face.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),15)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
