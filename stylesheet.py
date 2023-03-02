# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:52:53 2023

@author: Adam
"""

main_window =  """
    background-color: #02111B;
    """
video_capture_label = """
    QLabel {
            background-color: #3F4045;
            border-radius: 10px;
            padding: 15px;
            width:100%;
            min-width: 120px;
            
            ;}
     """
     
  # logItem
image_label = """
        QLabel {
            min-height: 60px;
            min-width: 80px;
            max-height: 60px;
            max-width: 80px;
            background-color:gray;
            border-radius:10px;
            margin: 0px;
            padding:0px}
    """
name_label = """
    QLabel {
            font-weight: 500;
            color:white;
            font-size: 14px;
            margin-left: 2px;
            }
 """
date_label = """
    QLabel {
            color:white;
            margin: 0;
            text-align:right;
            }
     """ 
icon_label = """
     QLabel {
             color:white;
             margin-left: 5px;
             }
      """ 
      
log_item = """
    QWidget {
        background-color: #3F4045;
        border-radius: 10px;
        margin: 0px;
        padding: 10px;
        max-height: 80px;

        }"""
    
# logsLayout
logs_layout_scroll_area = """
border: none;
"""
image_input_label = """
QLabel {
    min-height: 60px;
    min-width: 60px;
    background-color:gray;
    border-radius:10px;
    margin: 0;}
"""
log_item_image_label = """
    QLabel {
        
        background-color:gray;
        border-radius:10px;
        margin: 1px;
        padding:5px}

"""
log_q_list_widget_item = """
QListWidget::item { 
    background-color: #3F4045;
    min-height:80px; 
    border-radius:15px;
    
    }
"""
#registerFaceInput

register_face_image_label = """
QLabel {
        min-height: 80px;
        min-width: 80px;
        background-color:gray;
        border-radius:10px;
        margin: 0;}
        """
register_input_field = """
QLineEdit {
    background-color: white;
    height: 45px;
    width: 100%;
    border-radius: 10px;
    font-weight: 500;
    font-size: 16px;
    padding: 2px;
    }
"""



image_input_buttons_widget = """
QWidget {
    padding: 10px;
    }
"""
register_buttons = """
QPushButton {
    height: 45px;
    width: 45px;
    }
"""

register_log_label = """
QLabel {
        color: white;
        font-weight: 500;
        font-size: 16px;
        }
"""

# FACE DETECTION ICONS

detection_widget_wrapper = """
 .detection-widget-wrapper {
    border: 2px solid #D4CECE;
                         border-radius: 10px;
    }
 .detection-text-label {
     color: white;
     font-weight: 500;
     margin: 0px auto;
     }
 .icons-label-detection-layout {
     display: flex;
     justify-content: center;
     }
 .icon-label {
     margin: 0px auto;
     }
 
"""

__all__ = ['main_window',
           'detection_widget_wrapper',
           'video_capture_label', 
           'image_label',
           'name_label',
          'date_label',
          'icon_label', 
          'log_item',
          'logs_layout_scroll_area', 
         'image_input_label', 
         'register_face_image_label',
         'register_input_field',
         'image_input_buttons_widget' ,
         'register_buttons',
         'register_log_label' ]