import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    now=datetime.now()
    date_string = now.strftime("%Y-%m-%d-%H:%M:%S.%f")
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    file = "//home/hdp/Documents/Netra/img/"+date_string+".png"
    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite(file, gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()