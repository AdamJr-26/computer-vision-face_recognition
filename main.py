# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:16:01 2023

@author: Adam
"""

import sys
import cv2
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import  QMainWindow,QListWidgetItem, QListWidget,QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QDialog, QGroupBox, QLabel, QHBoxLayout, QGridLayout, QFormLayout
from Tabs import Tabs
from RealTimeTab import RealTimeTab
from RealTimeComponents import Components 
import json
import os
from FaceRecognizer import FaceRecognizer
import numpy as np
from VideoThread import VideoThread
from ProcessFrame import ProcessFrame
import threading
class Main(QMainWindow, Tabs, FaceRecognizer ):
    faces_ignal_detection = pyqtSignal(str)
    body_ignal_detection = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.cap = cv2.VideoCapture(0) 
        
        
        self.list_detected_images = [] # max len is 20
        self.known_images = []
        self.known_face_names = []
        self.known_images_paths = []
        self.detected_unknown_faces_locations = [] # faces in current frame
        self.unknown_face_encodings = [] 
        self.known_face_encodings = [] # infinite.
        self.detected_names = None
        self.current_frame = None
        
        self.shot_face = None
        
        self.current_detected_face = None
        
        
        # log items
        self.log_data = []
        self.thread = QThread()
        
        # Create a timer to update the video frame
        self.timer = QTimer(self)
        self.timer.start(60)
        self.timer.timeout.connect(self.update_frame)
        
        # self.processFrameThread()
        self.thread = threading.Thread(target=self.processFrameThread)
        self.thread.daemon = True 
        self.thread.start()
        
        # methods
        # self.getImages() #get all images and supply to self.known_images
        self.getFaceEncodings() # encode all known images

        # from: name: image
        self.register_name = None
        self.register_image = None
        
        # databases
        self.db_json  = "./data/database/db.json"
        self.recent_json = "./data/database/recent.json"

        
    def updateFaceDetectionIcon(self,icon_path):
        pass
    
    def submitRegistration(self):
        if self.register_name is None and self.register_image is None:
            return
        self.registerPerson(self.register_name,self.register_image )
        self.getFaceEncodings()
        self.register_name = None
        self.register_image = None
        
    def resetRegisrationFrom(self):
        self.removeInputFromTextAndImage()
    def register_name_onTextChange(self, text):
        print("text", text)
        self.register_name = text;
    def clearRegisterNameInput(self):
        pass
    
    # def closeEvent(self):
    #     if cv2.waitKey(1) == ord('q'):
    #         self.cap.release()
            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

