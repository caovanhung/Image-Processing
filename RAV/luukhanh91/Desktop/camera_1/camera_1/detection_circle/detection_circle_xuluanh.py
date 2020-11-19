import cv2
import math
import numpy as np 
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
        if filter_list=="Averaging":
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
        if filter_list=="Gaussian Filtering":
            self.filter_img = cv2.GaussianBlur(self.img_cut,(self.kernel,self.kernel),0)
        if filter_list=="Median Filtering":
            self.filter_img =cv2.medianBlur(self.img_cut,self.kernel)
    def edges_img(self,lowlevel,highlevel):
        self.edges_img=cv2.Canny(self.filter_img,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img
    def detect_circle_img(self,img_color):
      #  img_0=cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        detected_circles=cv2.HoughCircles(self.edges_img, cv2.HOUGH_GRADIENT, 1, 300,param1=50, param2=0,minRadius=0,maxRadius=0)
        #print(circles)
        if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
            detected_circles = np.uint16(np.around(detected_circles)) 
  
            for pt in detected_circles[0, :]: 
                a, b, r = pt[0], pt[1], pt[2] 

                cv2.circle(img_color, (a+self.x0, b+self.y0), r, (0, 255, 0), 2)  
                cv2.circle(img_color, (a+self.x0, b+self.y0), 1, (0, 0, 255), 3)


        return img_color      
    def detect_counter(self,img_color,R_max,R_min):
        img_1=img_color[self.y0:self.y1,self.x0:self.x1]
        contours, hierarchy = cv2.findContours(self.edges_img,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contour_circle=[]
        coutour_circle=[]
        dem=0
        circle=[]
        
        for i in range (len(contours)):
            if len(contours[i])>R_min*2*3.14 and len(contours[i])<R_max*2*3.14 :
               toado_x=[]
               toado_y=[]
               dem=dem+1
               trunggian=contours[i]
               for i in range(len (trunggian)):
                   toado_x.append(trunggian[i][0][0])
                   toado_y.append(trunggian[i][0][1])
                    
               max_x=max(toado_x)
               min_x=min(toado_x)
               max_y=max(toado_y)
               min_y=min(toado_y)
               r=int((max_x-min_x)*0.5)
               tam_x=int(0.5*(max_x+min_x))+self.x0
               tam_y=int(0.5*(max_y+min_y))+self.y0
               circle.append([tam_x,tam_y,r])
            else :
                tam_x=0
                tam_y=0
                dem=0
                r=0
        self.cleanlist = []
        [self.cleanlist.append(x) for x in circle if x not in self.cleanlist]
      #  print(len(self.cleanlist))
        for i in range(len (self.cleanlist)):
            cv2.circle(img_color, (self.cleanlist[i][0], self.cleanlist[i][1]),self.cleanlist[i][2], (0, 255, 0), 2)           
        return self.cleanlist,len(self.cleanlist),img_color        

    def position_circle(self,img_color,number_circle):
        cv2.circle(img_color, (self.cleanlist[number_circle][0], self.cleanlist[number_circle][1]),self.cleanlist[number_circle][2], (0, 255, 0), 2)
        return self.cleanlist[number_circle][0],self.cleanlist[number_circle][1],len(self.cleanlist),self.cleanlist[number_circle][2],img_color
        #img_1=img_color[self.y0:self.y1,self.x0:self.x1]

                


        
