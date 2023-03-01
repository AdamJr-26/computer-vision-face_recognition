# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 11:31:08 2023

@author: Adam
"""



from gtts import gTTS
import pygame
import os

import secrets
import string

class TextToSpeech:
    
    def __init__(self):
        self.file_path_mp3 =""
        self.file_name = ""
        self.text = ""
        self.file_name = ""
        self.text_file_path = ""
        
    def getUserInput(self, user_input_speech):
        if(user_input_speech == "who are you"):
            self.text_file_path = "./data/tts/text_files/who_am_i.txt"
        elif(user_input_speech == "uknown_detected"):
            self.text_file_path = "./data/tts/text_files/ask_name.txt"
        elif(user_input_speech == "repeat_asking_name"):
             self.text_file_path = "./data/tts/text_files/name_again.txt"
        elif(user_input_speech == "after_asking_name"):
            self.text_file_path = "./data/tts/text_files/thanking_after_gave_name.txt"
        elif(user_input_speech == "hey"):
            self.text_file_path = "./data/tts/text_files/whats_up.txt"
        elif(user_input_speech == "greetings"):
            self.text_file_path = "./data/tts/text_files/greetings.txt"
        elif(user_input_speech == "hi"):
            self.text_file_path = "./data/tts/text_files/hello.txt"
        else:
            self.text_file_path = "./data/tts/text_files/not_clear.txt"
            
    def getTextResponse(self):
        with open(self.text_file_path, "r") as file:
            self.text = file.read()
        #if os.path.exists(self.text_file_path):
        #    os.remove(self.text_file_path)
            
    def modifyText(self, text_to_replace, text_replacement):    
        # Use gTTS to generate speech from the text
        self.text = self.text.replace(text_to_replace, text_replacement)
    
    def saveAudio(self):
        # random string file name
        alphabet = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(alphabet) for i in range(10))
        self.file_path_mp3 = random_string    
        tts = gTTS(self.text)
        tts.save(random_string)
        
    def playAudio(self):
        # Initialize pygame and play the audio file
        if(self.file_path_mp3 != ""):
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path_mp3)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    def stopAudio(self):
        # Fade out and stop the audio playback
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        
    

