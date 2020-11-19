import cv2
import math
import numpy as np
class detection_edges_xuluanh:
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
    def get_img_color(self):
        return self.img_color
    def get_img_position(self):
        return self.position_X,self.position_Y
    def get_position(self):
        return len (self.list_point_chia)

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
       # print(self.kernel)
        if filter_list=="Averaging":
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
        if filter_list=="Gaussian Filtering":
            self.filter_img = cv2.GaussianBlur(self.img_cut,(self.kernel,self.kernel),0)
        if filter_list=="Median Filtering":
            self.filter_img =cv2.medianBlur(self.img_cut,self.kernel)
    def edges_img(self,lowlevel,highlevel):
        thresh, self.img_thred = cv2.threshold(self.filter_img ,180, maxval=255, type=cv2.THRESH_BINARY)
        self.edges_img=cv2.Canny(self.img_thred,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img
       # self.img[self.y0:self.y1,self.x0:self.x1]=self.img_thred
    def edges_count(self,img):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        #im2,contours, hierarchy = cv2.findContours(self.img_thred,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NON)
        contours, hierarchy = cv2.findContours(self.edges_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam=[]
        for cnt in contours:
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_1,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam.append(tam)
        print(self.point_tam)
       # print(self.point_tam[0])
             
        return img
    def find_direction_xuly(self,img):
        self.point_sp=[]
        self.direction=[]
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        w,h,l=img.shape
        Dem_1=0
        Dem_2=0
        if len(self.point_tam)!=0:
            for i in range(len(self.point_tam)):
                if (self.point_tam[i][0]<h*0.5):
                    Dem_1=Dem_1+1
                else :
                    Dem_2=Dem_2+1
        print("Dem_1",Dem_1)
        print("Dem_2",Dem_2)
            
        print(len(self.point_tam))
        if ((Dem_1==0 and Dem_2%2==0)or(Dem_1==0 and Dem_2==0)or (Dem_1%2==0 and Dem_2==0) or (Dem_1%2==0 and Dem_2%2==0)):
            print("da chay")
            if (len(self.point_tam)<2):
            #print ("dung huog")
                self.direction.append("S")
                self.direction.append("S")
            elif (len(self.point_tam)==2):
                w,h,l=img.shape
            
                for i in range(len(self.point_tam)-1):
                    for j in range (i+1,len(self.point_tam)):
                        if (math.sqrt((self.point_tam[i][0]-self.point_tam[j][0])*(self.point_tam[i][0]-self.point_tam[j][0])+(self.point_tam[i][1]-self.point_tam[j][1])*(self.point_tam[i][1]-self.point_tam[j][1])))<100:
                            self.point_sp.append([self.point_tam[i][0],self.point_tam[i][1],self.point_tam[j][0],self.point_tam[j][1]])




                if (0.5*(self.point_sp[0][0]+ self.point_sp[0][2])<0.5*h):
                   if abs(self.point_sp[0][1]-self.point_sp[0][3])<10:
                       Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                       My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.direction.append("N")
                       self.direction.append("S")
                   if abs(self.point_sp[0][0]-self.point_sp[0][2])<10:
                        w,h,l=img.shape
                    #print("h",h)
                        if ((self.point_sp[0][0]<0.25*h)or ((self.point_sp[0][0]<0.75*h)and(self.point_sp[0][0]>0.5*h))):
                           Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                           My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("W")
                           self.direction.append("S")
                        if ((self.point_sp[0][0]<h)and (self.point_sp[0][0]>0.75*h))or ((self.point_sp[0][0]<0.5*h)and(self.point_sp[0][0]>0.25*h)):
                           Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                           My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("E")
                           self.direction.append("S")
                if (0.5*(self.point_sp[0][0]+ self.point_sp[0][2])>0.5*h):
                   self.direction.append("S") 
                   if abs(self.point_sp[0][1]-self.point_sp[0][3])<10:
                       Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                       My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.direction.append("N")
                   if abs(self.point_sp[0][0]-self.point_sp[0][2])<10:
                        w,h,l=img.shape
                        print("h",h)
                        if ((self.point_sp[0][0]<0.25*h)or ((self.point_sp[0][0]<0.75*h)and(self.point_sp[0][0]>0.5*h))):
                           Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                           My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("W")
                        if ((self.point_sp[0][0]<h)and (self.point_sp[0][0]>0.75*h))or ((self.point_sp[0][0]<0.5*h)and(self.point_sp[0][0]>0.25*h)):
                           Mx=int(0.5*(self.point_sp[0][0]+self.point_sp[0][2]))
                           My=int (0.5*(self.point_sp[0][1]+self.point_sp[0][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("E")
                    
           
            else:
                for i in range(len(self.point_tam)-1):
                    for j in range (i+1,len(self.point_tam)):
                        if (math.sqrt((self.point_tam[i][0]-self.point_tam[j][0])*(self.point_tam[i][0]-self.point_tam[j][0])+(self.point_tam[i][1]-self.point_tam[j][1])*(self.point_tam[i][1]-self.point_tam[j][1])))<100:
                            self.point_sp.append([self.point_tam[i][0],self.point_tam[i][1],self.point_tam[j][0],self.point_tam[j][1]])
                print(self.point_sp)
                if (self.point_sp[0][0]>self.point_sp[1][0]):
                    trunggian=[]
                    trunggian=self.point_sp[0]
                    self.point_sp[0]=self.point_sp[1]
                    self.point_sp[1]=trunggian
            
        
                for i in range (len(self.point_sp)):
                    if abs(self.point_sp[i][1]-self.point_sp[i][3])<10:
                       Mx=int(0.5*(self.point_sp[i][0]+self.point_sp[i][2]))
                       My=int (0.5*(self.point_sp[i][1]+self.point_sp[i][3]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.direction.append("N")
                    if abs(self.point_sp[i][0]-self.point_sp[i][2])<10:
                        w,h,l=img.shape
                    #print("h",h)
                        if ((self.point_sp[i][0]<0.25*h)or ((self.point_sp[i][0]<0.75*h)and(self.point_sp[i][0]>0.5*h))):
                           Mx=int(0.5*(self.point_sp[i][0]+self.point_sp[i][2]))
                           My=int (0.5*(self.point_sp[i][1]+self.point_sp[i][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("W")
                        if ((self.point_sp[i][0]<h)and (self.point_sp[i][0]>0.75*h))or ((self.point_sp[i][0]<0.5*h)and(self.point_sp[i][0]>0.25*h)):
                           Mx=int(0.5*(self.point_sp[i][0]+self.point_sp[i][2]))
                           My=int (0.5*(self.point_sp[i][1]+self.point_sp[i][3]))
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                           self.direction.append("E")
                    
        else:
            self.direction.append("NNNN")
            self.direction.append("NNNN")

        return self.direction, img
                
                    
            
     

