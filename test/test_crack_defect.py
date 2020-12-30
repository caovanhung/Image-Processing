import cv2
import numpy as np
import os
global allmin
global allmax
global allarea
global allnum
allmin=50000
allmax=0
allarea=0
allnum=0
def Change(img):
    # Thay đổi hình ảnh đen trắng thành trắng đen hoặc sử dụng chức năng cvThreshold
    sp = img.shape
    height = sp[0]  # height(rows) of image
    width = sp[1]  # width(colums) of image
    size = (width, height)
    iTmp = np.zeros(img.shape, np.uint8)
    for i in range(height):
        for j in range(width):
            iTmp[i, j] = 255 - img[i, j]
    cv2.imwrite(path, iTmp)# Ghi đè hình ảnh đen trắng ban đầu
    print("image %s bao ve thanh cong" % (path))

# 消除微小区域
def Big(contour):
    c_max = []
    for i in range(len(contour)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area < 30:
            contour.append(contour[i])
            c_min = []
            c_min.append(cnt)
            # thickness不为-1时，表示画轮廓线，thickness的值表示线的宽度。
            cv2.drawContours(img, c_min, -1, (0, 0, 0), thickness=-1)
            continue
        c_max.append(cnt)
    cv2.drawContours(img, c_max, -1, (255, 255, 255), thickness=-1)
    cv2.imwrite(path, img)
    print("image %s sua thanh cong" % (path))

def areaCal(contour):
    global allmin
    global allmax
    global allarea
    global allnum
    area = 0
    min=111111
    max=0

    for i in range(len(contour)):
        if cv2.contourArea(contour[i])>10:
            if cv2.contourArea(contour[i])>max:
                max=cv2.contourArea(contour[i])
            if cv2.contourArea(contour[i])<min:
                min=cv2.contourArea(contour[i])
            area += cv2.contourArea(contour[i])
            # print(len(contour))
            print("Tong so %d dien tich, dien tich cua %d dien tich la： %d" %(len(contour),i+1,cv2.contourArea(contour[i])))
    if area == 0:
        min = 0
    if min < allmin and min > 0:
        allmin = min
    if max > allmax:
        allmax = max
    allarea +=area
    allnum += len(contour)
    print("Dient ich toan phan la %d,dien tich toi da la %d，dien tich nho nhat la %d" % (area,max,min))
#Chu vi loi
def perimeterCal(contour):

    perimeter=0
    for i in range(len(contour)):
        if cv2.arcLength(contour[i],True)>10:
            perimeter += cv2.arcLength(contour[i],True)
            # print("共 %d 个缺陷，第 %d 个缺陷的周长为： %d" % (len(contour), i+1, cv2.arcLength(contour[i],True)))
    print("Tong chu vi cua khu vuc la %d" % perimeter)

num=0
filenum = 0
print("Chuong trinh bat dau chay......")
# if num==668:
while num<1600:
    num += 1
    #path='/home/hungcv/Desktop'+ str(num) +'.bmp'
    path = os.getcwd() + '/img_1/'+str(num)+'.bmp'
    if os.path.exists(path):
        filenum += 1
        img = cv2.imread(path)
        print("HInh anh %s tai thanh cong" %(path))
        # Change(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # Chuc nang phat hien duong vien
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Ve duong vien
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        # Big(contours)

        areaCal(contours)
        perimeterCal(contours)
        cv2.imshow("binary", binary)
        cv2.imshow("outline", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

averagearea = allarea/allnum
averagenum = allnum/filenum
print("Dien tich toi da cua vung %d" % (allmax))
print("Dien tich nho nhat cua vung %d" % (allmin))
print("Dien tich trung binh cua vung %d" % (averagearea))
print("So vung trung binh %d" % (averagenum))
print("Tong so vung %d" % (allnum))
print("Tong so hinh anh %d" % (filenum))