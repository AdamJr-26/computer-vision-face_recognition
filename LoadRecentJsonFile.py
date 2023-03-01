# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:38:06 2023

@author: Adam
"""

import json
import os
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtCore import pyqtSignal, QObject

class LoadRecentJsonFile(QListWidget, QObject):
    data_loaded = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.json_file = "./data/database/recent.json"
        self.load_data()

        # start file system event handler to watch for changes in the JSON file
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_modified = self.on_file_modified
        self.observer = Observer()
        self.observer.schedule(self.event_handler, os.path.dirname(self.json_file), recursive=False)
        self.observer.start()

    def load_data(self):
        with open(self.json_file, 'r') as f:
            data = json.load(f)

        self.clear()
        for item in data["recent_detected"]:
            print("printing recent item realtime: ", item)
            list_item = QListWidgetItem(item['date_time'])
            list_item.setToolTip(item.get('tooltip', ''))
            self.addItem(list_item)

        self.data_loaded.emit()

    def on_file_modified(self, event):
        if event.src_path == self.json_file:
            print("checking modified json")
            self.load_data()

    def closeEvent(self, event):
        self.observer.stop()
        self.observer.join()
        super().closeEvent(event)
        
        
# if __name__ == '__main__':
#     app = QApplication([])
#     widget = MyWidget()
#     widget.show()
#     app.exec_()
