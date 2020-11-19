import cv2
class Threshold_xulyanh:
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
    def Threshold_getdata(self):
        return self.img_s
    def Threshold_setdata(self,img):
        self.img_s=img_t
    def Threshold_set_thred(self,thread):
        self.thred=thread
    def template_matching(self,img_cut,img):
        kp1, des1 = sift.detectAndCompute(img_cut,None)
        kp2, des2 = sift.detectAndCompute(img,None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
# store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            h,w,d = img1.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv.perspectiveTransform(pts,M)
    #print ("hinh chu nhat",np.int32(dst))
   # print("..........",img1.shape)
            img2 = cv.polylines(img2,[np.int32(dst)],True,255,3, cv.LINE_AA)
        else:
            print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
            matchesMask = None
        return img_2
    
    def Threshold_xuly(self,thred,check):
        if check==1:
        #cv.THRESH_BINARY_INV
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY_INV)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
        if check==2:
            thresh, self.img_thred = cv2.threshold(self.img_s,thred, maxval=255, type=cv2.THRESH_BINARY)
            self.img_t[self.y0:self.y1,self.x0:self.x1]=self.img_thred
    
    def Threshold_count_den(self):
        dem=0
        w_i,h=self.img_thred.shape
        for i in range(w_i):
            for j in range(h):
                if self.img_thred[i][j]==0:
                   dem=dem+1
        return dem
