from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
import os
import pygame.mixer
from contextlib import closing
import time

session = Session(profile_name="default")
polly = session.client("polly")



def pollySays(value, debug):
    try:
        response = polly.synthesize_speech(Text=value, OutputFormat="ogg_vorbis", VoiceId="Emma")
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join("speech.ogg")

                with open(output,"wb") as file:
                    file.write(stream.read())

            pygame.mixer.init()
            pygame.mixer.music.load('speech.ogg')
            pygame.mixer.music.play()
            time.sleep(3)

    except(BotoCoreError, ClientError) as e:
        print("Error: computerspeech.py -> PollySays: {}".format(e))
