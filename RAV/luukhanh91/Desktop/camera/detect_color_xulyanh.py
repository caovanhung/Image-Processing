import cv2
class xulyanh:
    def __init__(self,img):
        self.img=img
    def getData(self):
        return self.img
    def setdata(self,img):
        self.img=img
    def GRB(self):
        img=cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        height,width,channel=img.shape
        Red=0;
        Green=0;
        Blue=0;
        for i in range(0,height):
            for j in range(0,width):
                Red=Red+img[i][j][0]
                Green=Green+img[i][j][1]
                Blue=Blue+img[i][j][2]

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
        for i in range(0,height):
            for j in range(0,width):
                H=H+img[i][j][0]
                S=S+img[i][j][1]
                V=V+img[i][j][2]

        H=H/(height*width)
        s=S/(height*width)
        V=V/(height*width)
        return H,S,V       
        
