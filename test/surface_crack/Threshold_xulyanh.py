import cv2
class Class_Threshold:
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
    '''
    THRESH_BINARY       : neu gia tri pixel lon hon nguong "thred" thi gan bang "maxval"
                        nguoc lai gan bang 0
    THRESH_BINARY_INV   : neu gia tri pixel lon hon nguong "thred" thi gan bang 0
                        nguoc lai gan bang maxval
    THRESH_TRUNC        : neu gia tri pixel lon hon nguong "thred" thi gan bang "thred"
                        nguoc lai thi giu nguyen
    THRESH_TOZERO       : neu gia tri pixel lon hon nguong "thred" thi giu nguyen gia tri
                        nguoc lai gan bang 0
    THRESH_TOZERO_INV   : neu gia tri pixel lon hon nguong "thred" thi gan bang 0
                        nguoc lai giu nguyen
    '''
    def SimpleThresholding(self,thred,check):
        if check==1:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        elif check==2:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY_INV)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        elif check==3:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_TRUNC)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        elif check==4:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_TOZERO)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        elif check==5:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_TOZERO_INV)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred

    '''
    ADAPTIVE_THRESH_MEAN_C: giá trị của pixel phụ thuộc vào các pixel lân cận
    ADAPTIVE_THRESH_GAUSSIAN_C: giá trị của pixel cũng phụ thuộc vào các pixel lân cận, tuy nhiên được khử nhiễu
    Block Size: số pixel lân cận dùng để tính toán ( thường là số lẻ)
    C: hằng số trừ đi giá trị trung bình (số nguyên bất kỳ)
    '''
    def AdaptiveThresholding(self, blockSize, C, check):
        if check==1:
            thresh, self.img_thred = cv2.threshold(self.img_s,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        elif check==2:
            thresh, self.img_thred = cv2.threshold(self.img_s,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize, C)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
    def OtsuThresholding(self):
        blur = cv2.GaussianBlur(self.img_s,(5,5),0)
        thresh, self.img_thred = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred





