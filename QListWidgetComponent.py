# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:34:37 2023

@author: Adam
"""
import sys
import json
import os 
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget,QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QDialog, QGroupBox, QLabel, QHBoxLayout, QGridLayout, QFormLayout
import stylesheet

import stylesheet
class QListWidgetComponent(QListWidget):
    def __init__(self):
        super().__init__()
        # watch recent json file
        
        # Create a timer to check for JSON file changes
        self.update_recent_data_timer = QTimer()
        self.update_recent_data_timer.setInterval(5000)  # Check every 1 second
        self.update_recent_data_timer.timeout.connect(self.update_recent_data)
        self.update_recent_data_timer.start()
        self.setStyleSheet(stylesheet.log_item_image_label)
    # internal components
    def update_recent_data(self):
        # load data
        if os.path.exists("./data/database/recent.json"):
            with open("./data/database/recent.json", "r") as f:
                data = json.load(f)
            # self.recent_data = data['recent_detected']
        # Clear the QListWidget
        self.clear()
        # Add each item from the JSON file to the QListWidget
        if len(data['recent_detected']):
            for recent in data['recent_detected']:
                log_widget = QWidget()
                
                image_label_widget = QWidget() #widget
                image_name_layout = QHBoxLayout()
                image_name_layout.setContentsMargins(0,0,0,0)
                image_label = QLabel()
                image_label.setFixedSize(90, 70)
                image_pixma = QPixmap(recent['image'])
                scaled_image_pixma = image_pixma.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(scaled_image_pixma)
                image_label.setAlignment(Qt.AlignCenter)
                
                name_label = QLabel(f"Name: {recent['name']}")
                image_name_layout.addWidget(image_label, 0)
                image_name_layout.addWidget(name_label, 1)
                image_label_widget.setLayout(image_name_layout)
                
                date_icon_widget = QWidget() #widget
                date_label = QLabel(recent['date_time'])
                icon_pixma = QPixmap("./assets/icon/danger_icon.png")
                icon_label = QLabel("Icon")
                icon_label.setPixmap(icon_pixma)

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
                
                image_label.setStyleSheet(stylesheet.log_item_image_label)
                name_label.setStyleSheet(stylesheet.name_label)
                date_label.setStyleSheet(stylesheet.date_label)
                date_label.setStyleSheet(stylesheet.icon_label)
                log_widget.setStyleSheet(stylesheet.log_item)
                self.setStyleSheet(stylesheet.log_q_list_widget_item)
                self.setSpacing(10)
                list_item = QListWidgetItem()
                
                self.addItem(list_item)
                self.setItemWidget(list_item, log_widget) # set the custom widget as the content of the item

        
        
        # log_label = QLabel("Logs")
        # layout = QVBoxLayout(list_widget)
        # layout.setSpacing(15)
       
        # # update the layout
        # list_widget.setLayout(layout)
        # scroll_area = QScrollArea()
        # scroll_area.setStyleSheet(stylesheet.logs_layout_scroll_area)
        # scroll_area.setWidget(list_widget)
        # # scroll_area.setMaximumWidth(640)
        # return scroll_area