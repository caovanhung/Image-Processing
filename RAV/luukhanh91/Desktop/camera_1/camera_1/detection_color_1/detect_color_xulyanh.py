import cv2
class xulyanh:
    def __init__(self,img):
        self.img=img
    def getdata(self):
        return self.img
    def setdata(self,img):
        self.img=img
    def GRB(self):
        img=cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        height,width,channel=img.shape
        Red=0;
        Green=0;
        Blue=0;
        for i in range(height):
            Red=Red+sum(img[i,:,0])
            Green=Green+sum(img[i,:,1])
            Blue=Blue+sum(img[i,:,2])
        Red=Red/(height*width)
        Green=Green/(height*width)
        Blue=Blue/(height*width)
        return Red,Green,Blue

    def HSV(self):
        img=cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        height,width,channel=img.shape
        H=0;
        S=0;
        V=0;
        for i in range(height):
            H=H+sum(img[i,:,0])
            S=S+sum(img[i,:,1])
            V=V+sum(img[i,:,2])


        H=H/(height*width)
        S=S/(height*width)
        V=V/(height*width)
        return H,S,V       
        
