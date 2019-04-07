#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 23:39:33 2018

@author: li
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.6.1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


import shutil
import time
from PIL import Image

import matplotlib.image as mpimg # mpimg 用于读取图片


#from ij import IJ
import imagej 
import json 

import matplotlib.pyplot as plt
import os
import sys
import math
#import matplotlib.pyplot
import numpy as np
import array
current_path = os.getcwd()

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):

        super(Ui_MainWindow, self).__init__(parent)
        self.mode = []
        self.time = []
        self.path = []
        self.fixed = []
        self.single = []        
        self.setupUi(self)
        self.flag = 0
        self.way = 0  
        
# =============================================================================
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(550, 600)
#         font = QtGui.QFont()
#         font.setFamily("Arial")
#         font.setBold(False)
#         font.setWeight(50)
#         MainWindow.setFont(font)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(180, 480, 180, 75))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setObjectName("pushButton")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(20, 10, 361, 21))
#         self.label.setObjectName("label")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(120, 220, 221, 21))
#         self.label_4.setObjectName("label_4")
#         self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton.setGeometry(QtCore.QRect(20, 220, 89, 21))
#         font = QtGui.QFont()
#         font.setFamily("Arial")
#         self.radioButton.setFont(font)
#         self.radioButton.setObjectName("radioButton")
#         self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton_2.setGeometry(QtCore.QRect(20, 260, 91, 16))
#         self.radioButton_2.setObjectName("radioButton_2")
#         self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.textEdit.setGeometry(QtCore.QRect(340, 220, 41, 21))
#         self.textEdit.setObjectName("textEdit")
#         self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton_2.setGeometry(QtCore.QRect(110, 50, 91, 21))
#         self.toolButton_2.setObjectName("toolButton_2")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(20, 50, 91, 16))
#         self.label_2.setObjectName("label_2")
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(20, 290, 51, 16))
#         self.label_6.setObjectName("label_6")
#         self.label_8 = QtWidgets.QLabel(self.centralwidget)
#         self.label_8.setGeometry(QtCore.QRect(20, 190, 111, 16))
#         self.label_8.setObjectName("label_8")
#         self.label_9 = QtWidgets.QLabel(self.centralwidget)
#         self.label_9.setGeometry(QtCore.QRect(140, 260, 261, 16))
#         font = QtGui.QFont()
#         font.setFamily("Arial")
#         self.label_9.setFont(font)
#         self.label_9.setObjectName("label_9")
#         self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton_3.setGeometry(QtCore.QRect(20, 370, 89, 16))
#         self.radioButton_3.setObjectName("radioButton_3")
#         self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton_4.setGeometry(QtCore.QRect(20, 400, 89, 16))
#         self.radioButton_4.setObjectName("radioButton_4")
#         self.label_10 = QtWidgets.QLabel(self.centralwidget)
#         self.label_10.setGeometry(QtCore.QRect(20, 340, 54, 12))
#         self.label_10.setObjectName("label_10")
#         self.label_11 = QtWidgets.QLabel(self.centralwidget)
#         self.label_11.setGeometry(QtCore.QRect(20, 430, 151, 16))
#         self.label_11.setObjectName("label_11")
#         self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton_3.setGeometry(QtCore.QRect(440, 260, 91, 21))
#         self.toolButton_3.setObjectName("toolButton_3")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(60, 80, 291, 20))
#         self.label_3.setText("")
#         self.label_3.setObjectName("label_3")
#         self.label_7 = QtWidgets.QLabel(self.centralwidget)
#         self.label_7.setGeometry(QtCore.QRect(50, 290, 291, 20))
#         self.label_7.setText("")
#         self.label_7.setObjectName("label_7")
#         self.label_12 = QtWidgets.QLabel(self.centralwidget)
#         self.label_12.setGeometry(QtCore.QRect(160, 430, 291, 20))
#         self.label_12.setText("")
#         self.label_12.setObjectName("label_12")
#         self.label_13 = QtWidgets.QLabel(self.centralwidget)
#         self.label_13.setGeometry(QtCore.QRect(20, 80, 51, 16))
#         self.label_13.setObjectName("label_13")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(60, 140, 291, 20))
#         self.label_5.setText("")
#         self.label_5.setObjectName("label_5")
#         self.label_14 = QtWidgets.QLabel(self.centralwidget)
#         self.label_14.setGeometry(QtCore.QRect(20, 110, 91, 16))
#         self.label_14.setObjectName("label_14")
#         self.label_15 = QtWidgets.QLabel(self.centralwidget)
#         self.label_15.setGeometry(QtCore.QRect(20, 140, 51, 16))
#         self.label_15.setObjectName("label_15")
#         self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton_4.setGeometry(QtCore.QRect(110, 110, 91, 21))
#         self.toolButton_4.setObjectName("toolButton_4")
#         self.label_16 = QtWidgets.QLabel(self.centralwidget)
#         self.label_16.setGeometry(QtCore.QRect(70, 370, 211, 16))
#         self.label_16.setObjectName("label_16")
#         self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.textEdit_2.setGeometry(QtCore.QRect(280, 370, 51, 21))
#         self.textEdit_2.setObjectName("textEdit_2")
# # =============================================================================
# #         self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
# #         self.textEdit_2.setGeometry(QtCore.QRect(320, 380, 51, 21))
# #         self.textEdit_2.setObjectName("textEdit_2")
# # =============================================================================
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
# 
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
# 
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "IACT/ICT Generation"))
#         self.pushButton.setText(_translate("MainWindow", "Proceed"))
#         self.label.setText(_translate("MainWindow", "<html><head/><body><p>Input two CT images (In Analyze 7.5 format)</p></body></html>"))
#         self.label_4.setText(_translate("MainWindow", "Input value for n (n is larger than  0):  n="))
#         self.radioButton.setText(_translate("MainWindow", "Empirical"))
#         self.radioButton_2.setText(_translate("MainWindow", "Customized"))
#         self.toolButton_2.setText(_translate("MainWindow", "Select Image"))
#         self.label_2.setText(_translate("MainWindow", "End-expiration:"))
#         self.label_6.setText(_translate("MainWindow", "Path:"))
#         self.label_8.setText(_translate("MainWindow", "Read motion curve"))
#         self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Input motion curve file (In .xlsx format)</span></p></body></html>"))
#         self.radioButton_3.setText(_translate("MainWindow", "ICT"))
#         self.radioButton_4.setText(_translate("MainWindow", "IACT"))
#         self.label_10.setText(_translate("MainWindow", "Output"))
#         self.label_11.setText(_translate("MainWindow", "Output images saved at"))
#         self.toolButton_3.setText(_translate("MainWindow", "Select File"))
#         self.label_13.setText(_translate("MainWindow", "Path:"))
#         self.label_14.setText(_translate("MainWindow", "End-expiration:"))
#         self.label_15.setText(_translate("MainWindow", "Path:"))
#         self.toolButton_4.setText(_translate("MainWindow", "Select Image"))
#         self.label_16.setText(_translate("MainWindow", "The number of ICTs to be generated:"))
#         
#         self.toolButton_2.clicked.connect(self.openFile2)
#         self.toolButton_3.clicked.connect(self.openFile3)
#         self.toolButton_4.clicked.connect(self.openFile4)
#         self.pushButton.clicked.connect(self.Registration)
# =============================================================================
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 480, 180, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 21))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 205, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 275, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(125, 30, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 35, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 175, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(125, 275, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 380, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 410, 89, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 350, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 440, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(290, 270, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 65, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 101, 21))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 440, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 65, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 125, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 130, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(125, 95, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(80, 379, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 380, 51, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 240, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 240, 51, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IACT/ICT Generation"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Input two CT images (In Analyze 7.5 format)</span></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "Equal amplitude"))
        self.radioButton_2.setText(_translate("MainWindow", "Customized"))
        self.toolButton_2.setText(_translate("MainWindow", "Select Image"))
        self.label_2.setText(_translate("MainWindow", "End-expiration:"))
        self.label_6.setText(_translate("MainWindow", "Path:"))
        self.label_8.setText(_translate("MainWindow", "Interpolation method"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">motion curve (.xlsx file)</span></p></body></html>"))
        self.radioButton_3.setText(_translate("MainWindow", "ICT"))
        self.radioButton_4.setText(_translate("MainWindow", "IACT"))
        self.label_10.setText(_translate("MainWindow", "Output"))
        self.label_11.setText(_translate("MainWindow", "Output images saved at"))
        self.toolButton_3.setText(_translate("MainWindow", "Select File"))
        self.label_12.setText(_translate("MainWindow", "C:Users/user/Desktop/Result"))
        self.label_13.setText(_translate("MainWindow", "Path:"))
        self.label_14.setText(_translate("MainWindow", "End-expiration:"))
        self.label_15.setText(_translate("MainWindow", "Path:"))
        self.toolButton_4.setText(_translate("MainWindow", "Select Image"))
        self.label_16.setText(_translate("MainWindow", "The number of ICTs to be generated:"))
        self.radioButton_5.setText(_translate("MainWindow", "Empirical  n="))
        
        self.toolButton_2.clicked.connect(self.openFile2)
        self.toolButton_3.clicked.connect(self.openFile3)
        self.toolButton_4.clicked.connect(self.openFile4)
        self.pushButton.clicked.connect(self.Registration)


    def openFile2(self):
        self.fileName2 = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Select Image',
            QtCore.QDir.currentPath(),
            'all files (*.*)'
            )
        print(self.fileName2[0])
        self.label_3.setText(self.fileName2[0])
        self.flag = 1
        
    def openFile3(self):
        self.fileName3 = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Select File',
            QtCore.QDir.currentPath(),
            'all files (*.*)'
            )
        self.flag = 1
        
    def openFile4(self):
        self.fileName4 = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Select Image',
            QtCore.QDir.currentPath(),
            'all files (*.*)'
            )
        print(self.fileName4[0])
        self.label_5.setText(self.fileName4[0])
        self.flag = 1
     
        
    
        
    def Registration(self):
       #Deformation 
       os.system('C:\Users\user\Desktop\elastix_windows64_v4.8\elastix.exe -f '+self.fileName2[0] +' -m ' +self.fileName4[0] +' -out '+ current_path +'\Result'+'\ -p '+current_path+'\Result\WB_SPECT_affine.txt -p '+current_path+'\Result\WB_SPECT_bs.txt')
       #Generate motion vector
       os.system('C:\Users\user\Desktop\elastix_windows64_v4.8\\transformix.exe -def all -tp '+ current_path+'\Result\\TransformParameters.1.txt'+' -out '+ current_path +'\Result')
        
       n=(self.textEdit_2.text())#read the number of ICT
       m=int(n, base=10)     
       k=0  
       aList=[]
       t = 1
       for t in range(1,m+1):
