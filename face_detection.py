# -*- coding: utf-8 -*-

'''
Author: João Areias
Project: Enable Reader

This file detect faces and blinks, which will
trigger the event for turning pages
'''
from WebcamVideoStream import WebcamVideoStream
import threading
import cv2


class Detect(threading.Thread):
    """
            Here it will be created a thread to find faces and
            detect blinking
    """

    def _detect(self):

        # Benchmark results
        runs = 0
        eyes = 0
        
        """Class function to detect faces and eyes within faces"""
        video_stream = WebcamVideoStream()
        video_stream.start()
        # Cascade Classifiers
        face_cascade = cv2.CascadeClassifier(
            'haarcascades/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
        while True:
            frame = video_stream.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detecting faces and eyes
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+h]
                roi_color = frame[y:y+h, x:x+h]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                print('[FACE DETECTION] %d eyes detected' % len(eyes))
                if len(eyes)/len(faces) == 2:
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey),
                                      (ex+ew, ey+eh), (0, 255, 0), 1)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_stream.stop()
                break
            
            # Display image
            cv2.imshow('Image', frame)


    def run(self):
        """Run threads"""
        self._detect()
        cv2.destroyAllWindows()
