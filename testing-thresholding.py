import cv2
import numpy as np
import os
import argparse
from PIL import Image

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image for thresholding")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])

grayscaled=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original',image)
cv2.imshow('Adaptive threshold',th)

filename = "{}.png".format(os.getpid())
path = "/home/mottakin/tesseract-ocr/tesseract-testing/output/"
name = os.path.join(path,filename)
cv2.imwrite(name, th)

cv2.waitKey(0)
cv2.destroyAllWindows()