import argparse
import os
import pickle

import cv2
import face_recognition
from imutils import paths
import dlib


class VisualProcessor:

    # uses haarcascade to detect face
    # won't start next operations until face is detected
    def detect_face(self):
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

    def encode_faces(self):
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--dataset", required=True,
                        help="path to input directory of faces + images")
        ap.add_argument("-e", "--encodings", required=True,
                        help="path to serialized db of facial encodings")
        ap.add_argument("-d", "--detection-method", type=str, default="hog",
                        help="face detection model to use: either `hog` or `cnn`")
        args = vars(ap.parse_args())

        # grab the paths to the input images in our dataset
        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images("C:\\Users\\Admin\\PycharmProjects\\Therapy-bot\\Visual\\Dataset"))
        print(imagePaths)
        # initialize the list of known encodings and known names
        knownEncodings = []
        knownNames = []

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1,
                                                         len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            print(imagePath)
            image = cv2.imread(imagePath)
            cv2.imshow('image', image)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb, model=args["detection_method"])

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(name)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")
        data = {"encodings": knownEncodings, "names": knownNames}
        f = open(encodings.pickle, "wb")
        f.write(pickle.dumps(data))
        f.close()

    def recognizer(self):
        print("todo")
        # ToDO

    def detectMood(self):
        print("todo")
        # ToDo
