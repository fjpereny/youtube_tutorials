
import mss
import pyautogui
import cv2 as cv
import numpy as np
import time


w, h = pyautogui.size()
print("Screen Resolution: " + "w: " + str(w) + " h:" + str(h))

img = None
monitor = {"top": 0, "left": 0, "width": w, "height": h}

t0 = time.time()
n_frames = 1
with mss.mss() as sct:
    while True:
        img = sct.grab(monitor=monitor)
        img = np.array(img)

        small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

        cv.imshow("Computer Vision", small)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

        elapsed_time = time.time() - t0
        fps = (n_frames / elapsed_time)
        print("FPS: " + str(fps))
        n_frames += 1


cv.destroyAllWindows()