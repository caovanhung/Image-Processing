import cv2
import numpy as np

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("01.jpg")
    
    # Select ROI

    slicedImage = im[230:310, 240:430]
    
    # Crop image
    #imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    # Display cropped image
    cv2.imshow("Image", slicedImage)
    cv2.waitKey(0)
