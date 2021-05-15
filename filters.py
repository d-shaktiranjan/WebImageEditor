import cv2 as cv
import numpy as np


def makeGray(name):
    img = cv.imread(f"static/temp/{name}", 0)
    newName = f"Gray_{name}"
    cv.imwrite(f"static/temp/{newName}", img)
    return newName


def makeRed(name):
    img = cv.imread(f"static/temp/{name}", cv.IMREAD_UNCHANGED)
    newName = f"Red_{name}"
    red_channel = img[:, :, 2]
    red_img = np.zeros(img.shape)
    red_img[:, :, 2] = red_channel
    cv.imwrite(f"static/temp/{newName}", red_img)
    return newName
