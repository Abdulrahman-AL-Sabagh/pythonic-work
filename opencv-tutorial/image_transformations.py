# scaling
import numpy as np
import cv2 as cv
import matplotlib as plt
img = cv.imread('./mountain-2-scaled.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, 'file could not be read, check with os.path.exists()'


res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# OR

height, width = img.shape[:2]
res2 = cv.resize(img, (2*width, 2*height),  interpolation=cv.INTER_CUBIC)

rows, cols = img.shape
M = np.array([
    [1.0, 0, 0],
    [0, 1, 200]
]
)
# dst = cv.warpAffine(img, M, (cols, rows))

R = cv.getRotationMatrix2D(
    ((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
dst = cv.warpAffine(img, R, (cols, rows))

# Affine Transformation

aImg = cv.imread('./affine.jpg')

assert img is not None, 'file could not be read, check with os.path.exists()'

aColls, aRows, ch = img.shape

cv.imshow('img', dst)
cv.waitKey(0)


cv.destroyAllWindows()
