# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:19:10 2023

@author: Adam
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget,QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTabWidget, QVBoxLayout, QDialog, QGroupBox, QLabel, QHBoxLayout, QGridLayout, QFormLayout
import stylesheet
from PyQt5.QtCore import Qt, QTimer
from RealTimeComponents import Components 
from RealTimeTab import RealTimeTab

class Tabs(Components,RealTimeTab ):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Wanna be AI")
        self.setFixedSize(1280, 720)
        self.setStyleSheet(stylesheet.main_window)
        self.setCentralWidget(self.showTabs())
        

       
       
    def realTimeWidget(self):
        realtime_widget = QWidget()
        # add style here.
        realtime_widget.setLayout(self.realTimeLayout())
        return realtime_widget
    def reports(self):
        return  QWidget()
    def threats(self):
        return  QWidget()
    
    def showTabs(self):
        tabs = QTabWidget()
        tabs.addTab(self.realTimeWidget(), "Realtime")
        tabs.addTab(self.reports(), "Registered")
        tabs.addTab(self.threats(), "Threats")
        tabs.setStyleSheet("QTabBar::tab {height: 40px;font:Karla; width: %dpx; background-color: #3F4045; font-weight: 500; color:white; }"
                           "QTabBar::tab:selected { background-color:#EAE6E6; color:black; }"
                           % (self.width() / tabs.count()))
        return tabs
        



