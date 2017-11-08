# -*- coding: utf-8 -*-

"""  This file implements a threaded
video capture program for suplying images
to the face detection.

The implementation is as shown in:
https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
"""

from threading import Thread
import cv2

class WebcamVideoStream(object):
	"""WebcamVideoStream allows for multithreaded
	image io.
	"""
	def __init__(self, src=0):
		self.stream = cv2.VideoCapture(src)
		self.grabbed, self.frame = self.stream.read()
		self.stopped = False

	def start(self):
		Thread(target=self.update).start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return
			self.grabbed, self.frame = self.stream.read()

	def stop(self):
		self.stopped = True
		self.stream.release()

	def read(self):
		return self.frame
