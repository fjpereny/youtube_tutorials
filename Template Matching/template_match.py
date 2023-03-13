

import cv2


original = cv2.imread('mario_ss.png')

block_1 = cv2.imread('block1.png')
block_2 = cv2.imread('block2.png')
block_3 = cv2.imread('block3.png')
goomba = cv2.imread('goomba.png')

block_1_match = cv2.matchTemplate(original, goomba, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(block_1_match)



rect_w = len(block_1)
rect_h = len(block_1[0])
p1 = max_loc    
p2 = (max_loc[0] + rect_w, max_loc[1] + rect_h)
display = cv2.rectangle(original, p1, p2, (255, 0, 255), 3, cv2.LINE_AA)
p1 = (p1[0], p1[1] - 5)
display = cv2.putText(display, "Goomba", p1, cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('Original', display)
cv2.waitKey(0)

cv2.destroyAllWindows()