# =============================================================================
#             #Equal time
#             z=-2*math.cos(3.14*t/(2*m))**4
#             weighting_factor=(2+z)/2
# =============================================================================
           #Equal amp
            tt=float(t)
            weighting_factor=tt/m
            aList.append(weighting_factor)
            k=k+1
            t=t+1
       else:
            print aList #weighting factor
            
            
       # Motion vector to array
       defm_v= current_path +'\Result\deformationField.img'
       f = open(defm_v, 'rb')  # reopen the file
       nImages =47*3
       height =128
       width = 128
       I = np.fromfile(f,dtype='f4',count=nImages*height*width)
       f.close()
       data = np.array(I, np.float)
       data = np.reshape(data, (nImages, height*width))


        #Interpolation
       for ict in range(1,m+1):
             temp = aList[ict-1]*data
             defm_ict= current_path +'\Result\deformationField.img' 
             rawfile = open(defm_ict,'wb')
             a = array.array('f')             
             for o in temp :
                 a.fromlist(list(o))               
             a.tofile(rawfile)
             rawfile.close()
             
             #Image warping
             os.system('C:\Users\user\Desktop\elastix_windows64_v4.8\\transformix.exe -in '+'C:\Users\user\Desktop\Result\hct_in_n.hdr' + ' -out '+ current_path +'\Result' + ' -tp '+ current_path+'\Result\\TransformParameters.txt')
           
             #rename ICT
             os.rename('C:\\Users\\user\\Desktop\\Result\\result.hdr', 'C:\\Users\\user\\Desktop\\Result\\result_'+str(ict)+'.hdr')
             os.rename('C:\\Users\\user\\Desktop\\Result\\result.img', 'C:\\Users\\user\\Desktop\\Result\\result_'+str(ict)+'.img')
            
       
   

        # Generate IACT
       defm_v= current_path +'\\Result\\hct_ex_ict.img'            
       f = open(defm_v, 'rb')
       nImages =47
       height =128
       width = 128
       Iex = np.fromfile(f,dtype='f4',count=nImages*height*width)

       defm_v= current_path +'\\Result\\hct_in_ict.img'            
       f = open(defm_v, 'rb')
       nImages =47
       height =128
       width = 128
       Iin = np.fromfile(f,dtype='f4',count=nImages*height*width)
  
       ICT=[]
       ICT.append(Iin)
       for ict in range(1,m+1):
           defm_v= current_path +'\\Result\\result_'+str(ict)+'.img'            
           f = open(defm_v, 'rb')
           nImages =47
           height =128
           width = 128
           
           I= np.fromfile(f,dtype='f4',count=nImages*height*width)
           ICT.append(I)
       ICT.append(Iex)
        
       
       
       IACT=np.empty_like(Iin)
       for t in range(1,m+1):
          IACT+=ICT[t-1]          
       IACT1=IACT/(m+2)

       #Plot HCT-IN, ICT and HCT-EX
       nImages =47
       height =128
       width = 128
    
       dataa = np.array(IACT1, np.float)
       dataa = np.reshape(dataa, (nImages, height*width))
       temp = dataa
       defm_ict= current_path +'\Result\iact.img' 

       rawfile = open(defm_ict,'wb')
       a = array.array('f')             
       for o in temp :
            a.fromlist(list(o))            
       a.tofile(rawfile)
       rawfile.close()
             
       ictfigure=[]
       for t in range(1,m+3):

           data=np.array([ICT[t-1]])
           b =np.reshape(data,(47,128,128))
           s79=b[:,79,:]#show Slice 79
           news79=np.flipud(s79)
           ictfigure.append(news79)
           
       print 'Please wait for over 10 seconds, then close the interface and you can see the figure'     
       fig = plt.figure()    
       for t in range(1,m+3):
           
           fig.add_subplot(120+(10*m)+t)
           plt.imshow(ictfigure[t-1],cmap = plt.cm.gray)
           plt.axis('off')
           plt.hlines(15, 0, 127, colors = "c")
           
 
       
           
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec_())
    
                               
