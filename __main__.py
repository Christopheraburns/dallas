import sys
import computervision as vision
import computerspeech as speech


def main(init):
    debug = False

    try:

        if len(sys.argv) > 1:
            check = str(sys.argv[1]).lower()
            if (check == "true"):
                debug = True
            else:
                print("invalid parameter")

        # Take a picture
        vision.Vision.takeSinglePicture(debug)

        # Send to rekognition image-to-text service
        result = vision.Vision.imageToText(debug)

        # Send result to Polly
        speech.pollySays(result, debug)

    except Exception as e:
        print("Error in def main(): ".format(e))


if __name__ =="__main__":
    main(True)