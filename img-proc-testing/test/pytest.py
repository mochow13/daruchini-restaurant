import cv2
import pytesseract
import numpy as np
from PIL import Image
import os

def ocrpy(img):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file

    text = pytesseract.image_to_string(Image.open(filename), lang='ben')
    os.remove(filename)

    # outfile = os.path.basename(args['image']).split('.')[0];
    out = open(filename+".txt",'a')

    # print(outfile);
    out.write(text+'\n')


image = cv2.imread("./images/unnamed.png",0)
cv2.imshow('orig',image)
cv2.waitKey(0)

original_image = image.copy()

gray = image

#grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
# cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('second',thresh)
cv2.waitKey(0)

#dilation
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)

#find contours
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

# Matra X positions 
matraY = []

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # matraY.append(y)

    # Getting 
    # Use Copy method if dont want to alter the original image
    # roi = image[y:y+h, x:x+w].copy()
    roi = image[y:y+h, x:x+w]
    cv2.imwrite("ok.png", roi)

    ocrpy("ok.png")

    # text = pytesseract.image_to_string(Image.open("ok.png"), lang='ben')
    # os.remove("filename")
    # outfile = os.path.basename(args['image']).split('.')[0];
    # out = open("")
    # print(outfile);
    # out = open("random"+".txt","a")
    # out.write(text+' ')

    # Remove MATRA from the words. Need Some modification for adaptive width of MATRA
    # for i in np.where(np.sum(roi,axis=1) == np.min(np.sum(roi, axis=1))):
    #     # i is a list of numbers. Taking the max of it to make it an int type and making adjacent rows to white
    #     roi[max(i)-2: max(i) + 2] = np.max(roi)
    #     # print(max(i))
    #     # roi[i] = np.max(roi)


    # Trying Something New | Inserting Extra Spaces where No dots under or above the matra
    # for k in np.where(np.sum(roi,axis=1) == np.min(np.sum(roi, axis=1))):
    #     k = max(k)
    #     for j in roi[k,:]:
    #         if np.any(roi[k+2 : k+h,j] < 100):
    #             roi[:,j] = 255

    # show ROI
    # cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
    # cv2.waitKey(0)

cv2.imshow('marked areas',image)
cv2.waitKey(0)











# #binary
# ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('second',thresh)
# cv2.waitKey(0)

# #dilation
# # kernel = np.ones((1,1), np.uint8)
# # img_dilation = cv2.dilate(thresh, kernel, iterations=1)
# # cv2.imshow('dilated',img_dilation)
# # cv2.waitKey(0)

# img_dilation = thresh

# #find contours
# im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #sort contours
# sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

# for i, ctr in enumerate(sorted_ctrs):
#     # Get bounding box
#     x, y, w, h = cv2.boundingRect(ctr)

#     # Getting 
#     # Use Copy method if dont want to alter the original image
#     # roi = image[y:y+h, x:x+w].copy()
#     roi = image[y:y+h, x:x+w]

#     original_image[y-6:y, x+w:x+w+3] = 255


#     # Remove MATRA from the words. Need Some modification for adaptive width of MATRA
#     # for i in np.where(np.sum(roi,axis=1) == np.min(np.sum(roi, axis=1))):
#     #     # i is a list of numbers. Taking the max of it to make it an int type and making adjacent rows to white
#     #     roi[max(i)-2: max(i) + 2] = np.max(roi)
#         # print(max(i))
#         # roi[i] = np.max(roi)

#     # show ROI
#     cv2.imshow('segment no:'+str(i),roi)
#     cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
#     cv2.waitKey(0)

# cv2.imshow('marked areas',original_image)
# cv2.waitKey(0)