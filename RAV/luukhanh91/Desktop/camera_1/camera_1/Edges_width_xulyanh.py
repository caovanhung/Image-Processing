import cv2
import math
import numpy as np 
class Edges_width_xulyanh:
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
   #     print(self.img_cut)
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
     #       print("Averaging_1")
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
        if filter_list=="Gaussian Filtering":
            self.filter_img = cv2.GaussianBlur(self.img_cut,(self.kernel,self.kernel),0)
        if filter_list=="Median Filtering":
            self.filter_img =cv2.medianBlur(self.img_cut,self.kernel)
    def edges_img(self,lowlevel,highlevel):
      #  print(self.filter_img)
        self.img_edges=cv2.Canny(self.filter_img,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.img_edges
    def edges_count(self,img):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
      #  lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,1)
        self.contours, hierarchy = cv2.findContours(self.img_edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #    lines = cv2.HoughLinesP( self.img_edges,1,np.pi/180,100,10,1)
        img_cont=np.zeros_like(self.img_edges, np.uint8)
        print("len",len(self.contours))
 
        for i in range(len(self.contours)):
            trunggian=self.contours[i]
            for j in range (len(trunggian)):
                img_cont[trunggian[j][0][1],trunggian[j][0][0]]=255
            lines=0
            lines = cv2.HoughLines(img_cont,1,2*np.pi/180,30)
            circles=0

                
            circles = cv2.HoughCircles(img_cont,cv2.HOUGH_GRADIENT, 1, 10,param1=100, param2=30,minRadius=0,maxRadius=360)
          #  print("L",lines)
           # print("LL",len(lines))
            print("C",circles)
            if lines is not None:
                for rho,theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))
                    print ("x1",x1)
                    print("x2",x2)

                cv2.line(img_1,(x1,y1),(x2,y2),(0,0,255),2)
            if circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
                circles = np.uint16(np.around(circles)) 
  
                for pt in circles[0, :]: 
                    a, b, r = pt[0], pt[1], pt[2] 

                    cv2.circle(img_1, (a, b), r, (0, 255, 0), 2)  
                    cv2.circle(img_1, (a, b), 1, (0, 0, 255), 3)
            
         # #  if (circles!=None):
           # x_tam=int(circles[0][0][0])
           # y_tam=int(circles[0][0][1])
           # r_tam=int(circles[0][0][2])
           # cv2.circle(img_1, (x_tam,y_tam), r_tam, (0, 255, 0), 4)
                
            #for (x, y, r) in circles:
             #   cv2.circle(img_1, (x, y), r, (0, 255, 0), 4)
		# if (circles!=None):
              #  cv2.circle(img_1, (circles[0][0], circles[0][1]), circles[0][2], (0, 255, 0), 4)
                
            

        
       # for i in range(len(self.contours)):
        #    line_x=[]
       #     line_y=[]
       #     line_x_y=[]
       #     line_x_x=[]
       #     trunggian=self.contours[i]
         #   for j in range (len(trunggian)):
        #        line_x.append(trunggian[j][0][0])
        #        line_y.append(trunggian[j][0][1])
       #         line_x_y.append(trunggian[j][0][0]*trunggian[j][0][1])
       #         line_x_x.append(trunggian[j][0][0]*trunggian[j][0][0])
        #    b=(sum(line_x_y)-(sum(line_x)*sum(line_y)/len(self.contours[i])))/(sum(line_x_x)-(sum(line_x)*sum(line_x)/len(self.contours[i])))
       #     a=(sum(line_y))/len(self.contours[i])-b*(sum(line_x))/len(self.contours[i])
        #    print("a",a)
        #    print("b",b)
            
         #   test=[[0,0],[self.x1-self.x0,0],[0,self.y1-self.y0],[self.x1-self.x0,self.y1-self.y0]]
        #    point_A=[]
       #     point_B=[]
        #    for i in range (len(test)):
        #        y=a*test[i][0]+b
        #        print("y",y)
                
       #         x=(test[i][1]-b)/a
        #        print("x",x)
         #       if x>0 and y>0:
       #             x=int(x)
         #           y=int(y)
       #             point_A.append([test[i][0],y])
       #             point_B.append([x,test[i][1]])
         #   img_1=cv2.line(img_1,(point_A[0][1],point_A[0][0]),(point_B[0][1],point_B[0][0]),(0,255,0),2)
        
            

        
       # img_1 = cv2.drawContours(img_1, self.contours, -1, (0,255,0), 1)
       # for cnt in contours:
          #   box = cv2.minAreaRect(cnt)
            
        return img

    def edges_count_1(self,img,truc,number_pixel,Edge_threshold,Edge_sen):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
      #  lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,1)
        self.contours, hierarchy = cv2.findContours(self.img_edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        Not_line=[]
        self.line_a_b=[]
        self.line=[]
       # print(self.contours)
      #  img_cont=np.zeros_like(self.img_edges, np.uint8)
     #   dem=0
       # print(len(self.contours))
        for i in range(len(self.contours)):
            trunggian=self.contours[i]
            img_cont=np.zeros_like(self.img_edges, np.uint8)
            for j in range (len(trunggian)):
                img_cont[trunggian[j][0][1],trunggian[j][0][0]]=255
            lines=0
            lines = cv2.HoughLines(img_cont,number_pixel,Edge_sen*np.pi/360,Edge_threshold)
            circles=0          
         #   circles = cv2.HoughCircles(img_cont,cv2.HOUGH_GRADIENT, 1, 10,param1=100, param2=30,minRadius=0,maxRadius=360)
         #   if len(lines) == 0:
             #  Not_line.append(i)                
          #  print (lines)
            
            if lines is not None:
                for rho,theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))
                 #   dem=dem+1
                if (x1!=x2):
                    a1=(y2-y1)/(x2-x1)
                    b1=(y1*x2-x1*y2)/(x2-x1)
                else :
                    a1=x1
                    b1=-1
                    
                cv2.line(img_1,(x1,y1),(x2,y2),(0,0,255),2)
                self.line_a_b.append([a1,b1])
                self.line.append([x1,y1,x2,y2])
       #         print("i:",i)
            else :
                Not_line.append(i)
       #         print("not_i:",i)
        print ("not",Not_line)
        self.point_not_line_OX=[]    
        self.point_not_line_OY=[]
     #   print("dem",dem)
    #    for i in range(len(Not_line)):
      #      img_1 = cv2.drawContours(img_1, self.contours[Not_line[i]], -1, (0,255,0), 1)          
        for i in range(len(Not_line)):
            trunggian=self.contours[Not_line[i]]
            not_line_x=[]
            not_line_y=[]
            #img_1 = cv2.drawContours(img_1, trunggian, -1, (0,255,0), 1)
            for j in range (len(trunggian)):
                 #   cv2.circle(img_1,(trunggian[j][0][0],trunggian[j][0][1]),2,(255,0,0),2)
                    not_line_x.append(trunggian[j][0][0])
                    not_line_y.append(trunggian[j][0][1])
       #     print("x",not_line_x)
         #   print("y",not_line_y)
            max_x=max(not_line_x)
            min_x=min(not_line_x)
            max_y=max(not_line_y)
            min_y=min(not_line_y)
            for x in range (len(not_line_x)):
                if not_line_x[x]==max_x:
                    self.point_not_line_OX.append([max_x,trunggian[x][0][1]])
                    break
            for x in range (len(not_line_x)):
                if not_line_x[x]==min_x:
                    self.point_not_line_OX.append([min_x,trunggian[x][0][1]])
                    break            
        #    vitri_x=not_line_x.find(max_x,10)
          #  vitri_y=not_line_y.find(max_y,10)
            for y in range (len(not_line_y)):
                if not_line_y[y]==max_y:
                    self.point_not_line_OY.append([trunggian[y][0][0],max_y])
                    break
            for y in range (len(not_line_y)):
                if not_line_y[y]==min_y:
                    self.point_not_line_OY.append([trunggian[y][0][0],min_y])
                    break
         #   print ("ox",point_not_line_OX)
       #     print("oy",point_not_line_OY)
       # for i in range(len(point_not_line_OX)):
        #    cv2.circle(img_1,(point_not_line_OX[i][0],point_not_line_OX[i][1]),5,(0,255,255),2)
     #   for j in range (len (point_not_line_OX)):
       #     cv2.circle(img_1,(point_not_line_OX[j][0],point_not_line_OX[j][1]),2,(255,0,0),2)
        edge_point=[]    
        if (truc=="OX"):
            edge_point=self.point_not_line_OY
           # print("Ox")
            for i in range(len(self.line_a_b)):
                for j in range(len(self.point_not_line_OY)):
                    if (self.line_a_b[i][1]!=-1):
                        y_line=int(self.line_a_b[i][0]*self.point_not_line_OY[j][0]+self.line_a_b[i][1])
                #    print("y_line",y_line)
                 #   cv2.line(img_1,(point_not_line_OY[j][0]+1000,point_not_line_OY[j][1]),(0,point_not_line_OY[j][1]),(0,255,0),2)
                        cv2.line(img_1,(self.point_not_line_OY[j][0],y_line),(self.point_not_line_OY[j][0],self.point_not_line_OY[j][1]),(255,0,0),2)
                        cv2.circle(img_1,(self.point_not_line_OY[j][0],self.point_not_line_OY[j][1]),3,(0,0,255),2)
                    #else :
                   #     y_line=point_not_line_OY[j][1]
                     #   cv2.line(img_1,(point_not_line_OY[j][0],y_line),(point_not_line_OY[j][0],point_not_line_OY[j][1]),(255,0,0),2)
