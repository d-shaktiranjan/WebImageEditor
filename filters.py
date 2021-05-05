import cv2 as cv


def makeGray(name):
    img = cv.imread(f"temp/{name}", 0)
    newName = f"Gray_{name}"
    cv.imwrite(f"temp/{newName}", img)
    return newName
