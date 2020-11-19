import cv2
class Threshold_xulyanh:
    thred=0 
    img_t=0
    img_s=0
    img_cat=0;
    x0=0
    x1=0
    y1=0
    y2=0
    img_thred=0
    def __init__(self,img_t,img_s,x0,y0,x1,y1):
        self.img_t=img_t
        self.img_s=img_s[y0:y1,x0:x1]
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
    def Threshold_getdata(self):
        return self.img_s
    def Threshold_setdata(self,img):
        self.img_s=img_t
    def Threshold_set_thred(self,thread):
        self.thred=thread
    def Threshold_xuly(self,thred,check):
        if check==1:
        #cv.THRESH_BINARY_INV
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY_INV)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        if check==2:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred            
    def Threshold_count_den(self):
        dem=0
        w_i,h=self.img_thred.shape
        for i in range(w_i):
            for j in range(h):
                if self.img_thred[i][j]==0:
                   dem=dem+1
        return dem
