from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
import time
# from main_un import *
# from ceshi_format import *
# from format_tab import *


class img_viewed(QWidget):
    def __init__(self,parent =None):
        super(img_viewed,self).__init__(parent)
        self.parent = parent
        self.width = 1500
        self.height = 500

        self.scroll_ares_images = QScrollArea(self)
        self.scroll_ares_images.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget(self)
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContends')

        # Bo cuc
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scroll_ares_images.setWidget(self.scrollAreaWidgetContents)

        self.scroll_ares_images.setGeometry(20, 50, self.width, self.height)  # khung show image
        self.vertocal1 = QVBoxLayout()


        # self.meanbar = QMenu(self)
        # self.meanbar.addMenu('&菜单')
        # self.openAct = self.meanbar.addAction('&Open',self.open)
        # self.startAct =self.meanbar.addAction('&start',self.start_img_viewer)
        self.open_file_pushbutton =QPushButton(self)
        self.open_file_pushbutton.setGeometry(150,10,100,30)
        self.open_file_pushbutton.setObjectName('open_pushbutton')
        self.open_file_pushbutton.setText('Mo thu muc...')
        self.open_file_pushbutton.clicked.connect(self.open)


        self.start_file_pushbutton = QPushButton(self)
        self.start_file_pushbutton.setGeometry(750, 10, 100, 30)
        self.start_file_pushbutton.setObjectName('start_pushbutton')
        self.start_file_pushbutton.setText('Start')
        self.start_file_pushbutton.clicked.connect(self.start_img_viewer)

        self.vertocal1.addWidget(self.scroll_ares_images) # set khung show img can hang doc
        self.show()



        #Dat kich thuoc xem truoc cua hinh anh
        self.displayed_image_size = 200
        self.col = 0
        self.row =0

        self.initial_path =None



    def open(self):
        file_path = QFileDialog.getExistingDirectory(self, 'Chon thu muc tep', '/')
        if file_path ==None:
            QMessageBox.information(self,'Canh bao','Tep trong, vui long thu lai')
        else:
            self.initial_path =file_path





    def start_img_viewer(self):
        if self.initial_path:
            file_path = self.initial_path
            print('file_path{}'.format(file_path))
            print(file_path)
            img_type = 'png'
            if file_path and img_type:

                png_list = list(i for i in os.listdir(file_path) if str(i).endswith('.{}'.format(img_type)))
                print(png_list)
                num = len(png_list)
                if num !=0:
                    for i in range(num):
                        image_id = str(file_path + '/' + png_list[i])
                        print(image_id)
                        pixmap = QPixmap(image_id)
                        self.addImage(pixmap, image_id)
                        print(pixmap)
                        QApplication.processEvents()
                else:
                    QMessageBox.warning(self,'Error','Tep hinh anh duoc tao trong')
                    self.event(exit())
            else:
                QMessageBox.warning(self,'Error','Tep trong, vui long doi')
        else:

            QMessageBox.warning(self, 'Error', 'Tep trong, vui long doi')


    def addImage(self, pixmap, image_id):
        #So column anh
        nr_of_columns = self.get_nr_of_image_columns()
        #So anh trong bo cuc
        nr_of_widgets = self.gridLayout.count()
        self.max_columns =nr_of_columns
        if self.col < self.max_columns:
            self.col =self.col +1
        else:
            self.col =0
            self.row +=1

        print('So hang{}'.format(self.row))
        print('So phan tu khong co trong bo cuc hien tai{}'.format(nr_of_widgets))

        print('So cot la{}'.format(self.col))
        clickable_image = QClickableImage(self.displayed_image_size, self.displayed_image_size, pixmap, image_id)
        clickable_image.clicked.connect(self.on_left_clicked)
        clickable_image.rightClicked.connect(self.on_right_clicked)
        self.gridLayout.addWidget(clickable_image, self.row, self.col)


    def on_left_clicked(self,image_id):
        print('left clicked - image id = '+image_id)

    def on_right_clicked(self,image_id):
        print('right clicked - image id = ' + image_id)


    def get_nr_of_image_columns(self):
        #Khu vuc hien thi hinh anh
        scroll_area_images_width = self.width
        if scroll_area_images_width > self.displayed_image_size:
            pic_of_columns = scroll_area_images_width // self.displayed_image_size  #tinh toan 1 hang va 1 so cot
        else:
            pic_of_columns = 1
        return pic_of_columns

class QClickableImage(QWidget):
    image_id =''

    def __init__(self,width =0,height =0,pixmap =None,image_id = ''):
        QWidget.__init__(self)

        self.layout =QVBoxLayout(self) #sua o day
        self.label1 = QLabel()
        self.label1.setObjectName('label1') # cot 1
        self.lable2 =QLabel()
        self.lable2.setObjectName('label2') #cot 2
        self.width =width
        self.height = height
        self.pixmap =pixmap

        if self.width and self.height:
            self.resize(self.width,self.height)
        if self.pixmap:
            pixmap = self.pixmap.scaled(QSize(self.width,self.height),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.label1.setPixmap(pixmap)
            self.label1.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label1)
        if image_id:
            self.image_id =image_id
            self.lable2.setText(image_id)
            self.lable2.setAlignment(Qt.AlignCenter)
            ###Lam cho label thich ung voi kich thuoc
            self.lable2.adjustSize()
            self.layout.addWidget(self.lable2)
        self.setLayout(self.layout)

    clicked = pyqtSignal(object)
    rightClicked = pyqtSignal(object)

    def mouseressevent(self,ev):
        print('55555555555555555')
        if ev.button() == Qt.RightButton:
            print('dasdasd')
            #Click chuot phai
            self.rightClicked.emit(self.image_id)
        else:
            self.clicked.emit(self.image_id)

    def imageId(self):
        return self.image_id



if __name__ =='__main__':
    app =QApplication(sys.argv)
    windo = img_viewed()
    windo.show()
    sys.exit(app.exec_())
