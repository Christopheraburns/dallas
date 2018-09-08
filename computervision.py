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
            cameras = pygame.camera.list_cameras()
            for camera in cameras:
                if camera:
                    cam = pygame.camera.Camera(camera(640, 480), "RGB")
                    cam.start()
                    img = cam.get_image()
                    pygame.image.save(img, "capture.png")
                    cam.stop()
                break
        except Exception as e:
            print("error in ComputerVision.Vision.takeSinglePicture(): {}".format(e))

