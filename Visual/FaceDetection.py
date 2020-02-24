import os

import cv2
import face_recognition
import dlib


class VisualProcessor:
    # gets user input and creates new directory
    # of that name, then opens camera and takes
    # 30 photos and writes to new directory, these
    # photos can be found in 'Dataset' and are used for
    # facial recognition
    def collect_dataset(self):
        name = input("what is your name?")
        path = "C:\\Users\\Admin\\PycharmProjects\\Therapy-bot\\Visual\\Dataset"
        os.chdir(path)

        check_os = os.getcwd()
        print("Current working Directory: " + check_os)

        new_dir = check_os + "\\" + name
        print(new_dir)
        try:
            os.mkdir(new_dir)
        except OSError:
            print("Error creating %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        camera = cv2.VideoCapture(0)

        for i in range(30):
            return_value, image = camera.read()
            path = new_dir
            cv2.imwrite(os.path.join(path, name + str(i) + '.png'), image)
        del camera

    def visualrec(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        video = cv2.VideoCapture(0)

        while True:
            check, frame = video.read()
            frame = cv2.resize(frame, (320, 240))
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_img,
                                                  scaleFactor=1.05,
                                                  minNeighbors=5)

            # take position values from face_cascade and draw rectangle around face
            for x, y, w, h in faces:
                gray_img = cv2.rectangle(gray_img, (x, y), (x + w, y + h), (255, 255, 255), 1)
                cv2.putText(gray_img, 'Wow what a cutie', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                            1)

            # opens window to view webcam
            cv2.imshow("dickhead on cam", gray_img)
            key = cv2.waitKey(1)

            # exit key
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    def recognizer(self):
        print("todo")
        # ToDO

    def detectMood(self):
        print("todo")
        # ToDo
