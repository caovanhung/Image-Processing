import cv2
import math
import numpy as np
class Trend_Edge_width_xuluanh:
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
    def Trend_Edge_width_edges_img(self,lowlevel,highlevel):
        self.edges_img=cv2.Canny(self.filter_img,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img
    def edges_count(self,img,direction_trend,coordinate,direction_scan):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        self.contours, hierarchy = cv2.findContours(self.edges_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
      #  img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 1)
        position_scan_x=[]
        position_scan_y=[]
        self.position_line__cantim_x=[]
        self.position_line__cantim_y=[]
        
        for i in range(len(self.contours)):
            trunggian=self.contours[i]
            self.position_line__cantim_x.append(i)
            self.position_line__cantim_y.append(i)
            position_x_min=[]
            position_y_min=[]
            for j in range (len(trunggian)):
                position_x_min.append(trunggian[j][0][0])
                position_y_min.append(trunggian[j][0][1])#sflslfsdlfsd
            
            position_scan_x.append(min(position_x_min))
            position_scan_y.append(min(position_y_min))
        for i in range(len(self.contours)-1):
            for j in range (i+1,len(self.contours)):
                if (position_scan_x[i]>position_scan_x[j]):
                    trunggian_postion=position_scan_x[i]
                    position_scan_x[i]=position_scan_x[j]
                    position_scan_x[j]=trunggian_postion

                    trunggian_contours=self.position_line__cantim_x[i]
                    self.position_line__cantim_x[i]=self.position_line__cantim_x[j]
                    self.position_line__cantim_x[j]=trunggian_contours

                    trunggian_postion=position_scan_y[i]
                    position_scan_y[i]=position_scan_y[j]
                    position_scan_y[j]=trunggian_postion

                    trunggian_contours=self.position_line__cantim_y[i]
                    self.position_line__cantim_y[i]=self.position_line__cantim_y[j]
                    self.position_line__cantim_y[j]=trunggian_contours


        self.sapxep=[]
        if coordinate=="OX":
            for i in range(len(self.contours)):
                trunggian_x=self.contours[self.position_line__cantim_x[i]]
                list_point=[]
                for j in range (len(trunggian_x)):
                    list_point.append([trunggian_x[j][0][0],trunggian_x[j][0][1]])
                self.sapxep.append(list_point)
                font = cv2.FONT_HERSHEY_SIMPLEX
            if direction_trend=="->":
                for i in range (len(self.sapxep)):
                    for x in range(len(self.sapxep[i])-1): 
                        cv2.line(img_1,(self.sapxep[i][x][0],self.sapxep[i][x][1]),(self.sapxep[i][x+1][0],self.sapxep[i][x+1][1]),(0,255,0),1)
                    img_1=cv2.putText(img_1, str(i+1), (self.sapxep[i][0][0], self.sapxep[i][0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            if direction_trend=="<-":
                for i in range (len(self.sapxep)):
                    self.a=int(len(self.sapxep)-i-1)
                    for x in range(len(self.sapxep[self.a])-1):         
                        cv2.line(img_1,(self.sapxep[self.a][x][0],self.sapxep[self.a][x][1]),(self.sapxep[self.a][x+1][0],self.sapxep[self.a][x+1][1]),(0,255,0),1)
                    img_1=cv2.putText(img_1, str(i+1), (self.sapxep[self.a][0][0], self.sapxep[self.a][0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            sapxep_list_point_x=0
            sapxep_list_point_y=0         
         #   print("........",len(self.sapxep[0]))
            for i in range(len(self.sapxep)):
                #self.len_sapxep=len(self.sapxep[i])
                for x in range(len(self.sapxep[i])-1):
                    for y in range (x+1 ,len(self.sapxep[i])):
                           
                            if (self.sapxep[i][x][0]>self.sapxep[i][y][0]):
                                sapxep_list_point_x=self.sapxep[i][x][0]
                                sapxep_list_point_y=self.sapxep[i][x][1]

                                self.sapxep[i][x][0]=self.sapxep[i][y][0]
                                self.sapxep[i][x][1]=self.sapxep[i][y][1]

                                self.sapxep[i][y][0]=sapxep_list_point_x
                                self.sapxep[i][y][1]=sapxep_list_point_y    



        if coordinate=="OY":
            for i in range(len(self.contours)):
                trunggian_y=self.contours[self.position_line__cantim_y[i]]
                list_point=[]
                for j in range (len(trunggian_y)):
                    list_point.append([trunggian_y[j][0][0],trunggian_y[j][0][1]])
                self.sapxep.append(list_point)
                font = cv2.FONT_HERSHEY_SIMPLEX
            if direction_scan=="high->low":
                for i in range (len(self.sapxep)):
                    for x in range(len(self.sapxep[i])-1): 
                        cv2.line(img_1,(self.sapxep[i][x][0],self.sapxep[i][x][1]),(self.sapxep[i][x+1][0],self.sapxep[i][x+1][1]),(0,255,0),1)
                    img_1=cv2.putText(img_1, str(i+1), (self.sapxep[i][0][0], self.sapxep[i][0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            if direction_scan=="low->high":
                for i in range (len(self.sapxep)):
                    self.a=int(len(self.sapxep)-i-1)
                    for x in range(len(self.sapxep[self.a])-1):         
                        cv2.line(img_1,(self.sapxep[self.a][x][0],self.sapxep[self.a][x][1]),(self.sapxep[self.a][x+1][0],self.sapxep[self.a][x+1][1]),(0,255,0),1)
                    img_1=cv2.putText(img_1, str(i+1), (self.sapxep[self.a][0][0], self.sapxep[self.a][0][1]), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            sapxep_list_point_x=0
            sapxep_list_point_y=0         
                
            for i in range(len(self.sapxep)):
               # self.len_sapxep=len(self.sapxep[i])
                for x in range(len(self.sapxep[i])-1):
                    for y in range (x+1 ,len(self.sapxep[i])):
                           
                            if (self.sapxep[i][x][1]>self.sapxep[i][y][1]):
                                sapxep_list_point_x=self.sapxep[i][x][0]
                                sapxep_list_point_y=self.sapxep[i][x][1]

                                self.sapxep[i][x][0]=self.sapxep[i][y][0]
                                self.sapxep[i][x][1]=self.sapxep[i][y][1]

                                self.sapxep[i][y][0]=sapxep_list_point_x
                                self.sapxep[i][y][1]=sapxep_list_point_y    


        for cnt in self.contours:
             box = cv2.minAreaRect(cnt)
            # print (box)
        return img
    def divid_line_shift(self,shift,coordinate,direction,direction_scan,point,img_color):
      #  print(self.sapxep)
      #  position=0
        img_color_1=cv2.rectangle(img_color,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        img_color_1=img_color[self.y0:self.y1,self.x0:self.x1]
        if (coordinate== "OX"):
           
            if(direction =="->"):
            
                for i in range (len(self.sapxep)):
                    self.list_point_chia=[]
                    self.dc=self.sapxep[i][0][0]
                    self.list_point_chia.append([self.sapxep[i][0][0],self.sapxep[i][0][1]]) 
                    for x in range (1,len(self.sapxep[i])):
                        if abs(int(self.sapxep[i][x][0])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[i][x][0],self.sapxep[i][x][1]])
                            self.dc=self.sapxep[i][x][0]
                    for x in range (len(self.list_point_chia)-1):
                       if (x==point):
                           img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)


                       img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)

                    img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
            
            if direction=="<-":
                for i in range (len(self.sapxep)):
                    self.list_point_chia=[]
                    vitri_cuoi=len(self.sapxep[i])
                    self.dc=self.sapxep[i][vitri_cuoi-1][0]
                    self.list_point_chia.append([self.sapxep[i][vitri_cuoi-1][0],self.sapxep[i][vitri_cuoi-1][1]]) 
                    for x in range (1,len(self.sapxep[i])):
                        if abs(int(self.sapxep[i][vitri_cuoi-x][0])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[i][vitri_cuoi-x][0],self.sapxep[i][vitri_cuoi-x][1]])
                            self.dc=self.sapxep[i][vitri_cuoi-x][0]
                    for x in range (len(self.list_point_chia)-1):
                       if (x==point):
                           img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)
                       img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)
                    img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
        if  coordinate=="OY":
            if(direction_scan =="high->low"):
                for i in range (len(self.sapxep)):
                    self.list_point_chia=[]
                    self.dc=self.sapxep[i][0][1]
                    self.list_point_chia.append([self.sapxep[i][0][0],self.sapxep[i][0][1]]) 
                    for x in range (1,len(self.sapxep[i])):
                        if abs(int(self.sapxep[i][x][1])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[i][x][0],self.sapxep[i][x][1]])
                            self.dc=self.sapxep[i][x][1]

                    for x in range (len(self.list_point_chia)-1):
                       if (x==point):
                           img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)
                       img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)
                img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)

            if direction_scan=="low->high":
                for i in range (len(self.sapxep)):
                    self.list_point_chia=[]
                    vitri_cuoi=len(self.sapxep[i])
             #   print ("vi tri cuoi ",len(self.sapxep[position]))
                    self.dc=self.sapxep[i][vitri_cuoi-1][1]
                    self.list_point_chia.append([self.sapxep[i][vitri_cuoi-1][0],self.sapxep[i][vitri_cuoi-1][1]]) 
                    for x in range (1,len(self.sapxep[i])):
                        if abs(int(self.sapxep[i][vitri_cuoi-x][1])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[i][vitri_cuoi-x][0],self.sapxep[i][vitri_cuoi-x][1]])
                            self.dc=self.sapxep[i][vitri_cuoi-x][1]

                    for x in range (len(self.list_point_chia)-1):
                       if (x==point):
                           img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                       img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)
                       img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)
                    img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
        return len(self.sapxep),img_color     



    
    def divid_line(self,shift,posit,posit_1,coordinate,direction,direction_scan,point,img_color):
      #  print(self.sapxep)
        po=[]
        img_color_1=cv2.rectangle(img_color,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        img_color_1=img_color[self.y0:self.y1,self.x0:self.x1]
        po.append(posit)
        po.append(posit_1)
        self.list_point_divided=[]
        if (coordinate== "OX"):
           
            if(direction =="->"):     
                for i in range(2):
                    position=po[i]
                    self.list_point_chia=[]
                    self.dc=self.sapxep[i][0][0]
                    self.list_point_chia.append([self.sapxep[position][0][0],self.sapxep[position][0][1]]) 
                    for x in range (1,len(self.sapxep[position])):
                        if abs(int(self.sapxep[position][x][0])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[position][x][0],self.sapxep[position][x][1]])
                            self.dc=self.sapxep[position][x][0]
                  #  for x in range (len(self.list_point_chia)-1):
                    #   if (x==point):
                     #      img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                     #  img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)
                   #    img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)
                    self.list_point_divided.append(self.list_point_chia)
                   # img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
            
            if direction=="<-":
                for i in range(2):
                    position=po[i]
                    self.list_point_chia=[]
                    vitri_cuoi=len(self.sapxep[position])
                    self.dc=self.sapxep[position][vitri_cuoi-1][0]
                    self.list_point_chia.append([self.sapxep[position][vitri_cuoi-1][0],self.sapxep[position][vitri_cuoi-1][1]]) 
                    for x in range (1,len(self.sapxep[position])):
                        if abs(int(self.sapxep[position][vitri_cuoi-x][0])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[position][vitri_cuoi-x][0],self.sapxep[position][vitri_cuoi-x][1]])
                            self.dc=self.sapxep[position][vitri_cuoi-x][0]
  
                    self.list_point_divided.append(self.list_point_chia)


                    #img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
            len_1=len(self.list_point_divided[0])
            len_2=len(self.list_point_divided[1])

            trunggianlist_point_x=0
            trunggianlist_point_y=0

            for i in range (len_1-1):
                for j in range(i+1,len_1):
                    
                    if (self.list_point_divided[0][i][0]>self.list_point_divided[0][j][0]):
                        trunggianlist_point_x=self.list_point_divided[0][i][0]
                        trunggianlist_point_y=self.list_point_divided[0][i][1]

                        self.list_point_divided[0][i][0]=self.list_point_divided[0][j][0]
                        self.list_point_divided[0][i][1]=self.list_point_divided[0][j][1]

                        self.list_point_divided[0][j][0]=trunggianlist_point_x
                        self.list_point_divided[0][j][1]=trunggianlist_point_y
            for i in range (len_2-1):
                for j in range(i+1,len_2):
                    
                    if (self.list_point_divided[1][i][0]>self.list_point_divided[1][j][0]):
                        trunggianlist_point_x=self.list_point_divided[1][i][0]
                        trunggianlist_point_y=self.list_point_divided[1][i][1]

                        self.list_point_divided[1][i][0]=self.list_point_divided[1][j][0]
                        self.list_point_divided[1][i][1]=self.list_point_divided[1][j][1]

                        self.list_point_divided[1][j][0]=trunggianlist_point_x
                        self.list_point_divided[1][j][1]=trunggianlist_point_y                        
            #print (self.list_point_divided)
            for i in range (len_2-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),(self.list_point_divided[1][i+1][0],self.list_point_divided[1][i+1][1]),(0,255,0),2)
            for i in range (len_1-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),(self.list_point_divided[0][i+1][0],self.list_point_divided[0][i+1][1]),(0,255,0),2)          
            for i in range (2):
                cleanlist = []
                [cleanlist.append(x) for x in self.list_point_divided[i] if x not in cleanlist]
                self.list_point_divided[i]=cleanlist
        #    print("len_1",len_1)
       #     print(self.list_point_divided[0])
       #     print("len_2",len_2)
        #    print(self.list_point_divided[1])
            


        if  coordinate=="OY":
            if(direction_scan =="high->low"):
                for i in range(2):
                    position=po[i]

                    self.list_point_chia=[]
                    self.dc=self.sapxep[position][0][1]
                    self.list_point_chia.append([self.sapxep[position][0][0],self.sapxep[position][0][1]]) 
                    for x in range (1,len(self.sapxep[position])):
                        if abs(int(self.sapxep[position][x][1])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[position][x][0],self.sapxep[position][x][1]])
                            self.dc=self.sapxep[position][x][1]    
                    self.list_point_divided.append(self.list_point_chia)                              
            if direction_scan=="low->high":
                for i in range(2):
                    position=po[i]
                    self.list_point_chia=[]
                    vitri_cuoi=len(self.sapxep[position])
             #   print ("vi tri cuoi ",len(self.sapxep[position]))
                    self.dc=self.sapxep[position][vitri_cuoi-1][1]
                    self.list_point_chia.append([self.sapxep[position][vitri_cuoi-1][0],self.sapxep[position][vitri_cuoi-1][1]]) 
                    for x in range (1,len(self.sapxep[position])):
                        if abs(int(self.sapxep[position][vitri_cuoi-x][1])-self.dc)>shift :
                            self.list_point_chia.append([self.sapxep[position][vitri_cuoi-x][0],self.sapxep[position][vitri_cuoi-x][1]])
                            self.dc=self.sapxep[position][vitri_cuoi-x][1]

                    #for x in range (len(self.list_point_chia)-1):
                     #  if (x==point):
                      #     img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(0,0,255),2)
                   #    img_color_1=cv2.circle(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),3,(255,0,0),1)
                   #    img_color_1=cv2.line(img_color_1,(self.list_point_chia[x][0],self.list_point_chia[x][1]),(self.list_point_chia[x+1][0],self.list_point_chia[x+1][1]),(0,255,0),2)
                    self.list_point_divided.append(self.list_point_chia)
                 #   img_color_1=cv2.circle(img_color_1,(self.list_point_chia[len(self.list_point_chia)-1][0],self.list_point_chia[len(self.list_point_chia)-1][1]),3,(255,0,0),1)
            len_1=len(self.list_point_divided[0])
            len_2=len(self.list_point_divided[1])
            trunggianlist_point_x=0
            trunggianlist_point_y=0
            
            for i in range (len_1-1):
                for j in range(i+1,len_1):
                    
                    if (self.list_point_divided[0][i][1]>self.list_point_divided[0][j][1]):
                        trunggianlist_point_x=self.list_point_divided[0][i][0]
                        trunggianlist_point_y=self.list_point_divided[0][i][1]

                        self.list_point_divided[0][i][0]=self.list_point_divided[0][j][0]
                        self.list_point_divided[0][i][1]=self.list_point_divided[0][j][1]

                        self.list_point_divided[0][j][0]=trunggianlist_point_x
                        self.list_point_divided[0][j][1]=trunggianlist_point_y
            for i in range (len_2-1):
                for j in range(i+1,len_2):
                    
                    if (self.list_point_divided[1][i][1]>self.list_point_divided[1][j][1]):
                        trunggianlist_point_x=self.list_point_divided[1][i][0]
                        trunggianlist_point_y=self.list_point_divided[1][i][1]

                        self.list_point_divided[1][i][0]=self.list_point_divided[1][j][0]
                        self.list_point_divided[1][i][1]=self.list_point_divided[1][j][1]

                        self.list_point_divided[1][j][0]=trunggianlist_point_x
                        self.list_point_divided[1][j][1]=trunggianlist_point_y                        
            for i in range (len_2-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),(self.list_point_divided[1][i+1][0],self.list_point_divided[1][i+1][1]),(0,255,0),2)
            for i in range (len_1-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),(self.list_point_divided[0][i+1][0],self.list_point_divided[0][i+1][1]),(0,255,0),2)          
            #print("ket qua",self.list_point_divided)
            for i in range (2):
                cleanlist = []
                [cleanlist.append(x) for x in self.list_point_divided[i] if x not in cleanlist]
                self.list_point_divided[i]=cleanlist
        return img_color 
        
    def divid_point(self,shift,point_1,direction,coordinate,direction_scan,Jubged_comboBox,img_color):
        img_color_1=cv2.rectangle(img_color,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        img_color_1=img_color[self.y0:self.y1,self.x0:self.x1]
        
        len_1=len(self.list_point_divided[0])
        len_2=len(self.list_point_divided[1])
        self.point_1_2=[]


        for i in range (len_2-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),(self.list_point_divided[1][i+1][0],self.list_point_divided[1][i+1][1]),(0,255,0),2)
        for i in range (len_1-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),(self.list_point_divided[0][i+1][0],self.list_point_divided[0][i+1][1]),(0,255,0),2)   



        if coordinate=="OX":
            for i in range(len_1):
                j=0
                while j<len_2:
                     if abs(self.list_point_divided[0][i][0]-self.list_point_divided[1][j][0])<shift:
                         self.point_1_2.append([self.list_point_divided[0][i][0],self.list_point_divided[0][i][1],self.list_point_divided[1][j][0],self.list_point_divided[1][j][1]])
                         j=len_2
                     j=j+1
        if coordinate=="OY":
            for i in range(len_1):
                j=0
                while j<len_2:
                     if abs(self.list_point_divided[0][i][1]-self.list_point_divided[1][j][1])<shift:
                        # cv2.line(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),(self.list_point_divided[1][j][0],self.list_point_divided[1][j][1]),(0,255,0),2)       
                         self.point_1_2.append([self.list_point_divided[0][i][0],self.list_point_divided[0][i][1],self.list_point_divided[1][j][0],self.list_point_divided[1][j][1]])
                         j=len_2
                     j=j+1
        self.length_point_1_2=[]
        for i in range (len(self.point_1_2)):
                L=math.sqrt((self.point_1_2[i][0]-self.point_1_2[i][2])*(self.point_1_2[i][0]-self.point_1_2[i][2])+(self.point_1_2[i][1]-self.point_1_2[i][3])*(self.point_1_2[i][1]-self.point_1_2[i][3]))
                self.length_point_1_2.append(L)
      #  print(self.length_point_1_2)
        Max_L=max(self.length_point_1_2)
        Min_L=min(self.length_point_1_2)
        self.L=0
        if Jubged_comboBox=="Max": 
            for i in range (len (self.length_point_1_2)):
                if Max_L==self.length_point_1_2[i]:
                    M_x=int ((self.point_1_2[i][0]+self.point_1_2[i][2])*0.5)-5
                    M_y=int ((self.point_1_2[i][1]+self.point_1_2[i][3])*0.5)-5
                
                    cv2.line(img_color_1,(self.point_1_2[i][0],self.point_1_2[i][1]),(self.point_1_2[i][2],self.point_1_2[i][3]),(0,0,255),2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img_color_1, str(Max_L), (M_x,M_y), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    self.L=Max_L
                    break
        if Jubged_comboBox=="Min": 
            for j in range (len (self.length_point_1_2)):
                if Min_L==self.length_point_1_2[j]:
                    M_x=int ((self.point_1_2[j][0]+self.point_1_2[j][2])*0.5)+5
                    M_y=int ((self.point_1_2[j][1]+self.point_1_2[j][3])*0.5)+5
                
                    cv2.line(img_color_1,(self.point_1_2[j][0],self.point_1_2[j][1]),(self.point_1_2[j][2],self.point_1_2[j][3]),(0,0,255),2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img_color_1, str(Min_L), (M_x,M_y), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    self.L=Min_L
                    break
        if Jubged_comboBox=="Middle":
            for j in range (len (self.length_point_1_2)):
               # if Min_L==self.length_point_1_2[j]:
                    M_x=int ((self.point_1_2[j][0]+self.point_1_2[j][2])*0.5)+5
                    M_y=int ((self.point_1_2[j][1]+self.point_1_2[j][3])*0.5)+5
                
                    cv2.line(img_color_1,(self.point_1_2[j][0],self.point_1_2[j][1]),(self.point_1_2[j][2],self.point_1_2[j][3]),(0,0,255),2)
                    
            
        return self.L,len(self.length_point_1_2),img_color 
     
    def divid_middle_point(self,shift,point_1,direction,coordinate,direction_scan,Jubged_comboBox,img_color):
        img_color_1=cv2.rectangle(img_color,(self.x0,self.y0),(self.x1,self.y1),(0,0,255),3)
        img_color_1=img_color[self.y0:self.y1,self.x0:self.x1]
        len_1=len(self.list_point_divided[0])
        len_2=len(self.list_point_divided[1])
        for i in range (len_2-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[1][i][0],self.list_point_divided[1][i][1]),(self.list_point_divided[1][i+1][0],self.list_point_divided[1][i+1][1]),(0,255,0),2)
        for i in range (len_1-1):
                img_color_1=cv2.circle(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),3,(255,0,0),1)
                img_color_1=cv2.line(img_color_1,(self.list_point_divided[0][i][0],self.list_point_divided[0][i][1]),(self.list_point_divided[0][i+1][0],self.list_point_divided[0][i+1][1]),(0,255,0),2)   

        M_x=int ((self.point_1_2[point_1][0]+self.point_1_2[point_1][2])*0.5)-5
        M_y=int ((self.point_1_2[point_1][1]+self.point_1_2[point_1][3])*0.5)-5
                
        cv2.line(img_color_1,(self.point_1_2[point_1][0],self.point_1_2[point_1][1]),(self.point_1_2[point_1][2],self.point_1_2[point_1][3]),(0,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_color_1, str(self.length_point_1_2[point_1]), (M_x,M_y), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        
        return self.length_point_1_2[point_1],img_color
