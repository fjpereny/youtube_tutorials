

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open video capture")


while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)

    class_names = [
        'apple',
        'banana',
        'tomato',
        'orange',
    ]

    # choice, score = img_predicut(model, class_names, frame)
    choice = class_names[0]
    score = 0.984

    cv2.putText(
        frame,
        choice,
        (35, 35),
        cv2.FONT_HERSHEY_DUPLEX,
        0.8,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )

    cv2.putText(
        frame,
        str(f"{score * 100:.2f}%"),
        (35, 70),
        cv2.FONT_HERSHEY_DUPLEX,
        0.8,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )

    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(10)
    if key == 27: # Esc key break
        break

cap.release()
cv2.destroyAllWindows()
    