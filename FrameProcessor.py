# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:54:08 2023

@author: Adam
"""
import cv2
from PyQt5.QtCore import QThread, QTimer, pyqtSignal

class FrameProcessor(QThread):
    frame_processed = pyqtSignal(object, object)

    def __init__(self, cap):
        super().__init__()
        self.cap = cap

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                # Process the frame using the detectFaces and recognizeFaces functions
                self.detectFaces(frame)
                processed_frame = self.recognizeFaces(frame)

                # Emit a signal with the processed frame and detected faces to update the UI
                self.frame_processed.emit(processed_frame, self.detected_unknown_faces_locations, self.detected_names)

    def detectFaces(self, frame):
        # Code to detect faces and store the locations in self.detected_unknown_faces_locations
        pass

    def recognizeFaces(self, frame):
        # Code to recognize faces and store the names in self.detected_names
        # Code to draw rectangles and names around the recognized faces on the frame
        processed_frame = frame.copy()
        if self.detected_unknown_faces_locations is not None and self.detected_names is not None:
            for (top, right, bottom, left), name in zip(self.detected_unknown_faces_locations, self.detected_names):
                cv2.rectangle(processed_frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(processed_frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        return processed_frame


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a timer to update the video frame
        self.timer = QTimer(self)
        self.timer.start(30)
        self.timer.timeout.connect(self.update_frame)

        # Create an instance of the FrameProcessor thread
        self.processor = FrameProcessor()
        self.processor.frame_processed.connect(self.show_processed_frame)
        self.processor.start()

    def update_frame(self):
        # This function will be called every 30ms to update the video frame in the UI
        # It doesn't need to do anything in this example because the processed frame
        # will be shown in the show_processed_frame function
        pass
    def show_processed_frame(self, processed_frame):
        # This function will be called when a new processed frame is available
        # It should update the UI to display the processed frame
        # For example:
        # Convert the processed frame to a QPixmap and show it in a QLabel
        pixmap = QPixmap.fromImage(QImage(processed_frame.data, processed_frame.shape[1], processed_frame.shape[0], QImage.Format_RGB888))
        self.label.setPixmap(pixmap)
