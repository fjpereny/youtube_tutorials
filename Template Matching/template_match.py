

import cv2


original = cv2.imread('./Template Matching/mario_ss.png')
small = cv2.resize(original, (0, 0), fx=0.5, fy=0.5)

block_1 = cv2.imread('./Template Matching/block1.png')
block_1_match = cv2.matchTemplate(original, block_1, cv2.TM_CCOEFF_NORMED)
block_1_match = cv2.resize(block_1_match, (0, 0), fx=0.5, fy=0.5)

block_2 = cv2.imread('./Template Matching/block2.png')
block_2_match = cv2.matchTemplate(original, block_2, cv2.TM_CCOEFF_NORMED)
block_2_match = cv2.resize(block_2_match, (0, 0), fx=0.5, fy=0.5)

block_3 = cv2.imread('./Template Matching/block3.png')
block_3_match = cv2.matchTemplate(original, block_3, cv2.TM_CCOEFF_NORMED)
block_3_match = cv2.resize(block_3_match, (0, 0), fx=0.5, fy=0.5)

goomba = cv2.imread('./Template Matching/goomba.png')
goomba_match = cv2.matchTemplate(original, goomba, cv2.TM_CCOEFF_NORMED)
goomba_match = cv2.resize(goomba_match, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Original', small)
cv2.waitKey(0)

cv2.imshow('Template', block_1)
cv2.imshow('Match', block_1_match)
cv2.waitKey(0)
cv2.destroyWindow('Template')
cv2.destroyWindow('Match')

cv2.imshow('Template', block_2)
cv2.imshow('Match', block_2_match)
cv2.waitKey(0)
cv2.destroyWindow('Template')
cv2.destroyWindow('Match')

cv2.imshow('Template', block_3)
cv2.imshow('Match', block_3_match)
cv2.waitKey(0)
cv2.destroyWindow('Template')
cv2.destroyWindow('Match')

cv2.imshow('Template', goomba)
cv2.imshow('Match', goomba_match)
cv2.waitKey(0)
cv2.destroyWindow('Template')
cv2.destroyWindow('Match')