# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import time

start_time=time.time()
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# print(args['image'])

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image 
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it

filename = "{}.png".format(os.getpid())
path = "/home/mottakin/tesseract-ocr/tesseract-testing/output/"
name = os.path.join(path,filename)
cv2.imwrite(name, gray)

########## Chaniging here ##########


gray = Image.open(name);
gray.save(name,dpi=(150,150))

# gray = gray.save(name,quality=20,optimize=True)

####################################

filename = name
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
print(time.time()-start_time)
# text = pytesseract.image_to_string(Image.open(filename), lang='ben', config='--oem 0')
text = pytesseract.image_to_string(Image.open(filename), lang='eng', config='--oem 2')
# os.remove(filename)
outfile = os.path.basename(args['image']).split('.')[0];
# out = open("")
# print(outfile);

name = os.path.join(path,outfile+".txt")
out = open(name,"w")
out.write(text)
 
# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)	

print(time.time()-start_time)