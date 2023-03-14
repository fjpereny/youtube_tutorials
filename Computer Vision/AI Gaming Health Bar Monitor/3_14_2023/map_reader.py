

import pytesseract
import numpy as np
import cv2


def get_cur_zone(img):
    
    top_left = (1700, 5)
    bottom_right = (1850, 19)

    zone_name_img = img[
        top_left[1]:bottom_right[1],
        top_left[0]:bottom_right[0]
    ]

    zone_name_img = cv2.cvtColor(zone_name_img, cv2.COLOR_BGR2GRAY)
    zone_name_img = cv2.threshold(zone_name_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    zone = pytesseract.image_to_string(zone_name_img)

    return zone