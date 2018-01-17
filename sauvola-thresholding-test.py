# Sauvola, Otsu_Global, Niblack Binarization method is applied here. Sauvola works best for most of the images. 
# Usage : python sauvola-thresholding-test.py input.png output.png
# 



import sys, getopt

import matplotlib
import matplotlib.pyplot as plt

from skimage.io import imread, imsave, imshow
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)


matplotlib.rcParams['font.size'] = 9

def binarize(inputfile):
    image = imread(inputfile, as_grey = True)
    binary_global = image > threshold_otsu(image)

    window_size = 25
    thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
    thresh_sauvola = threshold_sauvola(image, window_size=window_size)

    binary_niblack = image > thresh_niblack
    binary_sauvola = image > thresh_sauvola

    # plt.figure(figsize=(8, 7))
    # plt.subplot(2, 2, 1)
    plt.figure(1)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.title('Original')
    plt.axis('off')
    plt.show()

    # plt.subplot(2, 2, 2)
    plt.figure()
    plt.title('Global Threshold')
    plt.imshow(binary_global, cmap=plt.cm.gray)
    plt.axis('off')
    plt.show()

    # plt.subplot(2, 2, 3)
    plt.figure(3)
    plt.imshow(binary_niblack, cmap=plt.cm.gray)
    plt.title('Niblack Threshold')
    plt.axis('off')
    plt.show()

    # plt.subplot(2, 2, 4)
    plt.figure(4)
    plt.imshow(binary_sauvola, cmap=plt.cm.gray)
    plt.title('Sauvola Threshold')
    plt.axis('off')
    plt.imsave(outputfile, binary_sauvola, cmap = plt.cm.gray)
    plt.show()


if len(sys.argv) != 3:
    print("python binarize_sauvola.py in_image out_image")
    sys.exit(1)

inputfile, outputfile = sys.argv[1:3]
binarize(inputfile)
