import cv2 as cv


def makeGray(name):
    img = cv.imread(f"static/temp/{name}", 0)
    newName = f"Gray_{name}"
    cv.imwrite(f"static/temp/{newName}", img)
    return newName
