from cv2 import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)
pTime = 0

while True:

    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                0.68, (255, 0, 0), 3)
    cv2.imshow("img", img)
    cv2.waitKey(1)
