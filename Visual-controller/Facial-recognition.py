import cv2
import time


# utilizes haarcascade

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# enter in webcam path or 0,1,2,3

video = cv2.VideoCapture(0)
a = 1

# loops through each video frame

while True:
    a = a+1
    check, frame = video.read()
    print(check)
    print(frame)

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,
     scaleFactor=1.05,
     minNeighbors=5)

    for x, y, w, h in faces:
        gray_img = cv2.rectangle(gray_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Capture", gray_img)


    key = cv2.waitKey(1)

    if key == ord ('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()

