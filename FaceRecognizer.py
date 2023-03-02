# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:38:38 2023

@author: Adam
"""

import os
from PIL import Image
import cv2
import face_recognition
import numpy as np
from Signals import Signals
import os
import json
from datetime import datetime
from PIL import Image
import random
import string
from datetime import datetime
from tts.TextToSpeech import TextToSpeech

class FaceRecognizer:
    def __init__(self):
        pass
        
    # load images from different folder or specified folder.
    def getImages(self):
        images = []
        names = []
        if os.path.exists("./data/database/db.json"):
            with open("./data/database/db.json", "r") as f:
                data = json.load(f)

        for registered in data["registered"]:            
            image = face_recognition.load_image_file(registered["image_file_directory"])
            images.append(image)
            names.append(registered["name"])
        self.known_images = images
        self.known_face_names = names
        return images
        
    def getFaceEncodings(self):
        if len(self.getImages()):
            for loaded_image in self.getImages():
                gray_frame = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
                face = face_recognition.face_locations(gray_frame)
                # face_recognition.face_encodings(loaded_image, face)
                if len(face_recognition.face_encodings(loaded_image, face)):
                    self.known_face_encodings.append(face_recognition.face_encodings(loaded_image, face)[0])
                        
    
    # draw reactangle on detected faces.
    def detectFaces(self, frame):
        print("self.detected_unknown_faces_locations", self.detected_unknown_faces_locations)
        print(" self.detected_names",  self.detected_names)
        if self.detected_unknown_faces_locations and self.detected_names:
            for (top, right, bottom, left), name in zip(self.detected_unknown_faces_locations, self.detected_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        return frame
        # print("I am running and recognizing the faces.")

    def recognizeFaces(self, modified_frame):
        # modified_frame = modified_frame.copy()
        
        # detect faces
        # size_frame = cv2.resize(modified_frame, (200, int(modified_frame.shape[0] * 200 / modified_frame.shape[1])))
        gray_frame = cv2.cvtColor(modified_frame, cv2.COLOR_BGR2GRAY)
        faces_locations = face_recognition.face_locations(gray_frame)
        face_encodings = face_recognition.face_encodings(np.array(modified_frame), np.array(faces_locations))
        
        if len(face_encodings) and len(faces_locations):
            self.detected_unknown_faces_locations = faces_locations
            self.unknown_face_encodings = face_encodings
            # update icons on widget
            
        else:
            self.detected_unknown_faces_locations = []
            self.unknown_face_encodings = []
            # update icons on widget


        # recognize faces
        names = []
        for encoding in self.unknown_face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, encoding)
            name = 'Unknown'
            if True in matches:
                idx = matches.index(True)
                name = self.known_face_names[idx]
                print("should know my name: ", name)
                # TTS
                # tts = TextToSpeech()
                # tts.getUserInput('greetings')
                # tts.getTextResponse()
                # tts.modifyText('person_name_to_replace', name)
                # tts.saveAudio()
                # tts.playAudio()
                # tts.stopAudio()
                self.addToLogItems(name, modified_frame)
                
            else:
                print("Am pretty sure you dont know me: ", name)
                self.addToLogItems(name, modified_frame)
                
                # print("self.log_items",self.log_items)

            names.append(name)
        self.detected_names = names

        return [ modified_frame, names, faces_locations, face_encodings ]
    
    def addToLogItems(self, name, image):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        folder_path = "./data/images/recent"
        file_path = f"{name}_{random_string}.jpg"
        
        # Save the image
        file_name = os.path.join(folder_path,file_path)
        cv2.imwrite(file_name, image)
       
        if os.path.exists(self.recent_json):
            with open(self.recent_json, "r") as f:
                data = json.load(f)
            
          
            # Sort the list of objects in recent_detected based on the date_time key
            data['recent_detected'] = sorted(data['recent_detected'], key=lambda x: datetime.fromisoformat(x['date_time']))
            
            # check if the face is in the current recent images if yes then do not add.
            # ----------------
            if self.checkRecentImagesAvoidSameFace(data['recent_detected'], image ):
                return
            
            # TTS
            # tts = TextToSpeech()
            # tts.getUserInput('uknown_detected')
            # tts.getTextResponse()
            # tts.saveAudio()
            # tts.playAudio()
            # tts.stopAudio()
            # Remove the oldest item from the list
            
            if len(data["recent_detected"]) >= 20 and os.path.exists(data['recent_detected'][0]["image"]):
                image_path_to_remove = data['recent_detected'][0]["image"]
                data['recent_detected'].pop(0)
                os.remove(image_path_to_remove)
                print("deleting item", image_path_to_remove)
            
            data["recent_detected"].append({
                "name": name,
                "image": file_name,
                "date_time": date_time
            })
    
            # Save the updated data file
            with open(self.recent_json, "w") as f:
                json.dump(data, f, indent=4)

    def checkRecentImagesAvoidSameFace(self, recent, new_image):
        # encodings
        isMatch = False
        recent_faces_encodings = []
        new_face_encoding = []
        if len(recent) and len(new_image):
            gray_frame = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
            new_face = face_recognition.face_locations(gray_frame)
            if len(new_face):
                
                new_face_encoding = face_recognition.face_encodings(np.array(new_image), np.array(new_face))[0]
                for image in recent:
                    # load the image.
                    load_recent_image =face_recognition.load_image_file(image["image"])
                    # convert
                    recent_gray_frame = cv2.cvtColor(load_recent_image, cv2.COLOR_BGR2GRAY)
                    # get the location
                    recent_face = face_recognition.face_locations(recent_gray_frame)
                    # add to new_faces_encoding list.      
                    if len(recent_face):
                        recent_faces_encodings.append(face_recognition.face_encodings(np.array(load_recent_image), np.array(recent_face))[0])
                
        if len(recent_faces_encodings):
            matches = face_recognition.compare_faces(recent_faces_encodings, new_face_encoding)
            # print("checkRecentImagesAvoidSameFace", matches)
            if matches != None:
                if True in matches:
                    print("Already in a recent")
                    isMatch = True
                else:
                    print("adding to recent")
                    isMatch = False
        return isMatch

        # compare with new face.
    def getFacesLocation(self):
        pass

    # load images
    # find all faces in frame
    # zoom in faces detected
    # convert the image to gray
    # draw rectangle for every faces
    # take a shot every 3 seconds and take a face encoding
    # compare it to existing endcoded images.
    # if matches then say Hi
    # else ask name
    # Release the capture and destroy windows