#
        if (truc=="OY"):
          #  print("OY")
            edge_point=self.point_not_line_OX
            for i in range(len(self.line_a_b)):
                for j in range(len(self.point_not_line_OX)):
                    if (self.line_a_b[i][0]!=0 and self.line_a_b[i][1]!=-1 ):
                        x_line=int((self.point_not_line_OX[j][1]-self.line_a_b[i][1])/self.line_a_b[i][0])
                #    y_line=int(line_a_b[i][0]*point_not_line_OY[j][0]+line_a_b[i][1])
                #    print("y_line",y_line)
                 #   cv2.line(img_1,(point_not_line_OY[j][0]+1000,point_not_line_OY[j][1]),(0,point_not_line_OY[j][1]),(0,255,0),2)
                        cv2.circle(img_1,(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),3,(0,0,255),2)
                        cv2.line(img_1,(x_line,self.point_not_line_OX[j][1]),(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),(255,0,0),2)
                    if (self.line_a_b[i][0]==0 and self.line_a_b[i][1]!=-1):
                         x_line=self.point_not_line_OX[j][0]
                         cv2.line(img_1,(x_line,self.point_not_line_OX[j][1]),(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),(255,0,0),2)
                         cv2.circle(img_1,(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),3,(0,0,255),2)
                    if (self.line_a_b[i][1]==-1):
                        x_line=self.line_a_b[i][0]
                        cv2.circle(img_1,(x_line,self.point_not_line_OX[j][1]),3,(0,0,255),2)
                        cv2.circle(img_1,(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),3,(0,0,255),2)
                        cv2.line(img_1,(x_line,self.point_not_line_OX[j][1]),(self.point_not_line_OX[j][0],self.point_not_line_OX[j][1]),(255,0,0),2)
                        
                         
        return len(self.line_a_b),len(edge_point),img
        
    def position_line(self,img,position,truc):# tim trung diem cua duong thang
        
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        self.length_1=0
        self.length_2=0
        if position=="Line":
            self.line_line=[]
            
            for i in range (len(self.line_a_b)):
                self.point_line_M=[]# giao cua duong thang voi cac truc 
                if self.line_a_b[i][0]==0:
                    x_A=0
                    x_B=abs(self.x0-self.x1)
                    y_A=int(self.line_a_b[i][1])
                    y_B=int(self.line_a_b[i][1])
                    x_M=int ((x_A+x_B)*0.5)
                    y_M=int ((y_A+y_B)*0.5)
             #   cv2.circle(img_1,(x_A,y_A),2,(255,0,0),2)
                    print("A",x_A,y_A)
                    print("B",x_B,y_B)
             #   cv2.circle(img_1,(x_B,y_B),2,(255,0,0),2)
                    self.line_line.append([x_M,y_M])

                elif self.line_a_b[i][1]==-1:
                    x_A=int(self.line_a_b[i][0])
                    x_B=int(self.line_a_b[i][0])
                    y_A=0
                    y_B=abs(self.y1-self.y0)
                    x_M=int ((x_A+x_B)*0.5)
                    y_M=int ((y_A+y_B)*0.5)
             #   cv2.circle(img_1,(x_A,y_A),2,(255,0,0),2)
                    print("A",x_A,y_A)
                    print("B",x_B,y_B)
             #   cv2.circle(img_1,(x_B,y_B),2,(255,0,0),2)
                    self.line_line.append([x_M,y_M])
                
                else :
                         
                         x_A=0
                         y_A=self.line_a_b[i][1]
                         self.point_line_M.append([x_A,y_A])
                         x_A=abs(self.x1-self.x0)
                         y_A=int(self.line_a_b[i][0]*abs(self.x0-self.x1)+self.line_a_b[i][1])
                         self.point_line_M.append([x_A,y_A])
                         x_B=int(-self.line_a_b[i][1]/self.line_a_b[i][0])
                         y_B=0
                         self.point_line_M.append([x_B,y_B])
                         x_B=int((abs(self.y1-self.y0)-self.line_a_b[i][1])/self.line_a_b[i][0])
                         y_B=abs(self.y1-self.y0)
                         self.point_line_M.append([x_B,y_B])
                if len(self.point_line_M)!=0:
                    self.point_line_M_trunggian=[]# trung diem cua cac duong thang
                    print("4 point",self.point_line_M)
                    for i in range (len(self.point_line_M)):# loai bo cac duong thang nam ngoai vung 
                          if self.point_line_M[i][0]>=0 and self.point_line_M[i][0]<=abs(self.x1-self.x0) and self.point_line_M[i][1]>=0 and self.point_line_M[i][1]<=abs(self.y1-self.y0):
                              self.point_line_M_trunggian.append(self.point_line_M[i])
                    print("2 point",self.point_line_M_trunggian)
                    print("point thu 1:",self.point_line_M_trunggian[0])
                    print("point thu 2:",self.point_line_M_trunggian[1])
                    x_M=int(0.5*(self.point_line_M_trunggian[0][0]+self.point_line_M_trunggian[1][0]))
                    y_M=int(0.5*(self.point_line_M_trunggian[0][1]+self.point_line_M_trunggian[1][1]))



                    self.line_line.append([x_M,y_M])
                self.length_1=len(self.line_line)
                self.length_2=len(self.line_line)
         
        if position=="Point":
            if truc=="OY":
                self.length_1=len(self.point_not_line_OX)
                self.length_2=len(self.point_not_line_OX)
                
            if truc=="OX":
                self.length_1=len(self.point_not_line_OY)
                self.length_2=len(self.point_not_line_OY)
        if position=="Point_Line":
            if truc=="OY":
                self.length_1=len(self.line_a_b)
                self.length_2=len(self.point_not_line_OX)
                
            if truc=="OX":
                self.length_1=len(self.line_a_b)
                self.length_2=len(self.point_not_line_OY)
        return self.length_1,self.length_2


    def display_value(self,img,value_edg_1,value_edg_2,truc):
        img_1=img[self.y0:self.y1,self.x0:self.x1]

        if (truc=="OX"):
            edge_point=self.point_not_line_OY
         #   for i in range(len(line_a_b)):
           #     for j in range(len(point_not_line_OY)):
            if (self.line_a_b[value_edg_1][1]!=-1):
                 y_line=int(self.line_a_b[value_edg_1][0]*self.point_not_line_OY[value_edg_2][0]+self.line_a_b[value_edg_1][1])
                 self.length_line=abs(self.point_not_line_OX[value_edg_2][1]-y_line)
                 M_x=int((self.point_not_line_OY[value_edg_2][0]+self.point_not_line_OY[value_edg_2][0])*0.5)
                 M_y=int((y_line+self.point_not_line_OY[value_edg_2][1])*0.5)
                 font = cv2.FONT_HERSHEY_SIMPLEX
                 cv2.circle(img_1,(self.point_not_line_OY[value_edg_2][0],y_line),2,(0,255,0),2)


                 cv2.line(img_1,(self.point_not_line_OY[value_edg_2][0],y_line),(self.point_not_line_OY[value_edg_2][0],self.point_not_line_OY[value_edg_2][1]),(0,255,0),2)
                 cv2.circle(img_1,(self.point_not_line_OY[value_edg_2][0],self.point_not_line_OY[value_edg_2][1]),2,(0,0,255),2)

              #   cv2.line(img_1,(self.point_not_line_OY[value_edg_2][0],self.point_not_line_OY[value_edg_2][1]),(self.point_not_line_OY[value_edg_2][0],self.point_not_line_OY[value_edg_2][1]+100),2,(0,0,255),2)
                 A_x=self.point_not_line_OY[value_edg_2][0]-20
                 A_y=self.point_not_line_OY[value_edg_2][1]
                 B_x=self.point_not_line_OY[value_edg_2][0]+20
                 B_y=self.point_not_line_OY[value_edg_2][1]
                 cv2.line(img_1,(A_x,A_y),(B_x,B_y),(0,255,0),2)
                 cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)
                 img_1=cv2.putText(img_1, str(self.length_line), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)


        if (truc=="OY"):
        
                    edge_point=self.point_not_line_OX
                    if (self.line_a_b[value_edg_1][0]!=0 and self.line_a_b[value_edg_1][1]!=-1 ):
                        x_line=int((self.point_not_line_OX[value_edg_2][1]-self.line_a_b[value_edg_1][1])/self.line_a_b[value_edg_2][0])

                        M_x=int((x_line+self.point_not_line_OX[value_edg_2][0])*0.5)
                        M_y=int((self.point_not_line_OX[value_edg_2][1]+self.point_not_line_OX[value_edg_2][1])*0.5)
                        cv2.circle(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),2,(255,0,255),2)
                        cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)
                        cv2.circle(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)
                        self.length_line=abs(self.point_not_line_OX[value_edg_2][0]-x_line)


                      #  cv2.line(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0]+100,self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)

                        A_x=self.point_not_line_OX[value_edg_2][0]
                        A_y=self.point_not_line_OX[value_edg_2][1]-20
                        B_x=self.point_not_line_OX[value_edg_2][0]
                        B_y=self.point_not_line_OX[value_edg_2][1]+20
                        cv2.line(img_1,(A_x,A_y),(B_x,B_y),(255,0,0),2)
                    #    print("A_x",A_x)

                        font = cv2.FONT_HERSHEY_SIMPLEX
                        img_1=cv2.putText(img_1, str(self.length_line), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

                        cv2.line(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(255,0,0),2)
                    if (self.line_a_b[value_edg_1][0]==0 and self.line_a_b[value_edg_1][1]!=-1):
                         x_line=self.point_not_line_OX[value_edg_2][0]
                         M_x=int((x_line+self.point_not_line_OX[value_edg_2][0])*0.5)
                         M_y=int((self.point_not_line_OX[value_edg_2][1]+self.point_not_line_OX[value_edg_2][1])*0.5)
                         cv2.circle(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),2,(255,0,255),2)

                         cv2.line(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(0,255,0),2)


                         cv2.circle(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)

                         A_x=self.point_not_line_OX[value_edg_2][0]
                         A_y=self.point_not_line_OX[value_edg_2][1]-20
                         B_x=self.point_not_line_OX[value_edg_2][0]
                         B_y=self.point_not_line_OX[value_edg_2][1]+20
                         cv2.line(img_1,(A_x,A_y),(B_x,B_y),(255,0,0),2)
                    #     print("A_x",A_x)
                         self.length_line=abs(self.point_not_line_OX[value_edg_2][0]-x_line)
                         cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)



                      #   cv2.line(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0]+100,self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)

                         img_1=cv2.putText(img_1, str(self.length_line), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    if (self.line_a_b[value_edg_1][1]==-1):
                        x_line=self.line_a_b[value_edg_1][0]
                        self.length_line=abs(self.point_not_line_OX[value_edg_2][0]-x_line)
                        M_x=int((x_line+self.point_not_line_OX[value_edg_2][0])*0.5)
                        M_y=int((self.point_not_line_OX[value_edg_2][1]+self.point_not_line_OX[value_edg_2][1])*0.5)
                        cv2.circle(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),2,(255,0,255),2)
                        cv2.circle(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)
                        cv2.line(img_1,(x_line,self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(0,255,0),2)
                        font = cv2.FONT_HERSHEY_SIMPLEX

                        A_x=self.point_not_line_OX[value_edg_2][0]
                        A_y=self.point_not_line_OX[value_edg_2][1]-20
                        B_x=self.point_not_line_OX[value_edg_2][0]
                        B_y=self.point_not_line_OX[value_edg_2][1]+20
                        cv2.line(img_1,(A_x,A_y),(B_x,B_y),(255,0,0),2)
                    #    print("A_x",A_x)

                        
                        cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)

                       # cv2.line(img_1,(self.point_not_line_OX[value_edg_2][0],self.point_not_line_OX[value_edg_2][1]),(self.point_not_line_OX[value_edg_2][0]+100,self.point_not_line_OX[value_edg_2][1]),3,(0,255,255),2)

                        img_1=cv2.putText(img_1, str(self.length_line), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        return self.length_line,img   
    def length_line_line(self,img,value_edg_1,value_edg_2,truc,position):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        self.position_line(img,position,truc)
        self.length_line_line_1=0 # khoang cac giua 2 duong thang 
        if (truc=="OY"):
            print("da chay")
            y_H=self.line_line[value_edg_2][1]
            if (self.line_a_b[value_edg_1][1]==-1):
                x_H=self.line_a_b[value_edg_1][0]
            else:
                x_H=int((y_H-self.line_a_b[value_edg_1][1])/self.line_a_b[value_edg_1][0])
            cv2.line(img_1,(x_H,y_H),(self.line_line[value_edg_2][0],self.line_line[value_edg_2][1]),(0,255,0),2)
            cv2.circle(img_1,(self.line_line[value_edg_2][0],self.line_line[value_edg_2][1]),3,(0,255,255),2)
            cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)
            cv2.line(img_1,(self.line[value_edg_2][0],self.line[value_edg_2][1]),(self.line[value_edg_2][2],self.line[value_edg_2][3]),(0,255,0),2)
            cv2.circle(img_1,(x_H,y_H),3,(0,255,255),2)
            self.length_line_line_1=abs (self.line_line[value_edg_2][0]-x_H)
            M_y=y_H
            M_x=int (0.5*(x_H+self.line_line[value_edg_2][0]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_1=cv2.putText(img_1, str(self.length_line_line_1), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            
        if (truc=="OX"):
            x_H=self.line_line[value_edg_2][0]
            y_H=int(self.line_a_b[value_edg_1][0]*x_H+self.line_a_b[value_edg_1][1])
            cv2.circle(img_1,(self.line_line[value_edg_2][0],self.line_line[value_edg_2][1]),3,(0,255,255),2)
           # print("X_H",x_H)
        #    print("y_H",y_H)
            cv2.line(img_1,(x_H,y_H),(self.line_line[value_edg_2][0],self.line_line[value_edg_2][1]),(0,255,0),2)
            cv2.circle(img_1,(x_H,y_H),3,(0,255,255),2)
            cv2.line(img_1,(self.line[value_edg_1][0],self.line[value_edg_1][1]),(self.line[value_edg_1][2],self.line[value_edg_1][3]),(0,255,0),2)
           # cv2.line(img_1,(self.line[value_edg_2][0],self.line[value_edg_2][1]),(self.line[value_edg_2][2],self.line[value_edg_2][3]),(255,0,0),2)
            self.length_line_line_1=abs (self.line_line[value_edg_2][1]-y_H)
            M_x=x_H
            M_y=int (0.5*(y_H+self.line_line[value_edg_2][1]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_1=cv2.putText(img_1, str(self.length_line_line_1), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)         
        return self.length_line_line_1,img
    def length_point_point(self,img,value_edg_1,value_edg_2,truc,position):
        img_1=img[self.y0:self.y1,self.x0:self.x1]
     #   self.position_line(img,position,truc)
        self.length_point_point_1=0
        if (truc=="OX"):
            print("ox....................")
            M_mid_x=int(0.5*(self.point_not_line_OY[value_edg_1][0]+self.point_not_line_OY[value_edg_2][0]))
            cv2.line(img_1,(M_mid_x,self.point_not_line_OY[value_edg_1][1]),(M_mid_x,self.point_not_line_OY[value_edg_2][1]),(255,0,0),2)
            cv2.line(img_1,(M_mid_x-100,self.point_not_line_OY[value_edg_1][1]),(M_mid_x+100,self.point_not_line_OY[value_edg_1][1]),(0,255,0),2)
            cv2.line(img_1,(M_mid_x-100,self.point_not_line_OY[value_edg_2][1]),(M_mid_x+100,self.point_not_line_OY[value_edg_2][1]),(0,255,0),2)
            cv2.circle(img_1,(M_mid_x,self.point_not_line_OY[value_edg_1][1]),3,(0,255,255),2)
            cv2.circle(img_1,(M_mid_x,self.point_not_line_OY[value_edg_2][1]),3,(0,255,255),2)
            self.length_point_point_1=abs(self.point_not_line_OY[value_edg_1][1]-self.point_not_line_OY[value_edg_2][1])
            M_x=M_mid_x
            M_y=int (0.5*(self.point_not_line_OY[value_edg_1][1]+self.point_not_line_OY[value_edg_2][1]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_1=cv2.putText(img_1, str(self.length_point_point_1), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            #img_1=cv2.putText(img_1, "00", (M_x,self.point_not_line_OY[value_edg_1][1]), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        if (truc=="OY"):
            print("oy....................")
            M_mid_y=int(0.5*(self.point_not_line_OX[value_edg_1][1]+self.point_not_line_OX[value_edg_2][1]))
            cv2.line(img_1,(self.point_not_line_OX[value_edg_1][0],M_mid_y),(self.point_not_line_OX[value_edg_2][0],M_mid_y),(255,0,0),2)
            cv2.line(img_1,(self.point_not_line_OX[value_edg_1][0],M_mid_y-100),(self.point_not_line_OX[value_edg_1][0],M_mid_y+100),(0,255,0),2)
            cv2.line(img_1,(self.point_not_line_OX[value_edg_2][0],M_mid_y-100),(self.point_not_line_OX[value_edg_2][0],M_mid_y+100),(0,255,0),2)
            cv2.circle(img_1,(self.point_not_line_OX[value_edg_1][0],M_mid_y),3,(0,255,255),2)
            cv2.circle(img_1,(self.point_not_line_OX[value_edg_2][0],M_mid_y),3,(0,255,255),2)
            self.length_point_point_1=abs(self.point_not_line_OX[value_edg_1][0]-self.point_not_line_OX[value_edg_2][0])
            M_y=M_mid_y
            M_x=int (0.5*(self.point_not_line_OY[value_edg_1][0]+self.point_not_line_OY[value_edg_2][0]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_1=cv2.putText(img_1, str(self.length_point_point_1), (M_x,M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            #img_1=cv2.putText(img_1, "00", (self.point_not_line_OY[value_edg_1][0],M_y), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        return self.length_point_point_1,img
        
    def display_value_A_B(self,img,value_edg_1,value_edg_2,truc,position):
        self.position_line(img,position,truc)
        if position=="line_point":
            self.length_line_point,self.img_xuly=self.display_value(self,img,value_edg_1,value_edg_2,truc)
