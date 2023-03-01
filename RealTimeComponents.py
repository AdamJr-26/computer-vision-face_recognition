# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:53:06 2023

@author: Adam
"""
import sys
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QImage , QPixmap,  QPalette,QColor, QFont, QIcon
from PyQt5.QtWidgets import  QScrollArea, QListWidget ,QListWidgetItem,  QMainWindow, QApplication,QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QDialog, QGroupBox, QLabel, QHBoxLayout, QGridLayout, QFormLayout
import stylesheet 
import json
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Components:
    def __init__(self):
        pass
        
    def captureLayout(self):
        capture_label = QLabel() # Create a label for the video capture
        
        capture_label.setStyleSheet(stylesheet.video_capture_label)
        # capture_label.setPixmap(QPixmap.fromImage(self.current_image))
        
        return capture_label
    def logItems(self):
        print("hello world")
        return QWidget()
    def registerFaceInput(self, image_label):
        image_input_layout = QHBoxLayout()
        image_input_layout.setSpacing(5)
        image_input_buttons_widget = QWidget()
        
        
        image_label.setStyleSheet(stylesheet.register_face_image_label)
        input_and_label_widget = QWidget()
        input_layout= QVBoxLayout() #layout
        input_label = QLabel("Name") #label
        input_label.setStyleSheet(stylesheet.register_log_label)
        self.register_text_input = QLineEdit() # input
        self.register_text_input.textChanged.connect(self.register_name_onTextChange)
        self.register_text_input.setStyleSheet(stylesheet.register_input_field)
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.register_text_input)
        input_and_label_widget.setLayout(input_layout)
        
        # confirm cancel buttons
        cancel_confirm_widget = QWidget()
        cancel_confirm_layout =QHBoxLayout()
        cancel_confirm_layout.setSpacing(1)
        cancel_confirm_layout.setAlignment(Qt.AlignBottom )
        cancel_button = QPushButton()
        cancel_button.setStyleSheet(stylesheet.register_buttons)
        confirm_button = QPushButton()
        confirm_icon = QIcon("./assets/icon/confirm_icon.png")
        cancel_icon = QIcon("./assets/icon/cancel_icon.png")
        cancel_button.setIcon(cancel_icon)
        confirm_button.setIcon(confirm_icon)
        cancel_button.setIconSize(QSize(50, 50))
        confirm_button.setIconSize(QSize(50, 50))
        cancel_confirm_layout.addWidget(cancel_button, 1)
        cancel_confirm_layout.addWidget(confirm_button,1)
        cancel_confirm_widget.setLayout(cancel_confirm_layout)
        
        image_input_layout.addWidget(image_label ,1)
        image_input_layout.addWidget(input_and_label_widget ,2)
        image_input_layout.addWidget(cancel_confirm_widget, 1)
        image_input_buttons_widget.setLayout(image_input_layout)
        # connnect buttons
        confirm_button.clicked.connect(self.submitRegistration)
        cancel_button.clicked.connect(self.resetRegisrationFrom)
        
        return image_input_buttons_widget
    
    def logItem(self, name, image, date_time):
        log_widget = QWidget()
        
        image_label_widget = QWidget() #widget
        image_name_layout = QHBoxLayout()
        image_name_layout.setContentsMargins(0,0,0,0)
        image_label = QLabel()
        image_label.setFixedSize(90, 70)
        image_pixma = QPixmap("../assets/images/robot.png")
        scaled_image_pixma = image_pixma.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_image_pixma)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet(stylesheet.log_item_image_label)
        name_label = QLabel(f"Name: {name}")
        name_label.setStyleSheet(stylesheet.name_label)
        image_name_layout.addWidget(image_label, 0)
        image_name_layout.addWidget(name_label, 1)
        image_label_widget.setLayout(image_name_layout)
        
        date_icon_widget = QWidget() #widget
        date_label = QLabel(date_time)
        if name == "Unknown":
            icon_pixma = QPixmap("./assets/icon/danger_icon.png")
        else :
            icon_pixma = QPixmap("./assets/icon/secure_icon.png")
        icon_label = QLabel()
        icon_label.setPixmap(icon_pixma)
        date_label.setStyleSheet(stylesheet.date_label)
        date_label.setStyleSheet(stylesheet.icon_label)
        date_icon_layout  = QHBoxLayout()

        date_icon_layout.addWidget(date_label, 1)
        date_icon_layout.addWidget(icon_label, 0)
        date_icon_widget.setLayout(date_icon_layout)
        
        image_name_date_icon_layout = QHBoxLayout()
        image_name_date_icon_layout.addWidget(image_label_widget, 2)
        image_name_date_icon_layout.addWidget(date_icon_widget, 0)
        image_name_date_icon_layout.setContentsMargins(0,0,0,0)
        
        log_widget.setLayout(image_name_date_icon_layout)
        log_widget.setFixedWidth(500)
        log_widget.setStyleSheet(stylesheet.log_item)
        return log_widget
    
    def cameraButton(self, widget):
        print("widget.width()", widget.width())
        button = QPushButton('', widget)
        button_icon = QIcon("./assets/icon/camera_icon.png")
        button.setIcon(button_icon)
        button.setIconSize(QSize(50, 50))
        button.setGeometry(500,410 , 50 ,50)
        button.clicked.connect(self.takeShot)
        return button 