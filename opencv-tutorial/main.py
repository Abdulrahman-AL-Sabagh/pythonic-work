
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("mountain-2-scaled.jpg"))

if img is None:
    sys.exit("Could'nt raed the image")
cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("mountain-2-scaled.jpg", img)
