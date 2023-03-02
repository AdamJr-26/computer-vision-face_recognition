# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:54:08 2023

@author: Adam
"""
from PyQt5.QtCore import QObject, pyqtSignal
import cv2

class Worker(QObject):
    frame_processed = pyqtSignal()

    def __init__(self, main_window, cap):
        super().__init__()
        self.main_window = main_window
        self.cap = cap

    def run(self):
        
        while True:
            ret, frame = self.cap.read()
            if ret:
                current_frame = cv2.resize(frame, (200, int(frame.shape[0] * 200 / frame.shape[1])))
                modified_frame, names, faces_locations, face_encodings = self.main_window.recognizeFaces(frame)
                self.frame_processed.emit()