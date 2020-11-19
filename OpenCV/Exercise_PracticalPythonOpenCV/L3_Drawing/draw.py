import numpy as nu
import cv2

canvas = nu.zeros((300, 300, 3), dtype = "uint8")
green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas,(300,0), (0,300),red,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (0,0), (200,300), green,1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

white = (255,255,255)
cv2.circle(canvas,(150,150),30,white,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)



