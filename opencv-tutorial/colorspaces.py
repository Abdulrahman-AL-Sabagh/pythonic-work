# About converting spaces. From RGB to Gray Scales or to HSV or whatever
# Required Functions: cv.cvtColor(), cv.inRange()

# There are some contsant to use like cv.COLOR_BGR2GRAY cv.COLOR_bGR2HSV


import cv2 as cv
import numpy as np
flags = [i for i in dir(cv) if i.startswith('COLOR_')]

# the commented command below will print all existing flags in OpenCV
# print(flags)


# That being said... Object Detection should be easier (According to the online tutorial)


# So if I understand this code correctly it should
#  1. Convert the image to HSV
#  2. Copy every blue pixel in a new image
#  3. bitwise-and every pixel in both images. only the blue pixel should remain. Everything else will be black

# Take each frame
frame = cv.imread('./mountain-2-scaled.jpg')

# Convert BGR to HSV
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(frame, frame, mask=mask)

cv.imshow('frame', frame)
cv.imshow('mask', mask)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
