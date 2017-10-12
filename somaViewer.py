import cv2
import sys
import glob
from scipy import misc
import code
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import pickle

TOPLEFTROW= 208
TOPLEFTCOL = 99

TOPRIGHTROW= 208
TOPLEFTCOL = 1094

def nothing(x):
    pass
	
def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def adjustDots(originalImg, value, locDict):
	name, zVal1, xVal1, yVal1, zVal2, xVal2, yVal2 = locDict[value]
	print(name)
	originalImg[208 + zVal1-3:208 + zVal1+3, 99 + xVal1-3:99 + xVal1+3] = 255
	originalImg[208 + zVal2-3: 208 + zVal2+ 3, 1094 + yVal1-3:1094 + yVal1+3] = 255
	boop = originalImg
	return boop		
		
def somaVis(img, locDict):
	oldThresh = 0
	cv2.namedWindow('image')
	
	# create trackbars for picking threshold
	cv2.createTrackbar('Threshold', 'image', 0, len(locDict)-1, nothing)
	threshImg = img
	while(1):
		k = cv2.waitKey(1)
		if k == 32:
			break
		try:
			cv2.imshow('image', threshImg)
		except:
			print('WARNING: cv2 did not read the image correctly')

		# get current positions of four trackbars
		r = cv2.getTrackbarPos('Threshold','image')
		if (r != oldThresh):
			oldThresh = r
			threshImg = adjustDots(img, r, locDict)


	cv2.destroyAllWindows()

	return oldThresh, threshImg
		
def main():
	folderDir = sys.argv[1]
	pathList = glob.glob(folderDir + '*.png')

	imgPath = pathList[0]
	img = misc.imread(imgPath)
	img[:,:,2] = 0
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	locDict = load_obj("locationDictionary")
	
	somaVis(img,locDict)

if __name__ == "__main__":
	main()

