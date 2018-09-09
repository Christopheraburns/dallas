import sys
import computervision as vision
import computerspeech as speech


def main(init):
    debug = False

    try:

        if len(sys.argv) > 1:
            check = sys.argv[1]
            if (check is not True) or (check is not False):
                print("invalid parameter")
            else:
                debug = sys.argv[1]

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