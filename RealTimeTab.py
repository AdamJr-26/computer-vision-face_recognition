# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:17:37 2023

@author: Adam
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QDialog, QGroupBox, QLabel, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
import stylesheet
import cv2
import face_recognition
import numpy as np
from Signals import Signals
import threading
import os
import json
from datetime import datetime

import random
import string
from LoadRecentJsonFile import LoadRecentJsonFile
from QListWidgetComponent import QListWidgetComponent
class RealTimeTab():
    
    def __init__(self):
        
        pass
    
    def videoCaptureVoiceVisualizer(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        self.capture_label = QLabel(self) # Create a label for the video capture
        self.capture_label.setStyleSheet(stylesheet.video_capture_label)
        self.cameraButton(self.capture_label)
        layout.addWidget(self.capture_label, 3) # video capture
        qlabel = QLabel("voice")
        qlabel.setStyleSheet("""QLabel {border: 2px solid #D4CECE;
                             border-radius: 10px; }
                                                       """)
        layout.addWidget(qlabel, 1) # voice visualizer
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    def logsAndNewPersonRegister(self):
        self.log_person_register_layout = QVBoxLayout()
        self.log_person_register_layout.setSpacing(15)
        self.image_label = QLabel("")
        self.log_list_widget = LoadRecentJsonFile() # instantiate QListWidget
        self.log_person_register_layout.addWidget(QListWidgetComponent(), 3) # logs
        self.log_person_register_layout.addWidget(self.registerFaceInput(self.image_label), 1) # input name
        widget = QWidget()
        widget.setLayout(self.log_person_register_layout)
        self.log_list_widget.data_loaded.connect(self.log_list_widget.update)
        return widget
    
    def realTimeLayout(self):
        layout =QHBoxLayout()
        layout.addWidget(self.videoCaptureVoiceVisualizer(), 1)
        layout.addWidget(self.logsAndNewPersonRegister(), 1)
        return layout
    
               
    # display frame, ito yung tatawagin ng connect if signal emitted.
    def update_frame(self, frame):
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
        self.capture_label.setPixmap(QPixmap.fromImage(image))

            
    
    # process fame, ito mag eemit ng signal also start ng thread.
    def processFrame(self):
        ret, frame = self.cap.read()
        if ret:
            print("hello i am running...")
            self.current_frame = cv2.resize(frame, (200, int(frame.shape[0] * 200 / frame.shape[1])))
            cv2.resize(frame, (100, int(frame.shape[0] * 100 / frame.shape[1])))
            
            modified_frame, names, faces_locations, face_encodings = self.recognizeFaces(frame)
        
        # self.frame_processed.emit(modified_frame, names, faces_locations)
        
        # image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
        # self.capture_label.setPixmap(QPixmap.fromImage(image))
        
        
        # detect faces and store to the main variables
        # recognize faces and names and stoe to the variables.
        
    def registerPerson(self, name, person_image):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you want to continue?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = msg.exec()  
        
        if response == QMessageBox.Yes:
            # Check if the data file exists and load its contents
            if os.path.exists("./data/database/db.json"):
                with open("./data/database/db.json", "r") as f:
                    data = json.load(f)
            else:
                print("json did found.")
            # reset text input.
            self.removeInputFromTextAndImage()
            # Get the name and path of the image to save
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            folder_path = "./data/images/registered"
            file_path = f" {name}_{random_string}.jpg"
            # Save the image
            file_name = os.path.join(folder_path,file_path)
            cv2.imwrite(file_name, person_image)      
            # Add the image to the data file
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["registered"].append({
                "name": name,
                "image_file_directory": file_name,
                "date_of_registered": now
            })
            data["total_registered"] += 1
            
            # Save the updated data file
            with open("./data/database/db.json", "w") as f:
                json.dump(data, f, indent=4)
            
        elif response == QMessageBox.No:
            print("User clicked No.")              
            
    def takeShot(self):
        
        if self.current_frame is None or len(self.detected_unknown_faces_locations) <= 0:
            return 
        faces = self.detected_unknown_faces_locations
        if len(faces):
            print("took a shot")
            # get first detected in frame
            x, y, w, h = faces[0]
            # crop image
            # face_image = self.current_frame[y:y+h, x:x+w]
            face_image = self.current_frame
            # resize image
            
            # check if the image is already registered.
            
            face_image = cv2.resize(face_image, (640, 480))
            
            self.register_image = face_image
            qimage = QImage(face_image, face_image.shape[1], face_image.shape[0], QImage.Format_RGB888).rgbSwapped()
            
            if not qimage.isNull():
                # add image
                shot = Signals()
                shot.data_changed.connect(self.updateRegisterImageLabel)
                shot.data = qimage
                        
    def removeInputFromTextAndImage(self):
            # reset text input.
            self.register_text_input.setText(None)
            self.image_label.setPixmap(QPixmap())
            
    def updateRegisterImageLabel(self, data):
        # update qlabel. 
        pixmap = QPixmap.fromImage(data)
        scaled_pixmap = pixmap.scaled(self.image_label.width() + 50, self.image_label.height(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        