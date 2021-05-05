import cv2 as cv


def makeGray(fName):
    img = cv.imread(fName, 0)
    cv.imwrite(f'temp/{fName}_gray', img)
