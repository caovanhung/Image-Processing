import cv2
import numpy as np
import pytesseract
class Detect_OCR_xulyanh:
    thred=0 
    img_t=0
    img_s=0
    img_cat=0;
    x0=0
    x1=0
    y1=0
    y2=0
    img_thred=0
    img_c=0
    def __init__(self,img_t,img_s,img_c,x0,y0,x1,y1):
        self.img_t=img_t
        #img_s=cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)
        self.img_s=img_s[y0:y1,x0:x1]
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.img_c=img_c
        self.img_kequa=img_c[y0:y1,x0:x1]
    def Threshold_getdata(self):
        return self.img_c
    def Threshold_setdata(self,img):
        self.img_s=img_t
    def Threshold_set_thred(self,thread):
        self.thred=thread
    def Threshold_xuly(self,thred):

        thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY)
        self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
    def Detect_OCR(self):
        custom_config = r'--oem 3 --psm 6'
        text=pytesseract.image_to_string(self.img_thred, config=custom_config)
        h, w = self.img_thred.shape
        boxes = pytesseract.image_to_boxes(self.img_thred)
        for b in boxes.splitlines():
            b = b.split(' ')
            self.img_kequa = cv2.rectangle(self.img_kequa, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
            self.img_c[self.y0:self.y1,self.x0:self.x1]=self.img_kequa
        return text    
