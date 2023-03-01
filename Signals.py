# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:17:55 2023

@author: Adam
"""
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

class Signals(QObject):
    data_changed = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self._data = ''
        
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.data_changed.emit(self._data)
        self.data_changed.emit(self._data)
    
    

# class MyData(QObject):
#     data_changed = pyqtSignal(str)

#     def __init__(self):
#         super().__init__()
#         self._data = ''

#     @property
#     def data(self):
#         return self._data

#     @data.setter
#     def data(self, value):
#         self._data = value
#         self.data_changed.emit(self._data)

# app = QApplication([])
# window = QWidget()

# layout = QVBoxLayout(window)

# label = QLabel('Initial data', window)
# layout.addWidget(label)

# my_data = MyData()

# # Define a slot that updates the label with the new data
# def update_label(data):
#     label.setText(data)

# # Connect the data_changed signal of the MyData object to the update_label slot
# my_data.data_changed.connect(update_label)

# # Change the data of the MyData object
# my_data.data = 'New data'

# window.setGeometry(100, 100, 250, 100)
# window.setWindowTitle('Dynamic Label Example')
# window.show()

# app.exec_()