import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
class Detect_QR_code_xulyanh:
    thred=0 
    img_t=0
    img_s=0
    img_cut=0;
    x0=0
    x1=0
    y1=0
    y2=0
   # img_thred=0
   # img_c=0
    def __init__(self,img_1,img_2,x0,y0,x1,y1):
        #self.img_t=img_t
  
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.img_cut=img_1[y0:y1,x0:x1]
        self.img=img_2
    def dection_QR_code_filter(self,filter_list,kernel):
        if kernel=="3X3":
            self.kernel=3
        if kernel=="5X5":
            self.kernel=5
        if kernel=="7X7":
            self.kernel=7
        if kernel=="9X9":
            self.kernel=9
        if kernel=="11X11":
            self.kernel=11
       # print(self.kernel)
        if filter_list=="Averaging":
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
        if filter_list=="Gaussian Filtering":
            self.filter_img = cv2.GaussianBlur(self.img_cut,(self.kernel,self.kernel),0)
        if filter_list=="Median Filtering":
            self.filter_img =cv2.medianBlur(self.img_cut,self.kernel)
        

    def Detect_QR_Code(self):
        font = cv2.FONT_HERSHEY_PLAIN
        decodedObjects = pyzbar.decode( self.filter_img )
        self.str_QR=""
        for obj in decodedObjects:

            
            if len(str(obj.data))!=0:
                for i in range(2,len(str(obj.data))-1):
                    self.str_QR=self.str_QR+str(obj.data)[i]
                x, y, w, h = obj.rect
                cv2.rectangle( self.filter_img , (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText( self.filter_img ,self.str_QR, (10, 10), font, 1,(255, 0, 0),1)
            self.img[self.y0:self.y1,self.x0:self.x1]=self.filter_img
       # print( self.str_QR)
        if len(self.str_QR)==0:
                self.str_QR="Khong phat hien"
                
        return  self.str_QR,self.img
