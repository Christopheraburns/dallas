import sys
import computervision as vision



def main(init):
    try:
        # Take a picture
        vision.Vision.takeSinglePicture()

        # Send to rekognition image-to-text service

        # Get result

        # Send result to Polly

        # Get result

        # Play audio file from Polly
    except Exception as e:
        print("Error in def main(): ".format(e))


if __name__ =="__main__":
    main(True)