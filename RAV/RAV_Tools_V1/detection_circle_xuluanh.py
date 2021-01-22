import cv2
import math
class detection_circle_xuluanh:
    img=0
    img_cut=0
    x0=0
    y0=0
    x1=0
    y1=0
    position_X=0
    position_Y=0
   # sapxep=[]
    def __init__(self,img_1,img_2,x0,y0,x1,y1):
        self.y0=y0
        self.y1=y1
        self.x0=x0
        self.x1=x1
       # img_11=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
       # img_21=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
        self.img_cut=img_1[y0:y1,x0:x1]
        self.img=img_2
        self.sapxep=[]
        self.sapxep.append([])
        self.sapxep.append([])
        #self.img_color=img_color
    def get_img(self):
        return self.img
    def get_img_cut(self):
        return self.img_cut

    def get_img_position(self):
        return self.position_X,self.position_Y

    def filter_img(self,filter_list,kernel):
       # cv2.cvtColor(self.img_2, cv2.COLOR_BGR2GRAY)
        #self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        #self.img_cut=cv2.cvtColor(self.img_cut,cv2.COLOR_BGR2GRAY)
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
    def edges_img(self,lowlevel,highlevel):
        self.edges_img=cv2.Canny(self.filter_img,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img




        
