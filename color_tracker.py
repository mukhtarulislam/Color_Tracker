# color Trackbar MINI Project

import cv2
import numpy as np

# function for passs the Trackbar
def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
# 300x512 is the dimention of window
# 3 is the label
cv2.namedWindow('image')
# we declare the image Name by this method
cv2.createTrackbar('R','image',0,255,nothing)
# by this method we are create trackbar in this we are provide Name of trackbar
# is R, on the Image Window , color range is 0,255,nothing function call for no change value
cv2.createTrackbar('G','image',0,255,nothing)
# similar for Greeen color
cv2.createTrackbar('B','image',0,255,nothing)
# for Blue color
switch = '0: OFF \n 1: ON'
# switch is the method of trackbar i.e work on 0 off and on the 1 is on
cv2.createTrackbar(switch,'image',0,1,nothing)
# this trckbar for the switch mathod which we are create above
while(True):
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == 13:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
# this while looop are work perform untill the situation
    if s == 0:
        img[:]= 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()