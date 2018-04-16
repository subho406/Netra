import os
import cv2
import time
import numpy as np
import argparse
import imutils

from imutils.video import FPS,VideoStream
from multiprocessing import Queue

import datetime

MAX = 20

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())


vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
fps = FPS().start()

while(True):
    # Capture frame-by-frame
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S.%f%p")
    #output_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    file = "//home/hdp/Documents/Netra/img/"+ts+".png"
    # Display the resulting frame
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
    	0.35, (0, 0, 255), 1)
    cv2.imshow('frame',frame)
    cv2.imwrite(file, frame)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
    	0.007843, (300, 300), 127.5)


    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break



fps.stop()


# When everything done, release the capture
vs.stop()
cv2.destroyAllWindows()