# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# load the image
image = cv2.imread('image.png')

# find all the 'black' shapes in the image
lower = np.array([180, 50, 200])
upper = np.array([200, 70, 255])

shapeMask = cv2.inRange(image, lower, upper)

# find the contours in the mask
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("I found {} black shapes".format(len(cnts)))
cv2.imshow("Mask", shapeMask)

# loop over the contours
for c in cnts:
	# draw the contour and show it
	#"-1" draw all contours
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()