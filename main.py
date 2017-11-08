# -*- coding: utf-8 -*-

'''
Author: João Areias
Project: Enable Reader

This is the main file on project E-Reader which will control
face detection threads and PDF reading
'''


from face_detection import Detect


def main():
    detection_thread = Detect()
    detection_thread.start()

if __name__ == '__main__':
    main()
