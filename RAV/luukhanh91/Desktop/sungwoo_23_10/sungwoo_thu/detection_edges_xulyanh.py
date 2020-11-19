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
    def __init__(self,img_1,img_2,x0,y0,x1,y1,x01,y01,x11,y11,x02,y02,x12,y12,x03,y03,x13,y13):
        self.y0=y0
        self.y1=y1
        self.x0=x0
        self.x1=x1

        self.y01=y01
        self.y11=y11
        self.x01=x01
        self.x11=x11


        self.y02=y02
        self.y12=y12
        self.x02=x02
        self.x12=x12

        self.y03=y03
        self.y13=y13
        self.x03=x03
        self.x13=x13


        
       # img_11=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
       # img_21=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
        self.img_cut=img_1[y0:y1,x0:x1]
        self.img_cut1=img_1[y01:y11,x01:x11]
        self.img_cut2=img_1[y02:y12,x02:x12]
        self.img_cut3=img_1[y03:y13,x03:x13]
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
            self.filter_img__0 = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img1 = cv2.blur(self.img_cut1,(self.kernel,self.kernel))
            self.filter_img2 = cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img__2= cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img3 = cv2.blur(self.img_cut3,(self.kernel,self.kernel))
            
            
        if filter_list=="Gaussian Filtering":
            self.filter_img__0 = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img1 = cv2.blur(self.img_cut1,(self.kernel,self.kernel))
            self.filter_img2 = cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img__2= cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img3 = cv2.blur(self.img_cut3,(self.kernel,self.kernel))
        if filter_list=="Median Filtering":
            self.filter_img__0 = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
            self.filter_img1 = cv2.blur(self.img_cut1,(self.kernel,self.kernel))
            self.filter_img2 = cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img__2= cv2.blur(self.img_cut2,(self.kernel,self.kernel))
            self.filter_img3 = cv2.blur(self.img_cut3,(self.kernel,self.kernel))
    def edges_img(self,lowlevel,highlevel):
        w,h=self.filter_img.shape
        self.img_thred=self.filter_img
     #  # self.img_thred_00=self.filter_img
        self.filter_img_00=self.filter_img[0:int (w*0.7),0:h]
        
        thresh, self.img_thred_01 = cv2.threshold(self.filter_img_00 ,254, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((0,0), np.uint8)
        self.img_thred_01 = cv2.dilate(self.img_thred_01, kernel, iterations=1)
     #   print(self.img_thred_01)
        self.filter_img_01=self.filter_img[int (w*0.7):w,0:h]
        thresh, self.img_thred_02 = cv2.threshold(self.filter_img_01 ,60, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((0,0), np.uint8)
        self.img_thred_02 = cv2.dilate(self.img_thred_02, kernel, iterations=1)
        self.img_thred[0:int (w*0.7),0:h]=self.img_thred_01
        self.img_thred[int (w*0.7):w,0:h]=self.img_thred_02

        thresh, self.img_thred_00 = cv2.threshold(self.filter_img__0,50, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((0,0), np.uint8)
        self.img_thred_00 = cv2.dilate(self.img_thred_00, kernel, iterations=1)
        
        self.edges_img=cv2.Canny(self.img_thred,lowlevel,highlevel)
        self.edges_img00=cv2.Canny(self.img_thred_00,lowlevel,highlevel)
        self.img[self.y0:self.y1,self.x0:self.x1]=self.edges_img

#000000000000000000000000000000000000000000000000000000000000000000000000000000

        thresh, self.img_thred1 = cv2.threshold(self.filter_img1 ,250, maxval=255, type=cv2.THRESH_BINARY)      
        kernel1 = np.ones((0,0), np.uint8)
        self.img_thred1 = cv2.dilate(self.img_thred1, kernel1, iterations=1) 
        self.edges_img1=cv2.Canny(self.img_thred1,lowlevel,highlevel)
        self.img[self.y01:self.y11,self.x01:self.x11]=self.edges_img1

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        w_2,h_2=self.filter_img2.shape
      #  print(w_2)
    #    print(h_2)
        self.img_thred2=self.filter_img2
     #  # self.img_thred_00=self.filter_img
        self.filter_img_21=self.filter_img2[0:int (w_2*0.7),0:h_2]
        
        thresh, self.img_thred_21 = cv2.threshold(self.filter_img_21 ,160, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((5,5), np.uint8)
        self.img_thred_21 = cv2.dilate(self.img_thred_21, kernel, iterations=1)
      #  print(self.img_thred_21.shape)

      
        self.filter_img_22=self.filter_img2[int (w_2*0.7):w_2,0:h_2]
        thresh, self.img_thred_22 = cv2.threshold(self.filter_img_22 ,20, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((5,5), np.uint8)
        self.img_thred_22 = cv2.dilate(self.img_thred_22, kernel, iterations=1)
      #  print(self.img_thred_22.shape)
        self.img_thred2[0:int (w_2*0.7),0:h_2]=self.img_thred_21
        self.img_thred2[int (w_2*0.7):w_2,0:h_2]=self.img_thred_22
        self.edges_img2=cv2.Canny(self.img_thred2,lowlevel,highlevel)

        thresh, self.img_thred_20 = cv2.threshold(self.filter_img__2,20, maxval=255, type=cv2.THRESH_BINARY)      
        kernel = np.ones((3,3), np.uint8)
    
        self.img_thred_20 = cv2.dilate(self.img_thred_20, kernel, iterations=1)    
        self.edges_img20=cv2.Canny(self.img_thred_20,lowlevel,highlevel)
        self.img[self.y02:self.y12,self.x02:self.x12]=self.edges_img2









 
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        thresh, self.img_thred3 = cv2.threshold(self.filter_img3 ,200, maxval=255, type=cv2.THRESH_BINARY)      
        kernel3 = np.ones((3,3), np.uint8)
        self.img_thred3 = cv2.dilate(self.img_thred3, kernel1, iterations=1) 
        self.edges_img3=cv2.Canny(self.img_thred3,lowlevel,highlevel)
        self.img[self.y03:self.y13,self.x03:self.x13]=self.edges_img3


        
       # self.img[self.y0:self.y1,self.x0:self.x1]=self.img_thred
    def edges_count(self,img_0):
        self.dien_tich_1=0
        self.dien_tich_21=0
        self.dien_tich_22=0
        self.dien_tich_3=0
        
        img=img_0[self.y0:self.y1,self.x0:self.x1]
        img_1=img_0[self.y01:self.y11,self.x01:self.x11]
        img_2=img_0[self.y02:self.y12,self.x02:self.x12]
        img_3=img_0[self.y03:self.y13,self.x03:self.x13]
        w,h=self.edges_img.shape
        self.edges_img_00=self.edges_img[0:int (w*0.7),0:h]
        img_00=img[0:int (w*0.7),0:h]
        
      #  im2,contours, hierarchy = cv2.findContours(self.img_thred,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NON)
        contours_00, hierarchy = cv2.findContours(self.edges_img_00,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     #   img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam00=[]
        for cnt in contours_00:
           area = cv2.contourArea(cnt)
           length=cv2.arcLength(cnt, True)
       #    print("leng.....",length)
       #    print("den_tich",area)
           if (length>50):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_00,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam00.append(tam)
   #     print("tam...........",self.point_tam00)


        self.edges_img_01=self.edges_img[int (w*0.7):w,0:h]
        img_01=img[int (w*0.7):w,0:h]
        #im2,contours, hierarchy = cv2.findContours(self.img_thred,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NON)
        contours_01, hierarchy = cv2.findContours(self.edges_img_01,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # print("len",contours_01)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam01=[]
        for cnt in contours_01:
           area = cv2.contourArea(cnt)
         #  print("den_tich",area)
           if (area>0):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_01,[box_1],0,(0,0,255),2)

             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam01.append(tam)
      #  print("00",self.point_tam00)
        contours_02, hierarchy = cv2.findContours(self.edges_img00,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     #   print("len",contours_01)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam02=[]
        for cnt in contours_02:
           length=cv2.arcLength(cnt, True)
          # print("den_tich",area)
           if (length>20):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
            # cv2.drawContours(img,[box_1],0,(0,255,0),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam02.append(tam)
           if length>400:
               self.dien_tich_1=1
               
   #     print("02",self.point_tam02)





#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        contours1, hierarchy = cv2.findContours(self.edges_img1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        w_1,h_1=self.edges_img1.shape
        self.point_tam1=[]
        for cnt in contours1:
           area = cv2.contourArea(cnt)
       #    print("den_tich",area)
           if (area>20):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_1,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             if tam[0]<0.5*h_1:
                 if area>400:
                     self.dien_tich_21=1
                    # print("????????????")
             if tam[0]>0.5*h_1:
                 if area>400:
                     self.dien_tich_22=1
                  #   print("????????????")
             self.point_tam1.append(tam)
     #   print(self.point_tam1)

#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        contours2, hierarchy = cv2.findContours(self.edges_img20,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   #    # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam22=[]
        for cnt in contours2:
           length=cv2.arcLength(cnt, True)
   #    #    print("den_tich",area)
           if (length>30):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
          #  cv2.drawContours(img_2,[box_1],0,(0,255,0),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam22.append(tam)
           if (length>100):            
                     self.dien_tich_3=1
      #  print("22222",self.point_tam22)
        w2,h2=self.edges_img2.shape
        self.edges_img_20=self.edges_img2[0:int (w2*0.7),0:h2]
        img_20=img_2[0:int (w2*0.7),0:h2]
        
      #  im2,contours, hierarchy = cv2.findContours(self.img_thred,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NON)
        contours_20, hierarchy = cv2.findContours(self.edges_img_20,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     #   img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam20=[]
        for cnt in contours_20:
           area = cv2.contourArea(cnt)
       #    print("den_tich",area)
           if (area>20):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_20,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam20.append(tam)

                
    #    print(self.point_tam00)


        self.edges_img_21=self.edges_img2[int (w2*0.7):w2,0:h2]
        img_21=img_2[int (w2*0.7):w2,0:h2]
        #im2,contours, hierarchy = cv2.findContours(self.img_thred,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NON)
        contours_21, hierarchy = cv2.findContours(self.edges_img_21,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # print("len",contours_01)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
       # self.point_tam01=[]
        for cnt in contours_21:
           area = cv2.contourArea(cnt)
         #  print("den_tich",area)
           if (area>0):
          #   print("da chay")
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_21,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam20.append(tam)
      #  print("20",self.point_tam20)


#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        contours3, hierarchy = cv2.findContours(self.edges_img3,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # img_1 = cv2.drawContours(img_1, contours, -1, (0,255,0), 3)
        self.point_tam3=[]
        for cnt in contours3:
           area = cv2.contourArea(cnt)
       #    print("den_tich",area)
           if (area>20):
             box = cv2.minAreaRect(cnt)
             retag=cv2.boxPoints(box)
             box_1 = np.int0(retag)
             cv2.drawContours(img_3,[box_1],0,(0,0,255),2)
             #img_1 = cv2.drawContours(img_1, box, -1, (0,255,0), 3)
             tam=(np.int0(0.25*(box_1[0]+box_1[1]+box_1[2]+box_1[3])))
             self.point_tam3.append(tam)
      #  print(self.point_tam3)
       # print(self.point_tam[0])
             
        return img_0
    def find_direction_xuly_2(self,img_0):
            img=img_0[self.y0:self.y1,self.x0:self.x1]
            img_1=img_0[self.y01:self.y11,self.x01:self.x11]
            img_2=img_0[self.y02:self.y12,self.x02:self.x12]
            img_3=img_0[self.y03:self.y13,self.x03:self.x13]
            self.direction=[]
           # self.direction.append()
            w_1,h_1=self.edges_img1.shape
            self.point_tam10=[]
            self.point_tam11=[]
                
            for i in range (len(self.point_tam1)):
                   if self.point_tam1[i][0]<0.5*h_1:
                      self.point_tam10.append(self.point_tam1[i])
                   else:
                        self.point_tam11.append(self.point_tam1[i])

            self.direction.append("KK")
            self.direction.append("KK")
          #  print("len_1",len( self.point_tam10))
           # print("len_2",len( self.point_tam11))
          #  print("len_2",len( self.point_tam22))
            if (len(self.point_tam02)==1 and len(self.point_tam1)==2 and len(self.point_tam22)==1):
                self.direction[0]="NNNNN"
                self.direction[1]="NNNNN"
                return self.direction
 
            Trunggian_1=0
            Trunggian_2=0
            dem_0=0;
            w_0,h_0=self.edges_img.shape
           # print("xxxxx",self.point_tam00)
          #  print("sssss",self.edges_img.shape)
            for i in range (len(self.point_tam00)):
                for j in range (len(self.point_tam01)):
                    if abs(self.point_tam00[i][0]-self.point_tam01[j][0])<10:
                        if  abs(0.7*w_0-self.point_tam00[i][1]+self.point_tam01[j][1])>0.4*w_0:
                            dem_0=dem_0+1
        #    print("////////////",dem_0)
            if dem_0>=1:
               #dem_01=0
              #  for i in range (len(self.point_tam02)-1):
                #    for j in range (i+1,len(self.point_tam02)):
              #           if abs(self.point_tam02[i][0]-self.point_tam02[j][0])<10:
              #              dem_01=dem_01+1               
             #   if dem_01>=0:
              ##       print ("vi tri can tim_W_1")
                     Trunggian_1=Trunggian_1+1
                     self.direction[0]="W"

                    # print(">>>>>>>>>>>",self.point_tam00)
                     for i in range (len(self.point_tam00)):
                            for j in range (j,len(self.point_tam01)):
                                if abs(self.point_tam00[i][0]-self.point_tam01[j][0])<10:
                                        w,h,l=img.shape
                                        #cv2.circle(img, (self.point_tam00[i][0],self.point_tam00[i][1]),3, (0, 255, 0), 2)
                                        #cv2.circle(img, (self.point_tam00[j][0],self.point_tam00[j][1]),3, (0, 255, 0), 2)
                                        Mx=int((self.point_tam00[i][0]+self.point_tam01[j][0])*0.5)
                                        My=int(w_0*0.5)
                                        font = cv2.FONT_HERSHEY_SIMPLEX
                                        img=cv2.putText(img,"w", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
        
                #else :
                  #   print("k phai vi tri W_1 ")
            else :
                     print("k phai vi tri W_1")
     #00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            w_1,h_1=self.edges_img1.shape
            self.point_tam10=[]
            self.point_tam11=[]
            
            for i in range (len(self.point_tam1)):
                if self.point_tam1[i][0]<0.5*h_1:
                    self.point_tam10.append(self.point_tam1[i])
                else:
                    self.point_tam11.append(self.point_tam1[i])
            dem_10=0
            for i in range (len(self.point_tam10)-1):
                for j in range (i+1,len(self.point_tam10)):
                    if abs(self.point_tam10[i][0]-self.point_tam10[j][0])<5:
                        if abs(self.point_tam10[i][1]-self.point_tam10[j][1])>0.3*w_1:
                            w,h,l=img_1.shape
                            Mx=int((self.point_tam10[i][0]+self.point_tam10[j][0])*0.5)
                            My=int(w*0.5)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            img=cv2.putText(img_1,"E", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

                        
                            dem_10=dem_10+1
            if dem_10==1:
         #      print ("vi tri can tim_E_1")
                Trunggian_1=Trunggian_1+1
                self.direction[0]="E"
            else :
                print ("vi tri k phai can tim_E_1")            
            dem_11=0
         #   print("yyyyyyyyyyyyyy",self.point_tam11)
       #     print("shape",self.edges_img1.shape)
            for i in range (len(self.point_tam11)-1):
                for j in range (i+1,len(self.point_tam11)):
                    if abs(self.point_tam11[i][0]-self.point_tam11[j][0])<5:
                        print("Kc",abs(self.point_tam11[i][1]-self.point_tam11[j][1]))
                        if abs(self.point_tam11[i][1]-self.point_tam11[j][1])>0.3*w_1:
                            w,h,l=img_1.shape
                            Mx=int((self.point_tam11[i][0]+self.point_tam11[j][0])*0.5)
                            My=int(w*0.5)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            img=cv2.putText(img_1,"E", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
                        
                            dem_11=dem_11+1
            if dem_11==1:
                print ("vi tri can tim_E_2")
                Trunggian_2=Trunggian_2+1
                self.direction[1]="E"
            else :
                print ("vi tri k phai can tim_E_2")   
                    





                     
    #1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
         #   print("000000002222",self.point_tam20)
            dem_2=0;

            w_2,h_2=self.edges_img2.shape
            for i in range (len(self.point_tam20)-1):
                for j in range (i+1,len(self.point_tam20)):
                    if abs(self.point_tam20[i][0]-self.point_tam20[j][0])<10:
                        if abs(0.7*w_2-self.point_tam20[i][1]+self.point_tam20[j][1])>0.5*w_2:
                            dem_2=dem_2+1
            if dem_2==1:
             #   dem_02=0
              #  for i in range (len(self.point_tam22)-1):
              #      for j in range (i+1,len(self.point_tam22)):
               #          if abs(self.point_tam22[i][0]-self.point_tam22[j][0])<10:
              #              dem_02=dem_02+1               
              #  if dem_02>=1:

                 #   w,h,l=img_2.shape
                                        #cv2.circle(img, (self.point_tam00[i][0],self.point_tam00[i][1]),3, (0, 255, 0), 2)
                    for i in range (len(self.point_tam20)-1):
                        for j in range (i+1,len(self.point_tam20)):
                          if abs(self.point_tam20[i][0]-self.point_tam20[j][0])<10:                    #cv2.circle(img, (self.point_tam00[j][0],self.point_tam00[j][1]),3, (0, 255, 0), 2)
                            Mx=int((self.point_tam20[i][0]+self.point_tam20[j][0])*0.5)
                            My=int(w_2*0.5)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            img=cv2.putText(img_2,"W", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)


                    
                #    print ("vi tri can tim_W_2")
                    self.direction[1]="W"
                    Trunggian_2=Trunggian_2+1
              #  else :
               #      print("k phai vi tri w_2 ")
            else :
                     print("k phai vi tri w_2")

    #22222222222222222222222222222222222222222222222222222222222222222222222222222222
            w_3,h_3=self.edges_img3.shape
            self.point_tam30=[]
            self.point_tam31=[]
            
            for i in range (len(self.point_tam3)):
                if self.point_tam3[i][0]<0.5*h_3:
                    self.point_tam30.append(self.point_tam3[i])
                else:
                    self.point_tam31.append(self.point_tam3[i])
            dem_30=0
            for i in range (len(self.point_tam30)-1):
                for j in range (i+1,len(self.point_tam30)):
                    if abs(self.point_tam30[i][1]-self.point_tam30[j][1])<10:
                        if abs(self.point_tam30[i][0]-self.point_tam30[j][0])>30:
                            dem_30=dem_30+1

                            w,h,l=img_3.shape
                            Mx=int((self.point_tam30[i][0]+self.point_tam30[j][0])*0.5)
                            My=int(w*0.5)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            img_3=cv2.putText(img_3,"N", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
            if dem_30==1:
              #  print ("vi tri can tim_S_1")
                Trunggian_1=Trunggian_1+1
                self.direction[0]="N"
            else :
                print ("vi tri k phai can tim_S_1")            
            dem_31=0
            for i in range (len(self.point_tam31)-1):
                for j in range (i+1,len(self.point_tam31)):
                    if abs(self.point_tam31[i][1]-self.point_tam31[j][1])<10:

                        if abs(self.point_tam31[i][0]-self.point_tam31[j][0])>30:

                            dem_31=dem_31+1
                       # dem_30=dem_30+1

                            w,h,l=img_3.shape
                            Mx=int((self.point_tam31[i][0]+self.point_tam31[j][0])*0.5)
                            My=int(w*0.5)
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            img_3=cv2.putText(img_3,"N", (Mx,My), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
            if dem_31==1:
                print ("vi tri can tim_S_2")
                self.direction[1]="N"
                Trunggian_2=Trunggian_2+1
            else :
                print ("vi tri k phai can tim_S_2")   
            if len( self.point_tam11)==1 and len(self.point_tam22)==1 and  self.dien_tich_22==1 and self.dien_tich_3==1 :                
            
                self.direction[1]="NNNNN"
            else :
                if Trunggian_2==0:
                    self.direction[1]="S"
           # print("dien tich ",self.dien_tich_22,self.dien_tich_3)
            if len( self.point_tam10)==1 and len(self.point_tam02)==1 and self.dien_tich_21==1 and self.dien_tich_1==1:
                self.direction[0]="NNNNN"
            else:
                if Trunggian_1==0:
                    self.direction[0]="S"

            return self.direction




                 
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
    #    print("Dem_1",Dem_1)
      #  print("Dem_2",Dem_2)
            
        print(len(self.point_tam))
        if ((Dem_1==0 and Dem_2%2==0)or(Dem_1==0 and Dem_2==0)or (Dem_1%2==0 and Dem_2==0) or (Dem_1%2==0 and Dem_2%2==0)):
         #   print("da chay")
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
    def find_direction_xuly_1(self,img):
        Dem_1=0
        Dem_2=0
        self.object_1=[]
        self.object_2=[]
        self.dir=[]
        img_1=img[self.y0:self.y1,self.x0:self.x1]
        w,h,l=img.shape
        if len(self.point_tam)!=0:
            for i in range(len(self.point_tam)):
                if (self.point_tam[i][0]<h*0.5):
                    self.object_1.append(self.point_tam[i])
                else :
                    self.object_2.append(self.point_tam[i])
        for i in range (len (self.object_1)):
            cv2.circle(img_1, (self.object_1[i][0], self.object_1[i][1]),3, (0, 255, 0), 2)
        for i in range (len (self.object_2)):
            cv2.circle(img_1, (self.object_2[i][0], self.object_2[i][1]),3, (255, 0, 0), 2)
        if len(self.object_1)==0:
            self.dir.append("S")
        if len(self.object_1)==1:
            self.dir.append("S")
        if len(self.object_1)==2:
            if abs(self.object_1[0][1]-self.object_1[1][1])<10:
                       Mx=int(0.5*(self.object_1[0][0]+self.object_1[1][0]))
                       My=int (0.5*(self.object_1[0][1]+self.object_1[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("N")
            elif abs(self.object_1[0][0]-self.object_1[1][0])<10:
                if self.object_1[0][0]<0.25*h:
                       Mx=int(0.5*(self.object_1[0][0]+self.object_1[1][0]))
                       My=int (0.5*(self.object_1[0][1]+self.object_1[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("W")                    
                if (self.object_1[0][0]<0.5*h and self.object_1[0][0]>0.25*h):
                    
                       Mx=int(0.5*(self.object_1[0][0]+self.object_1[1][0]))
                       My=int (0.5*(self.object_1[0][1]+self.object_1[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("E")              
            else:
                self.dir.append("S")
        dem_1_x=0
        dem_1_y=0
        self.find_point_x=[]
        self.find_point_y=[]
     #   print("ob1>>>>>>>>>>>>>>",self.object_1)
     #   print("ob2>>>>>>>>>>>>>>",self.object_2)
        if len(self.object_1)>=3:
            print("da chay_1")
            for i in range (len(self.object_1)-1):
                for j in range (i+1,len(self.object_1)):
                    if math.sqrt((self.object_1[i][0]-self.object_1[j][0])*(self.object_1[i][0]-self.object_1[j][0])+(self.object_1[i][1]-self.object_1[j][1])*(self.object_1[i][1]-self.object_1[j][1]))<50:
                        if abs(self.object_1[i][0]-self.object_1[j][0])<10:
                            self.find_point_x.append(self.object_1[i])
                            self.find_point_x.append(self.object_1[j])
                    #    print("KKKy",abs(self.object_1[i][0]-self.object_1[j][0]))
                        if abs(self.object_1[i][1]-self.object_1[j][1])<10:
                            self.find_point_y.append(self.object_1[i])
                            self.find_point_y.append(self.object_1[j])                        
            if len(self.find_point_x)==2 and len(self.find_point_y)==0:                  
                
                 if self.find_point_x[0][0]<0.25*h:
                       Mx=int(0.5*(self.find_point_x[0][0]+self.find_point_x[1][0]))
                       My=int (0.5*(self.find_point_x[0][1]+self.find_point_x[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("W")                    
                 if (self.find_point_x[0][0]<0.5*h and self.find_point_x[0][0]>0.25*h):
                    
                       Mx=int(0.5*(self.find_point_x[0][0]+self.find_point_x[1][0]))
                       My=int (0.5*(self.find_point_x[0][1]+self.find_point_x[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("E")             
            elif len(self.find_point_x)==0 and len(self.find_point_y)==2:       
                       Mx=int(0.5*(self.find_point_y[0][0]+self.find_point_y[1][0]))
                       My=int (0.5*(self.find_point_y[0][1]+self.find_point_y[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("N")
            else:
                 self.dir.append("NNNNNN")


        if len(self.object_2)==0:
            self.dir.append("S")
        if len(self.object_2)==1:
            self.dir.append("S")
        if len(self.object_2)==2:
            if abs(self.object_2[0][1]-self.object_2[1][1])<10:
                       Mx=int(0.5*(self.object_2[0][0]+self.object_2[1][0]))
                       My=int (0.5*(self.object_2[0][1]+self.object_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("N")
            elif abs(self.object_2[0][0]-self.object_2[1][0])<10:
                if self.object_2[0][0]>0.5*h and self.object_2[0][0]<0.75*h:
                       Mx=int(0.5*(self.object_2[0][0]+self.object_2[1][0]))
                       My=int (0.5*(self.object_2[0][1]+self.object_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("W")                    
                if (self.object_2[0][0]<h and self.object_2[0][0]>0.75*h):
                    
                       Mx=int(0.5*(self.object_2[0][0]+self.object_2[1][0]))
                       My=int (0.5*(self.object_2[0][1]+self.object_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("E")              
            else:
                self.dir.append("S")
        dem_1_x=0
        dem_1_y=0
        self.find_point_x_2=[]
        self.find_point_y_2=[]
        print("len_1",len(self.object_1))
        print("len_2",len(self.object_2))
        if len(self.object_2)>=3:
          #  print("da chay_2")
            for i in range (len(self.object_2)-1):
                for j in range (i+1,len(self.object_2)):
                    if math.sqrt((self.object_2[i][0]-self.object_2[j][0])*(self.object_2[i][0]-self.object_2[j][0])+(self.object_2[i][1]-self.object_2[j][1])*(self.object_2[i][1]-self.object_2[j][1]))<50:
                     #   print("KKK",abs(self.object_2[i][0]-self.object_2[j][0]))
                        if abs(self.object_2[i][0]-self.object_2[j][0])<10:
                            self.find_point_x_2.append(self.object_2[i])
                            self.find_point_x_2.append(self.object_2[j])
                     #   print("KKK",abs(self.object_2[i][0]-self.object_2[j][0]))
                        if abs(self.object_2[i][1]-self.object_2[j][1])<10:
                            self.find_point_y_2.append(self.object_2[i])
                            self.find_point_y_2.append(self.object_2[j])
          #  print("PPPPP_x_2",self.find_point_x_2)
         #  print("PPPPP_y_2",self.find_point_y_2)
            if len(self.find_point_x_2)==2 and len(self.find_point_y_2)==0:                  
                
                 if self.find_point_x_2[0][0]>0.5*h and self.find_point_x_2[0][0]<0.75*h:
                       Mx=int(0.5*(self.find_point_x_2[0][0]+self.find_point_x_2[1][0]))
                       My=int (0.5*(self.find_point_x_2[0][1]+self.find_point_x_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"W", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("W")                    
                 if (self.find_point_x_2[0][0]>0.75*h and self.find_point_x_2[0][0]<h):
                    
                       Mx=int(0.5*(self.find_point_x_2[0][0]+self.find_point_x_2[1][0]))
                       My=int (0.5*(self.find_point_x_2[0][1]+self.find_point_x_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"E", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                       self.dir.append("E")             
            elif len(self.find_point_x_2)==0 and len(self.find_point_y_2)==2:      
                       Mx=int(0.5*(self.find_point_y_2[0][0]+self.find_point_y_2[1][0]))
                       My=int (0.5*(self.find_point_y_2[0][1]+self.find_point_y_2[1][1]))
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       self.img_color_2=cv2.putText(img_1,"N", (Mx,My), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

                       self.dir.append("N")
            else:
                 self.dir.append("NNNNNN")

        print(self.dir)
        return self.dir,img
