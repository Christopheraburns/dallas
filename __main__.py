import sys
import computervision as vision
import computerspeech as speech

debug = False

def main(init):
    try:

        if len(sys.argv) == 1:
            debug=sys.argv[1]


        # Take a picture
        vision.Vision.takeSinglePicture(False, debug)

        # Send to rekognition image-to-text service
        result = vision.Vision.imageToText(debug)

        # Send result to Polly
        speech.pollySays(result, debug)

    except Exception as e:
        print("Error in def main(): ".format(e))


if __name__ =="__main__":
    main(True)