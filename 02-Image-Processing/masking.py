import cv2
import math
import matplotlib.pyplot as plt
# Load two images
img1 = cv2.imread("../DATA/dog_backpack.png")
img2 = cv2.imread('../DATA/watermark_no_copy.png')
img2 = cv2.resize(img2,(600,600))

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[1401-600:1401,934-600:934 ]
import numpy as np
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey',img2gray)
mask=img2gray
mask_inv = cv2.bitwise_not(img2gray)
print(mask_inv.shape)


fg=cv2.bitwise_or(img2,img2,mask=mask_inv)
cv2.imshow('fg',fg)
final=cv2.bitwise_or(roi,fg)
cv2.imshow('final',final)
img1[1401-600:1401-600+final.shape[0],934-600:934-600+final.shape[1]]
cv2.imshow('final1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()