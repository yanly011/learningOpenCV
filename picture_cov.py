import numpy as np
import cv2

img = cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
cv2.waitKey(0)
(height,width) = img.shape
img_new = np.zeros([img.shape[0]-2,img.shape[1]-2])

print(img_new,np.shape(img),np.shape(img_new))
'''
(array([[0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]]), (512, 512), (510, 510))
'''

laplacien = np.array([-1,-1,-1, -1,8,-1, -1,-1,-1])

for i in range(1, img_new.shape[0]-1):
    for j in range(1, img_new.shape[1]-1):
        original_block = np.array([img[i-1, j-1], img[i-1, j], img[i-1, j+1],img[i, j-1], img[i, j], img[i, j+1],img[i+1, j-1], img[i+1, j], img[i+1, j+1]])
        img_new[i, j] = np.dot(original_block, laplacien)

#显示结果：
cv2.imshow('img_new',img_new)
cv2.waitKey(0)
