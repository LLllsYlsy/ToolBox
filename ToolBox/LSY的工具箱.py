# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:59:23 2020

@author: HP
"""
import subprocess
import os
import time
import json
import ffmpy
import sys#导入系统
from urllib import request,parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PIL import Image
import argparse
 
 
class FirstUi(QMainWindow):#第一个窗口类
    def __init__(self):
        super(FirstUi, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(580, 300)#设置窗口大小
        self.setWindowTitle('LSY的工具箱')#设置窗口标题
        self.btn1 = QPushButton('日历', self)#设置按钮和按钮名称
        self.btn1.setGeometry(30, 50, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn1.clicked.connect(self.slot_Calendarbtn_function)#将信号连接到槽
        self.btn1.setIcon(QIcon("日历.ico"))
        self.setWindowIcon(QIcon('main-icon.ico'))
        
        self.btn2 = QPushButton('字符画转换', self)#设置按钮和按钮名称
        self.btn2.setGeometry(200, 50, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn2.clicked.connect(self.slot_DrowByteUibtn_function)#将信号连接到槽
        self.btn2.setIcon(QIcon("转换图形.ico"))
        
        self.btn3 = QPushButton('计算器', self)#设置按钮和按钮名称
        self.btn3.setGeometry(380, 50, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn3.clicked.connect(self.slot_CalculatorUibtn_function)#将信号连接到槽
        self.btn3.setIcon(QIcon("计算器.ico"))
        
        self.btn4 = QPushButton('视频下载/转换', self)#设置按钮和按钮名称
        self.btn4.setGeometry(30, 150, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn4.clicked.connect(self.slot_DownloadUibtn_function)#将信号连接到槽
        self.btn4.setIcon(QIcon("视频.ico"))
        
        self.btn5 = QPushButton('音乐播放器', self)#设置按钮和按钮名称
        self.btn5.setGeometry(200, 150, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn5.clicked.connect(self.slot_MusicUibtn_function)#将信号连接到槽
        self.btn5.setIcon(QIcon("音乐.ico"))
        
        self.btn6 = QPushButton('翻译', self)#设置按钮和按钮名称
        self.btn6.setGeometry(380, 150, 150, 50)#前面是按钮左上角坐标，后面是窗口大小
        self.btn6.clicked.connect(self.slot_TranslationUibtn_function)#将信号连接到槽
        self.btn6.setIcon(QIcon("翻译.ico"))
        
        
    #跳转日历界面I
    def slot_Calendarbtn_function(self):
        self.hide()#隐藏此窗口
        self.s = CalendarUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    #字符画转换界面
    def slot_DrowByteUibtn_function(self):
        self.hide()#隐藏此窗口
        self.s = DrowByteUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    
    #字符画转换界面
    def slot_DownloadUibtn_function(self):
        self.hide()#隐藏此窗口
        self.s = DownloadUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    
    #计算器界面
    def slot_CalculatorUibtn_function(self):
        self.hide()#隐藏此窗口
        self.s = CalculatorUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    #音乐播放器界面
    def slot_MusicUibtn_function(self):
        self.hide()#隐藏此窗口
        self.s = MusicUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    
    #翻译界面
    def slot_TranslationUibtn_function(self):
        self.hide()#隐藏此窗口
        self.s = TranslationUi()#将第二个窗口换个名字
        self.s.show()#经第二个窗口显示出来
    
#日历功能 
class CalendarUi(QWidget):#建立第二个窗口的类
    def __init__(self):
        super(CalendarUi, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        
        self.resize(500, 350)#设置第二个窗口代码
        self.setWindowTitle('日历')#设置第二个窗口标题
        self.btn = QPushButton('返回', self)#设置按钮和按钮名称
        self.btn.setGeometry(350, 200, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        self.setWindowIcon(QIcon('日历.ico'))
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
 
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
 
        self.setGeometry(300, 300, 500, 300)
        self.show()
 
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
        
    def showDate(self, date):
        self.lbl.setText(date.toString())
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
 
#字符画转换
class DrowByteUi(QWidget):#建立第三个窗口的类
    def __init__(self):
        super(DrowByteUi, self).__init__()
        self.init_ui()
        self.cur_path=''
        self.img_path=''
        self.WIDTH=300
        self.HEIGHT=100
        
          
        self.ascii_char = list("10")  
 
    def init_ui(self):
        font = QFont()
        font.setFamily("Arial") #括号里可以设置成自己想要的其它字体
        font.setPointSize(1)
        self.setWindowIcon(QIcon('转换图形.ico'))
        self.resize(500, 350)#设置第三个窗口代码
        self.setWindowTitle('字符转换')#设置第三个窗口标题
        self.btn = QPushButton('返回', self)#设置按钮和按钮名称
        self.btn.setGeometry(350, 30, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        
        self.btnUp = QPushButton('选择图片', self)#设置按钮和按钮名称
        self.btnUp.setGeometry(50, 30, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnUp.clicked.connect(self.openDir)#将信号连接到槽
        self.btnUp.setStyle(QStyleFactory.create('Fusion'))
        
        self.btnChange = QPushButton('开始转换', self)#设置按钮和按钮名称
        self.btnChange.setGeometry(200, 30, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnChange.clicked.connect(self.changeImg)#将信号连接到槽
        self.btnChange.setStyle(QStyleFactory.create('Fusion'))
        
        self.text1 = QTextEdit(self)
        self.text1.setFocusPolicy(Qt.NoFocus) 
        self.text1.setGeometry(10,150,0,0)
        self.text1.setFont(font)
 
        self.lbl = QLabel(self)
        self.lbl.setGeometry(300, 200,300,300)
        
    def openDir(self):
        #self.reset()
        self.cur_path = QFileDialog.getOpenFileName(self, "选取图片", '',"*.jpg;;*.png;;All Files(*)")
        #print(self.cur_path[0])
        self.img_path=self.cur_path[0]
        img = Image.open(self.img_path)
        print(img.size[1])
        image = QImage(self.img_path)
        size = QSize(int(img.size[0]*0.6), int(img.size[1]*0.6))
        pixImg = QPixmap.fromImage(image.scaled(size, Qt.IgnoreAspectRatio))
        self.lbl.setGeometry(50, 100,img.size[0],img.size[1])
        self.resize(500+img.size[0]*0.6, 350+img.size[1]*0.6)#设置第三个窗口代码
        self.text1.setGeometry(img.size[0]*0.6+60,100,img.size[0]*0.6,img.size[1]*0.6)
        self.lbl.resize(img.size[0]*0.6, img.size[1]*0.6)
        self.lbl.setPixmap(pixImg)
        
        
    def changeImg(self):
        im=Image.open(self.img_path)  
        im=im.resize((self.WIDTH,self.HEIGHT),Image.NEAREST)  
        txt=""  
        for i in range(self.HEIGHT):  
            for j in range(self.WIDTH):  
                txt+=self.get_char(*im.getpixel((j,i)))  
            txt+='\n'  
      
        print (txt)  
        self.text1.setText(txt)
        #写入文件
        with open("output.txt",'w') as f:  
            f.write(txt)
        
    #将256灰度映射到70个字符上  
    def get_char(self,r,g,b,alpha=256):#alpha透明度  
        if alpha==0:  
            return ' '  
        length=len(self.ascii_char)  
        gray=int(0.299 *r+0.587*g+0.114*b)#计算灰度  
        unit=(256.0+1)/length  
        return self.ascii_char[int(gray/unit)]#不同的灰度对应着不同的字符  
    
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#计算器
class CalculatorUi(QWidget):#建立第四个窗口的类
    def __init__(self):
        super(CalculatorUi, self).__init__()
        self.init_ui()
        self.reset()
 
    def init_ui(self):
        font = QFont()
        font.setFamily("微软雅黑") #括号里可以设置成自己想要的其它字体
        font.setPointSize(16)
        self.resize(600, 650)#设置第四个窗口代码
        self.setWindowTitle('计算器')#设置第四个窗口标题
        #self.btn = QPushButton('返回', self)#设置按钮和按钮名称
        #self.btn.setGeometry(150, 150, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        #self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        self.setWindowIcon(QIcon('计算器.ico'))
        # 设置文本
        self.lineEdit = QLineEdit("0")
        # 文本从右面开始显示
        self.lineEdit.setAlignment(Qt.AlignRight)
        # 禁止直接输入 只读
        self.lineEdit.setReadOnly(True)
        # 设置显示文本得到字体
        self.lineEdit.setFont(QFont("Times", 20))
        # 设置最多显示的数字长度
        self.lineEdit.setMaxLength(15)
        grid = QGridLayout()
        self.setLayout(grid)
 
        names = [
            "AC", "Del", "back", "close",
            "7",  "8", "9", "+",
            "4",  "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "=", "/"
            ]
        
        positions = [(i,j) for i in range(1,6) for j in range(0,4)]
        grid.addWidget(self.lineEdit, 0, 0, 1, 4)
        for position, name in zip(positions, names):
            btn = QPushButton(name)
            btn.resize(btn.sizeHint())
            btn.setFont(font)
            btn.setFixedSize(90, 60)
            btn.clicked.connect(self.buttonClick)
            if name == '':
                continue
            grid.addWidget(btn, *position)
            
        #self.move(300, 150)
        self.setLayout(grid)
        self.show()
    
    def buttonClick(self):
        # 获取number
        text = self.sender().text()
        print(text)
        if text in "+-*/":
            self.string += text
            # 用来存储表达式
            self.number = ""
            # 在这里如果继续执行的话在界面展示会有问题所以退出
            self.last = text
            return
        # 用eval的话不需要判断点
        # elif text == ".":
 
        elif text == "=":
            self.resault()
            return
        elif text == "AC":
            self.reset()
        elif text == "Del":
            self.deleat()
        elif text == "close":
            self.close()
        elif text == "back":
            self.slot_btn_function()
        else:
            # 如果之前已经按了等号在按数字的话清空之前的值
            if self.last == "=" and type(eval(text)) == int:
                self.reset()
            # 除零判断
            elif self.last == "/" and text == "0":
                self.number = "error"
                self.lineEdit.setText(self.number)
                return
            # 如果 self.number ！= 0 self.number = self.number + text 否则 self.number = text
            if self.number != "0":
                self.number = self.number + text
            else:
                self.number = text
            #self.number = self.number + text if self.number != "0" else text
            self.string += text
            # 用来记录按键
        self.lineEdit.setText(self.number)
        
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
    def resault(self):
        self.lineEdit.setText(str(eval(self.string)))
        # 这一个设置每次运算完后直接将结果改变
        self.string = str(eval(self.string))
        self.number = ""
        self.last = "="
 
    def reset(self):
        #重置用来接收按钮数字
        self.number = "0"
        # 重置用来存储按钮数字和运算符的字符串
        self.string = ""
        self.last = ""
        self.symbol = ""
 
    def deleat(self):
        self.string = self.string[0:-1]
        # self.number = self.number[0:-1]
        # # 如果self.number 的删除后为空则设置为0
        # if not self.number:
        #     self.number = "0"
        # 间写
        self.number = self.number[0: -1] if self.number[0: -1] else "0"
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
 
#下载工具
class DownloadUi(QWidget):#建立第五个窗口的类
    def __init__(self):
        super(DownloadUi, self).__init__()
        self.init_ui()
        self.url=''
        self.FilePath=''
        self.dirPath=os.getcwd()
        self.reset()
        self.oldPath=''
        self.oldFilePath=''
 
    def init_ui(self):
        self.resize(500, 500)#设置第五个窗口代码
        font = QFont()
        font.setFamily("微软雅黑") #括号里可以设置成自己想要的其它字体
        font.setPointSize(16)
        self.setWindowIcon(QIcon('视频.ico'))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)#禁止最大化
        self.setWindowTitle('视频下载/转换工具')#设置第五个窗口标题
        self.btn1 = QPushButton('返回', self)#设置按钮和按钮名称
        self.btn1.setGeometry(50, 200, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn1.clicked.connect(self.slot_btn_function)#将信号连接到槽
        self.btn2 = QPushButton('下载', self)#设置按钮和按钮名称
        self.btn2.setGeometry(350, 200, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn2.clicked.connect(self.Download1)#将信号连接到槽
        
        self.le1 = QLineEdit(self)
        self.le1.setGeometry(130, 100,300,50)
        self.le1.textChanged.connect(self.getCon)
        
        self.lbl1 = QLabel("视频下载/转换工具", self)
        self.lbl1.setFont(font)
        self.lbl1.setGeometry(150, 20, 300, 50)
        
        self.lbl2 = QLabel("视频链接：", self)
        self.lbl2.setFont(font)
        self.lbl2.setGeometry(10, 100, 120, 50)
        
        self.lbl3 = QLabel("", self)
        #self.lbl3.setFont(font)
        self.lbl3.setGeometry(10, 150, 400, 50)
        
        self.btn3 = QPushButton('', self)#设置按钮和按钮名称
        self.btn3.setGeometry(435, 100, 50, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn3.setIcon(QIcon("文件夹.ico"))
        self.btn3.clicked.connect(self.OpenDir)#将信号连接到槽
        
        self.lbl4 = QLabel("FLV=>MP4转换", self)
        self.lbl4.setFont(font)
        self.lbl4.setGeometry(150, 260, 300, 50)
        
        self.lbl5 = QLabel("未选择文件", self)
        #self.lbl5.setFont(font)
        self.lbl5.setGeometry(10, 330, 360, 50)
    
        self.btn3 = QPushButton('', self)#设置按钮和按钮名称
        self.btn3.setGeometry(435, 330, 50, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn3.setIcon(QIcon("文件夹.ico"))
        self.btn3.clicked.connect(self.OpenFile)#将信号连接到槽
        
        self.btn4 = QPushButton('开始转换', self)#设置按钮和按钮名称
        self.btn4.setGeometry(200, 380, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn4.clicked.connect(self.change)#将信号连接到槽
        
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
    
    def reset(self): 
        self.lbl3.setText('下载到：'+self.dirPath)
        
    def Download1(self):
        print(1111)
        if self.url== '':
            return
        head = self.url.split("/")
        print(head)
        print('Download...')
        self.messageDialog()
        p = subprocess.call('you-get -o '+self.dirPath+' '+self.url)
        if p==0:
            msg_box = QMessageBox(QMessageBox.Warning, '下载状态', '下载成功!')
            msg_box.exec_()
       
    def change(self):
        if self.FilePath== '':
            return
        name = 'Change'+self.FilePath.split('/')[-1]
        name = name.split('.')[0]+'.mp4'
        print(name)
        
        ffmpeg_Path = os.path.join(os.getcwd(),'ffmpeg.exe')
        print(ffmpeg_Path)
        print('Changing...')
        self.messageDialog()
        p = subprocess.call(ffmpeg_Path+' -i '+self.FilePath+' -strict -2 -vcodec h264 '+name)
        if p==0:
            msg_box = QMessageBox(QMessageBox.Warning, '转换状态', '转换成功!')
            msg_box.exec_()
    def OpenDir(self):
        self.reset()
        self.oldPath=self.dirPath
        self.dirPath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.dirPath)
        #print(self.cur_path)
        if self.dirPath=='':
            self.dirPath=self.oldPath
        print(self.dirPath)
        self.lbl3.setText('下载到：'+self.dirPath)
            
    def OpenFile(self):
        self.oldFilePath=self.FilePath
        self.FilePath=QFileDialog.getOpenFileName(self, "选取要转换的文件", '',"*.FLV;;All Files(*)")
        #print(self.FilePath[0])
        self.FilePath = self.FilePath[0]
        if self.FilePath =='':
            self.FilePath=self.oldFilePath
            self.lbl5.setText('未选择文件')
            return
        print(self.FilePath)
        self.lbl5.setText('所选文件：'+self.FilePath.split('/')[-1])
    def getCon(self):
        self.url=self.sender().text()
    
    def messageDialog(self):
    	msg_box = QMessageBox(QMessageBox.Warning, '警告', '下载/转换中都会出现卡顿现象，请勿进行操作!')
    	msg_box.exec_()
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#音乐播放器
class MusicUi(QWidget):#建立第三个窗口的类
    def __init__(self):
        super(MusicUi, self).__init__()
        self.init_ui()
        self.reset()
        
    def init_ui(self):
        self.resize(500, 350)#设置第三个窗口代码
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)#禁止最大化
        self.setWindowTitle('音乐播放器')#设置第三个窗口标题
        self.btn = QPushButton('返回', self)#设置按钮和按钮名称
        self.btn.setGeometry(200, 260, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        
        self.setWindowIcon(QIcon('音乐.ico'))
        
        self.played = QMediaPlayer()
        self.played.setVolume(50.0)
        
        self.label2=QLabel(self)
        self.label2.setText("暂未播放音乐")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setGeometry(100, 200, 300, 50)
        
        self.btnUp = QPushButton('打开文件夹', self)#设置按钮和按钮名称
        self.btnUp.setGeometry(200, 30, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnUp.clicked.connect(self.openDir)#将信号连接到槽
        self.btnUp.setStyle(QStyleFactory.create('Fusion'))
        
        # --滑动条
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.sliderMoved[int].connect(lambda: self.played.setPosition(self.slider.value()))
        self.slider.setStyle(QStyleFactory.create('Fusion'))
        self.slider.setGeometry(100,150,300,50)
        
        # --计时器
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.playByMode)
        
        self.btnUp = QPushButton('上一首', self)#设置按钮和按钮名称
        self.btnUp.setGeometry(100, 100, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnUp.clicked.connect(self.previewMusic)#将信号连接到槽
        self.btnUp.setStyle(QStyleFactory.create('Fusion'))
        self.btnCon = QPushButton('播放', self)#设置按钮和按钮名称
        self.btnCon.setGeometry(200, 100, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnCon.clicked.connect(self.playMusic)#将信号连接到槽
        self.btnCon.setStyle(QStyleFactory.create('Fusion'))
        self.btnDown = QPushButton('下一首', self)#设置按钮和按钮名称
        self.btnDown.setGeometry(300, 100, 80, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btnDown.clicked.connect(self.nextMusic)#将信号连接到槽
        self.btnDown.setStyle(QStyleFactory.create('Fusion'))
        
    def slot_btn_function(self):
        self.played.pause() 
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
    
    def reset(self):
        self.cur_path=''
        self.songs_list=[]
        self.index=0
        self.is_pause=True
    def openDir(self):
        self.reset()
        self.cur_path = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cur_path)
        #print(self.cur_path)
        g = os.walk(self.cur_path)
        for path, d, files in g:
            for filename in files:
                file = os.path.join(path, filename)
                if 'mp3' in file:
                    self.songs_list.append(file)
        if self.cur_path:
            self.cur_playing_song = ''
            self.is_pause = True
            self.btnCon.setText('播放')
            print(self.songs_list)
            
            
    def playMusic(self):
        if len(self.songs_list) == 0:
            print(11111111111)
            self.Tips('当前路径内无可播放的音乐文件')
            return
        if not self.played.isAudioAvailable():
            self.setCurPlaying()
        if self.is_pause:
            self.played.play()
            self.label2.setText("当前播放:"+self.songs_list[self.index].split("\\")[-1])
            self.is_pause = False
            self.btnCon.setText('暂停')
            #print(self.played())
        elif not self.is_pause:
            self.played.pause()
            self.is_pause = True
            self.btnCon.setText('播放')
    
    '''上一首'''
    def previewMusic(self):
        self.slider.setValue(0)
        self.is_pause = True
        if len(self.songs_list) == 0 :
            self.setStatusTip('当前路径内无可播放的音乐文件')
            return
        if self.index != 0:
            self.index-=1
        else:
            self.index = len(self.songs_list)-1
        print(self.index)
        self.setCurPlaying()
        self.playMusic()
    '''下一首'''
    def nextMusic(self):
        self.slider.setValue(0)
        self.is_pause = True
        if len(self.songs_list) == 0 :
            self.setStatusTip('当前路径内无可播放的音乐文件')
            return
        if self.index != len(self.songs_list)-1:
            self.index+=1
        else:
            self.index=0
        self.setCurPlaying()
        self.playMusic()
    
    def setCurPlaying(self):
        self.cur_playing_song = self.songs_list[self.index]
        print(self.cur_playing_song)
        url = QUrl.fromLocalFile(self.cur_playing_song)
        print(url)
        self.played.setMedia(QMediaContent(url))
        
    def playByMode(self):
        if not self.is_pause:
            self.slider.setMinimum(0)
            self.slider.setMaximum(self.played.duration())
            self.slider.setValue(self.slider.value() + 1000)
        # 顺序播放
        if self.played.position() == self.played.duration():
            self.nextMusic()
            self.played.play()
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
     
#翻译      
class TranslationUi(QWidget):#建立第三个窗口的类
    def __init__(self):
        super(TranslationUi, self).__init__()
        self.init_ui()
        self.Translate_text=''
        self.HistoricalTranslation={}
        self.getHistoricalTranslation()
 
    def init_ui(self):
        font = QFont()
        font.setFamily("Arial") #括号里可以设置成自己想要的其它字体
        font.setPointSize(18)
        
        self.setWindowIcon(QIcon('翻译.ico'))
        
        self.resize(900, 350)#设置第三个窗口代码
        self.setWindowTitle('中英互译')#设置第三个窗口标题
        self.btn = QPushButton('返回', self)#设置按钮和按钮名称
        self.btn.setGeometry(450, 50, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        self.btn.setIcon(QIcon("icon.png"))
        self.le1 = QLineEdit(self)
        self.le1.setGeometry(10, 50,300,50)
        self.le1.textChanged.connect(self.getCon)
        self.le1.setFont(font)
        
        self.btn1 = QPushButton('翻译', self)#设置按钮和按钮名称
        self.btn1.setGeometry(330, 50, 100, 50)#前面是按钮左上角坐标，后面是按钮大小
        self.btn1.clicked.connect(self.getTranslate)#将信号连接到槽
        
        self.le2 = QLineEdit(self)
        self.le2.setGeometry(10, 100,150,30)
        self.le2.setText("翻译结果:")
        self.le2.setFont(font)
        self.le2.setFocusPolicy(Qt.NoFocus)
        self.le2.setStyleSheet('background:transparent;border:none')
        
        self.le3 = QLineEdit(self)
        self.le3.setGeometry(330, 100,150,30)
        self.le3.setText("历史翻译:")
        self.le3.setFont(font)
        self.le3.setFocusPolicy(Qt.NoFocus)
        self.le3.setStyleSheet('background:transparent;border:none')
        
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        j = 0#第几行（从0开始）
        i = 0#第几列（从0开始）
        self.tableWidget.setHorizontalHeaderLabels(['时间','翻译文本','结果'])  
        self.tableWidget.setColumnWidth(1,150)#设置j列的宽度
        self.tableWidget.setColumnWidth(2,260)#设置j列的宽度
        self.tableWidget.setRowHeight(i,30)#设置i行的高度
        self.tableWidget.setColumnWidth(0,180)#设置0列的宽度
        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直表头
        self.tableWidget.setGeometry(330,150,500,150)
        
        self.text1 = QTextEdit(self)
        self.text1.setFocusPolicy(Qt.NoFocus) 
        self.text1.setGeometry(10,150,300,150)
        self.text1.setFont(font)
        
    def getCon(self):
        self.Translate_text=self.le1.text()
        
    def getTranslate(self):
        if self.Translate_text=='':
            return
        Request_URL="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        form_data={}
        form_data['i']=self.Translate_text
        #print(form_data['from']+form_data['to'])
        form_data['smartresult'] = 'dict'
        form_data['doctype']='json'
        form_data['version']='2.1'
        form_data['keyfrom']='fanyi.web'
        form_data['action']='FY_BY_CLICKBUTTION'
        form_data['typoResult']='false'
        
        data=parse.urlencode(form_data).encode('utf-8')
        response=request.urlopen(Request_URL,data)
        html=response.read().decode('utf-8')
        translate_results = json.loads(html)
        print(translate_results)
        # 找到翻译结果
        translate_result = translate_results["translateResult"][0][0]['tgt']
        
        self.text1.setText(translate_result)
        self.localDir = os.getcwd()
        self.textDir = self.localDir+'/翻译文本.txt'
        with open(self.textDir,"a+",encoding='utf-8') as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"//"+self.Translate_text+'//'+translate_result+'\n')
        f.close()
        self.getHistoricalTranslation()
    
    def getHistoricalTranslation(self):
        self.localDir = os.getcwd()
        self.count=0
        self.index =0
        self.lists=[]
        self.textDir = self.localDir+'/翻译文本.txt'
        if not os.path.exists(self.textDir):
            open(self.textDir,'w')
        with open(self.textDir,"r",encoding='utf-8') as f:
            for line in f.readlines():
                #print(self.count)
                print(line)
                self.lists.append(line)
                self.count +=1
            self.tableWidget.setRowCount(self.count)
            for list in self.lists:
                self.tableWidget.setItem(self.index, 0, QTableWidgetItem(list.split("//")[0]))
                self.tableWidget.setItem(self.index, 1, QTableWidgetItem(list.split("//")[1]))
                self.tableWidget.setItem(self.index, 2, QTableWidgetItem(list.split("//")[2]))
                self.index+=1
        
        f.close()
        
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.f = FirstUi()#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来
    
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                               '本工具',
                                               "是否要退出程序？",
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    
def main():
    app = QApplication(sys.argv)
    w = FirstUi()#将第一和窗口换个名字
    w.show()#将第一和窗口换个名字显示出来
    sys.exit(app.exec_())#app.exet_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）
 

    
if __name__ == '__main__':#只有在本py文件中才能用，被调用就不执行
    main()