from instagrapi import Client
from config import *
import os, datetime, time, getpass

class session():
    def __init__(self):
        self.caminhoPasta = selectedFolder
        self.cl = Client()
        user = input("Username:")
        pw = getpass.getpass("password:")  
        self.cl.login(user, pw)

    
    def changeAcc(self):
        del self.cl
        self.cl = Client()
        user = input("Username: ")
        pw = getpass.getpass("password: ")
        self.cl.login(user, pw)
    
    #select image
    def SeekImage(self):
        while True:
            self.imagemNome = input("input image name (only jpg, without file extension):")
            caminhoFinal = self.caminhoPasta + self.imagemNome +".jpg"
            if os.path.isfile(caminhoFinal):
                return caminhoFinal
            else:
                print("ERROR: {}.jpg not found, check the file name".format(self.imagemNome))
    
    #post
    def postBuilder(self):
        image = self.SeekImage()
        caption = input("enter caption for media: ")
        questionLike = input("disable visible like count?  y/n: ").upper()
        while True:
            if questionLike == 'Y':
                likeBool = 1
                break
            if questionLike == 'N':
                likeBool = 0
                break
            print("invalid input!") 
        
        self.mediaObject = [image, caption, likeBool]
        return self.mediaObject
        
    def imageUpload(self, features):
        self.cl.photo_upload(
            features[0],
            features[1],
            extra_data={
            "like_and_view_counts_disabled": features[2]
            }
        )
        print("The selected image has been submitted")
    
    #schedule post
    def SchedulePost(self, features):
        scheduleTime = input("Digite a data e hora no formato 'AAAA-MM-DD HH:MM': ")
        scheduleTime = datetime.datetime.strptime(scheduleTime, '%Y-%m-%d %H:%M')

        while True:
            # check the current time
            data_hora_atual = datetime.datetime.now()

            # comparing current date and time w the user input 
            if data_hora_atual >= scheduleTime:
                self.imageUpload(features)
                break
            
            # waiting a sec before to try again
            time.sleep(1)