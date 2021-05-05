import cv2 as cv


def makeGray(fName):
    img = cv.imread(f"temp/{fName}", 0)
    cv.imwrite(f'temp/Gray_{fName}', img)
