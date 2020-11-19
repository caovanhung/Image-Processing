import cv2
import numpy as np
import matplotlib.pyplot as plt
img_color=cv2.imread("03.jpg",1)
img_0=cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_0 = cv2.blur(img_0, (3, 3))
edges_img=cv2.Canny(img_0,120,255)
detected_circles=cv2.HoughCircles(edges_img, cv2.HOUGH_GRADIENT, 1, 50,param1=50, param2=30,minRadius=0,maxRadius=250)

        #print(circles)
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
   detected_circles = np.uint16(np.around(detected_circles)) 
  
   for pt in detected_circles[0, :]: 
       a, b, r = pt[0], pt[1], pt[2] 

       cv2.circle(img_color, (a, b), r, (0, 255, 0), 2)  
       cv2.circle(img_color, (a, b), 1, (0, 0, 255), 3)
cv2.imshow("anh",img_color)
cv2.imshow("anh_edg",edges_img)
cv2.waitKey()
