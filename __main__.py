import sys
import computervision as vision
import computerspeech as speech



def main(init):
    try:

        # Take a picture
        vision.Vision.takeSinglePicture()

        # Send to rekognition image-to-text service
        result = vision.Vision.imageToText()

        # Send result to Polly
        speech.pollySays(result)

    except Exception as e:
        print("Error in def main(): ".format(e))


if __name__ =="__main__":
    main(True)