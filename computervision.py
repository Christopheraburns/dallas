import pygame
import pygame.camera
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError


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
    def takeSinglePicture(detect_labels=False):
        try:
            pygame.camera.init()
            # hardcode to the WebCam for the Dallas demo
            cam = pygame.camera.Camera("/dev/video0", (640, 480))
            cam.start()
            img = cam.get_image()
            pygame.image.save(img, "capture.png")
            cam.stop()

        except Exception as e:
            print("error in ComputerVision.Vision.takeSinglePicture(): {}".format(e))

