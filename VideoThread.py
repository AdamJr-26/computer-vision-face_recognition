# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:42:57 2023

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

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if ret:
                self.change_pixmap_signal.emit(frame)
                
    def stop(self):
        self.terminate()