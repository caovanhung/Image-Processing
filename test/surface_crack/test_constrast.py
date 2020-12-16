'''
import cv2
import numpy as np

img = cv2.imread('images.jpg')
original = img.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#全局直方图均衡化
def eaualHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)    #opencv的直方图均衡化要基于单通道灰度图像
    dst = cv.equalizeHist(gray)                #自动调整图像对比度，把图像变得更清晰
    cv.namedWindow("eaualHist_demo", cv.WINDOW_NORMAL)
    cv.imshow("eaualHist_demo", dst)
    return dst


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    clahe = cv.createCLAHE(5, (8,8))
    dst = clahe.apply(gray)
    cv.namedWindow("clahe_demo", cv.WINDOW_NORMAL)
    cv.imshow("clahe_demo", dst)
    cv.imwrite("03.bmp", dst)


src=cv.imread('01.bmp')

cv.imshow("origin", src)

clahe_demo(src)
dst = eaualHist_demo(src)
cv.imwrite("02.bmp", dst)

plt.hist(src.ravel(),256,[0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()