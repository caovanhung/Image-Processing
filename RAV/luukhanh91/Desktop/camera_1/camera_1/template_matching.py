import cv2
import numpy as np
import cv2 as cv
def template_matching(img1,img2):
        img3 = img2.copy()
        img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
       # img_1 = cv2.imread('01.jpg',1)
        #img2 = img_2.copy()
        template  = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
       # cv2.imshow("a",template)
        w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

      #  for meth in methods:
        #img = img2.copy()
        #method = eval(meth)

    # Apply template Matching
        res = cv2.matchTemplate(img,template,0)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print(top_left)

        cv2.rectangle(img3,top_left, bottom_right, (0,255,0), 2)
        return top_left, bottom_right,img3
