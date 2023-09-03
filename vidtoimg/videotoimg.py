import numpy as np
import cv2
import os
from glob import glob
vid = cv2.VideoCapture(cv2.samples.findFile("menu1.mp4"))
currentframe = 0

if not os.path.exists('data'):
    os.makedirs('data')

while (True):
    success, frame = vid.read()
    
    #cv2.imshow("Output", frame)
    cv2.imwrite('./data/frame' + str(currentframe) + '.jpg', frame)
    currentframe +=1
    
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
    
vid.release()
cv2.destroyAllWindows()