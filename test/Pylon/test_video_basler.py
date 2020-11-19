"""
Interesting things 
 not end yet 
2020/4/2 16:28
"""
from pypylon import pylon
import numpy as np
import cv2 as cv
 
 # Connect the first camera in the Basler camera list
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
 
 # Start reading image
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
converter = pylon.ImageFormatConverter()
 
 # Convert to OpenCV's BGR color format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
 
while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
 
    if grabResult.GrabSucceeded():
        # Convert to OpenCV image format
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv.namedWindow('title', cv.WINDOW_NORMAL)
        cv.imshow('title', img)
        k = cv.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
 
 # Turn off the camera
camera.StopGrabbing()
 # close the window
cv.destroyAllWindows()
 
 