import os
import cv2

# Read image
image_path = os.path.join('.', 'imgs','happy.jpg')
img = cv2.imread(image_path)

img = cv2.resize(img,(747,498))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,8)
ret, simple_thresh = cv2.threshold(gray_img,110,255,cv2.THRESH_BINARY)
# Visualize image
cv2.imshow('Adaptive Threshold Image',adaptive_thresh)
cv2.imshow('Simple Threshold Image',simple_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()