# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:37:07 2023

@author: Adam
"""

import cv2
from PyQt5.QtCore import QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import numpy as np
import face_recognition
import threading

class ProcessFrame(QThread):
    changed_frame = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if ret:
                self.changed_frame.emit(frame)
                
    def stop(self):
        self.terminate()