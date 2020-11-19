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
        self.edges_img=cv2.Canny(self.filter_img,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img
    def edges_count(self,img):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        contours, hierarchy = cv2.findContours(self.edges_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        for cnt in contours:
             box = cv2.minAreaRect(cnt)
            # print (box)
        return img
    def display_test(self,img_color_1):
        height,width=self.edges_img.shape
        img_color_1=cv2.rectangle(img_color_1,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
       # print(self.edges_img.shape)
        self.list_point=[]
      #  print(self.edges_img)
        for i in range(width):
            for j in range(height):
           #     print(self.edges_img[i][j])
                if self.edges_img[j][i]==255:
                   self.list_point.append([j+self.y0,i+self.x0])
       # print(self.list_point)
        dem_test=0
        return  img_color_1 
        

    def paint_line(self,img_color_1):
   #     print(self.list_point)
        height,width=self.edges_img.shape
        img_color_1=cv2.rectangle(img_color_1,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
       # print(self.edges_img.shape)
        self.list_point=[]
      #  print(self.edges_img)
        for i in range(height):
            for j in range(width):
           #     print(self.edges_img[i][j])
               if self.edges_img[i][j]==255:
                   self.list_point.append([i+self.y0,j+self.x0])
        dem_test=0
        print("test_point",self.list_point)
        for x in range (len(self.list_point)-1):
         #   cv2.line(img_color_1,(self.list_point[x][1],self.list_point[x][0]),(self.list_point[x+1][1],self.list_point[x+1][0]),(0,255,0),1)
            if abs(self.list_point[0][0]-self.list_point[i][0])<3:
                dem_test=dem_test+1
        if dem_test>5:
      #  img_color_1=cv2.rectangle(img_color_1,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
       # print(self.edges_img.shape)
            self.list_point=[]
      #  print(self.edges_img)
            for i in range(width):
                for j in range(height):
          
                    if self.edges_img[j][i]==255:
                       self.list_point.append([j+self.y0,i+self.x0])
        self.sapxep=[]
        self.sapxep.append([])
        self.sapxep.append([])
        dem=0
        self.vitri=[]
        while(len(self.list_point) != 0):
 
            #print ("do dai truoc",len(self.list_point))            
            self.dc_1=self.list_point[0]
            self.list_xoa=[]
            vitri_cacline=0
            for i in range (len(self.list_point)):                
                if abs( math.sqrt ((self.list_point[i][0]-self.dc_1[0])*(self.list_point[i][0]-self.dc_1[0])+(self.list_point[i][1]-self.dc_1[1])*(self.list_point[i][1]-self.dc_1[1])))<10:
                    self.sapxep[dem].append(self.list_point[i])
                    self.dc_1=self.list_point[i] 
                    self.list_xoa.append(i)
                    vitri_cacline=vitri_cacline+1
            self.vitri.append(vitri_cacline)
            dem=dem+1
            for j in range (len (self.list_xoa)):
                del self.list_point[int(self.list_xoa[j])-j]

        for i in range(len(self.sapxep)):
            for j in range (len (self.sapxep[i])):
                img_color_1=cv2.circle(img_color_1,(self.sapxep[i][len(self.sapxep)-1][1],self.sapxep[i][len(self.sapxep)-1][0]),3,(0,0,255),2)
                img_color_1=cv2.line(img_color_1,(self.sapxep[i][j][1],self.sapxep[i][j][0]),(self.sapxep[i][j][1],self.sapxep[i][j][0]),(0,255,0),1)
        return dem,img_color_1
   
    def position_direction(self,shift,position,coordinate,direction,direction_scan,point,img_color_1):
        #img_color_1=self.paint_line(img_color_1)
        img_color_1=cv2.rectangle(img_color_1,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        if (coordinate== "Both"):
            if(direction_scan =="high->low" or direction_scan=="low->high"):
                self.list_point_chia=[]
                self.dc=math.sqrt(self.sapxep[position][0][1]*self.sapxep[position][0][1]+self.sapxep[position][0][0]*self.sapxep[position][0][0])
                self.list_point_chia.append([self.sapxep[position][0][0],self.sapxep[position][0][1]])
                for x in range (1,len(self.sapxep[position])-1):
                    if abs(math.sqrt(self.sapxep[position][x][1]*self.sapxep[position][x][1]+self.sapxep[position][x][0]*self.sapxep[position][x][0])-self.dc)>shift :
                        self.list_point_chia.append([self.sapxep[position][x][0],self.sapxep[position][x][1]])
                        self.dc=math.sqrt(self.sapxep[position][x][1]*self.sapxep[position][x][1]+self.sapxep[position][x][0]*self.sapxep[position][x][0])
                for x in range (len(self.list_point_chia)-1):
                   if (x==point):
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(0,0,255),2)
                   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(255,0,0),1)


                   img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),(self.list_point_chia[x+1][1],self.list_point_chia[x+1][0]),(0,255,0),2)

                img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][1],self.list_point_chia[len(self.list_point_chia)-1][0]),3,(255,0,0),1)
                        
                
            

        if (coordinate== "OX"):
           
            if(direction_scan =="high->low"):
                self.list_point_chia=[]
                self.dc=self.sapxep[position][0][1]
                self.list_point_chia.append([self.sapxep[position][0][0],self.sapxep[position][0][1]]) 
                for x in range (1,len(self.sapxep[position])-1):
                    if abs(int(self.sapxep[position][x][1])-self.dc)>shift :
                        self.list_point_chia.append([self.sapxep[position][x][0],self.sapxep[position][x][1]])
                        self.dc=self.sapxep[position][x][1]
                for x in range (len(self.list_point_chia)-1):
                   if (x==point):
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(0,0,255),2)
                   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(255,0,0),1)


                   img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),(self.list_point_chia[x+1][1],self.list_point_chia[x+1][0]),(0,255,0),2)

                img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][1],self.list_point_chia[len(self.list_point_chia)-1][0]),3,(255,0,0),1)
            
            if direction_scan=="low->high":
                self.list_point_chia=[]
                vitri_cuoi=len(self.sapxep[position])
                self.dc=self.sapxep[position][vitri_cuoi-1][1]
                self.list_point_chia.append([self.sapxep[position][vitri_cuoi-1][0],self.sapxep[position][vitri_cuoi-1][1]]) 
                for x in range (1,len(self.sapxep[position])-1):
                    if abs(int(self.sapxep[position][vitri_cuoi-x][1])-self.dc)>shift :
                        self.list_point_chia.append([self.sapxep[position][vitri_cuoi-x][0],self.sapxep[position][vitri_cuoi-x][1]])
                        self.dc=self.sapxep[position][vitri_cuoi-x][1]

                for x in range (len(self.list_point_chia)-1):
                   if (x==point):
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(0,0,255),2)
                   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(255,0,0),1)
                   img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),(self.list_point_chia[x+1][1],self.list_point_chia[x+1][0]),(0,255,0),2)

                img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][1],self.list_point_chia[len(self.list_point_chia)-1][0]),3,(255,0,0),1)
        if  coordinate=="OY":
            if(direction_scan =="high->low"):
                self.list_point_chia=[]
                self.dc=self.sapxep[position][0][0]
                self.list_point_chia.append([self.sapxep[position][0][0],self.sapxep[position][0][1]]) 
                for x in range (1,len(self.sapxep[position])-1):
                    if abs(int(self.sapxep[position][x][0])-self.dc)>shift :
                        self.list_point_chia.append([self.sapxep[position][x][0],self.sapxep[position][x][1]])
                        self.dc=self.sapxep[position][x][0]

                for x in range (len(self.list_point_chia)-1):
                   if (x==point):
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(0,0,255),2)
                   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(255,0,0),1)
                   img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),(self.list_point_chia[x+1][1],self.list_point_chia[x+1][0]),(0,255,0),2)
            img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][1],self.list_point_chia[len(self.list_point_chia)-1][0]),3,(255,0,0),1)

            if direction_scan=="low->high":
                self.list_point_chia=[]
                vitri_cuoi=len(self.sapxep[position])
             #   print ("vi tri cuoi ",len(self.sapxep[position]))
                self.dc=self.sapxep[position][vitri_cuoi-1][0]
                self.list_point_chia.append([self.sapxep[position][vitri_cuoi-1][0],self.sapxep[position][vitri_cuoi-1][1]]) 
                for x in range (1,len(self.sapxep[position])-1):
                    if abs(int(self.sapxep[position][vitri_cuoi-x][0])-self.dc)>shift :
                        self.list_point_chia.append([self.sapxep[position][vitri_cuoi-x][0],self.sapxep[position][vitri_cuoi-x][1]])
                        self.dc=self.sapxep[position][vitri_cuoi-x][0]

                for x in range (len(self.list_point_chia)-1):
                   if (x==point):
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(0,0,255),2)
                   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),3,(255,0,0),1)
                   img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][1],self.list_point_chia[x][0]),(self.list_point_chia[x+1][1],self.list_point_chia[x+1][0]),(0,255,0),2)
                img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][1],self.list_point_chia[len(self.list_point_chia)-1][0]),3,(255,0,0),1)
        return img_color_1
    def display_point(self,shift,position,coordinate,direction_trend,direction_scan,point,img_color_1):
        
        self.img_color_2=self.position_direction(shift,position,coordinate,direction_trend,direction_scan,point,img_color_1)

        if (coordinate== "OX"):
            self.line_A=[]
            self.line_B=[]
            self.line_M=[]
            self.line_A.append([self.list_point_chia[point][1],self.list_point_chia[point][0]])
            if (direction_scan=="low->high"):
                self.line_B.append([self.list_point_chia[point][1],self.y0])
                self.line_M.append([int(0.5*(self.line_A[0][0]+self.line_B[0][0])),int(0.5*(self.line_A[0][1]+self.line_B[0][1]))])
                self.position_point=abs(self.list_point_chia[point][0]-self.y0)
            if (direction_scan=="high->low"):
                self.line_B.append([self.list_point_chia[point][1],self.y1])
                
                self.line_M.append([int(0.5*(self.line_A[0][0]+self.line_B[0][0])),int(0.5*(self.line_A[0][1]+self.line_B[0][1]))])
                self.position_point=abs(self.list_point_chia[point][0]-self.y1)
            self.position_X=self.position_point
            self.position_Y=0
       
        if (coordinate== "OY"):
           self.line_A=[]
           self.line_B=[]
           self.line_M=[]
           self.line_A.append([self.list_point_chia[point][1],self.list_point_chia[point][0]])
           if (direction_trend=="->"):

                self.line_B.append([self.x0,self.list_point_chia[point][0]])
                self.position_point=abs(self.list_point_chia[point][1]-self.x0)
                self.line_M.append([int(0.5*(self.line_A[0][0]+self.line_B[0][0])),int(0.5*(self.line_A[0][1]+self.line_B[0][1]))])
           if (direction_trend=="<-"):
                self.line_B.append([self.x1,self.list_point_chia[point][0]])
                self.position_point=abs(self.list_point_chia[point][1]-self.x1)
                self.line_M.append([int(0.5*(self.line_A[0][0]+self.line_B[0][0])),int(0.5*(self.line_A[0][1]+self.line_B[0][1]))])
           self.position_Y=self.position_point
           self.position_X=0
        if (coordinate== "OX" or coordinate== "OY"):
            self.img_color_2=cv2.line(self.img_color_2,(self.line_A[0][0], self.line_A[0][1]),(self.line_B[0][0], self.line_B[0][1]),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.img_color_2, str(self.position_point), (self.line_M[0][0], self.line_M[0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            
        if (coordinate== "Both"):
           self.line_A=[]
           self.line_B1=[]
           self.line_M1=[]
           self.line_B2=[]
           self.line_M2=[]
           self.img_color_2=self.position_direction(shift,position,coordinate,direction_trend,direction_scan,point,img_color_1)
           self.line_A.append([self.list_point_chia[point][1],self.list_point_chia[point][0]])
           if (direction_scan=="low->high"):
                self.line_B1.append([self.list_point_chia[point][1],self.y0])
                self.line_M1.append([int(0.5*(self.line_A[0][0]+self.line_B1[0][0])),int(0.5*(self.line_A[0][1]+self.line_B1[0][1]))])
                self.position_point=abs(self.list_point_chia[point][0]-self.y0)
           if (direction_scan=="high->low"):
                self.line_B1.append([self.list_point_chia[point][1],self.y1])
                
                self.line_M1.append([int(0.5*(self.line_A[0][0]+self.line_B1[0][0])),int(0.5*(self.line_A[0][1]+self.line_B1[0][1]))])
                self.position_point=abs(self.list_point_chia[point][0]-self.y1)
           if (direction_trend=="->"):

                self.line_B2.append([self.x0,self.list_point_chia[point][0]])
                self.position_point_1=abs(self.list_point_chia[point][1]-self.x0)
                self.line_M2.append([int(0.5*(self.line_A[0][0]+self.line_B2[0][0])),int(0.5*(self.line_A[0][1]+self.line_B2[0][1]))])
           if (direction_trend=="<-"):
                self.line_B2.append([self.x1,self.list_point_chia[point][0]])
                self.position_point_1=abs(self.list_point_chia[point][1]-self.x1)
                self.line_M2.append([int(0.5*(self.line_A[0][0]+self.line_B2[0][0])),int(0.5*(self.line_A[0][1]+self.line_B2[0][1]))])
           self.position_X=self.position_point
           self.position_Y=self.position_point_1
           self.img_color_2=cv2.line(self.img_color_2,(self.line_A[0][0], self.line_A[0][1]),(self.line_B1[0][0], self.line_B1[0][1]),(0,255,0),2)  
           font = cv2.FONT_HERSHEY_SIMPLEX
           self.img_color_2=cv2.putText(self.img_color_2, str(self.position_point), (self.line_M1[0][0], self.line_M1[0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
           self.img_color_2=cv2.line(self.img_color_2,(self.line_A[0][0], self.line_A[0][1]),(self.line_B2[0][0], self.line_B2[0][1]),(0,255,0),2)  
           font = cv2.FONT_HERSHEY_SIMPLEX
           self.img_color_2=cv2.putText(self.img_color_2, str(self.position_point_1), (self.line_M2[0][0], self.line_M2[0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)        
        return self.img_color_2
    def display_line_xuly(self,img_color_1,position):
        img_color_1=cv2.rectangle(img_color_1,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        for x in range (len(self.sapxep[position-1])-1):
            img_color_1=cv2.line(img_color_1,(self.sapxep[position-1][x][1],self.sapxep[position-1][x][0]),(self.sapxep[position-1][x+1][1],self.sapxep[position-1][x+1][0]),(0,255,0),2)
        return img_color_1
     

