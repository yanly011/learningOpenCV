import cv2

img = cv2.imread('test.png',cv2.IMREAD_COLOR)
(height,width,deep) = img.shape
print(height, width, deep) #(512, 512, 3)

#将[200, 300]到[300,400]内的区域马赛克化
block_size = 10

(b, g, r)=img[200, 400]
for i in range (200, 500):
    for j in range(300, 400):
        if(i%20!=0 or j%20!=0):
            img[i, j] = img[int(i/20) * 20, int(j/20) * 20]


#显示结果：
cv2.imshow('img',img)
cv2.waitKey(0)


