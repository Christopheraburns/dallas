import pygame
import pygame.camera
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from random import *

# Create an AWS Client Obj
session = Session(profile_name="default")
rekognition = session.client("rekognition")


class Vision(object):

    @staticmethod
    def callRekognition():
        try:
            print("do something here")
        except(BotoCoreError, ClientError) as e:
            print("error: {}".format(e))


    @staticmethod
    def takeSinglePicture(debug):
        try:
            pygame.camera.init()
            # hardcode to the WebCam for the Dallas demo
            cam = pygame.camera.Camera("/dev/video0", (640, 480))
            cam.start()
            img = cam.get_image()
            pygame.image.save(img, "capture.png")
            cam.stop()
            if debug == True:
                print("image saved to capture.png")
        except Exception as e:
            print("error in ComputerVision.Vision.takeSinglePicture(): {}".format(e))


    @staticmethod
    def imageToText(debug):
        phraseBuilder = ""
        try:
            with open("capture.png", "rb") as imagefile:
                response = rekognition.detect_text(Image={'Bytes': imagefile.read()})


            if(debug == True):
                print("Reko imagetoText result: {}".format(response))

            if len(response["TextDetections"]) > 0:
                for detectedText in response["TextDetections"]:
                    if(detectedText['Type'] == 'WORD'):
                        phraseBuilder = phraseBuilder + " " + detectedText['DetectedText']

                phraseBuilder = "I believe it says, " + phraseBuilder + ". Is that correct?"
            else:
                phrases = ["Sorry, I don't see any readable text",
                           "I can't seem to read anything",
                           "I don't see anything to read",
                           "Is the light bad in here? I don't see any text"
                           ]
                select = randint(0, 3)
                phraseBuilder = phrases[select]

            if debug == True:
                print("Voice output should be: {}".format(phraseBuilder))

            return phraseBuilder
        except Exception as e:
            print("error in computervision.Vision.imageToText: {}".format(e))