#code.interact(local=dict(globals(), **locals())) 

from scipy import misc
import glob
import code
from PIL import Image
import numpy as np
import sys
from matplotlib import pyplot as plt
import pickle
import os

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

# TOP LEFT
def getXZCoordinates(img):
	subimg = img[100:800, 94:869, :]
	xx,yy,zz = subimg.shape
	subimg[108, :, :] = [255,0,0] # upper left corner
	subimg[xx-45, :, :] = [0,255,0] # lower right corner
	subimg[:, 5, :] = [0,0,255] 
	subimg[:, yy-15, :] = [100,0,0] 
	
	subimg = subimg[108:xx-45, 5:yy-15, :]
	#print(subimg.shape)
	#showimg = Image.fromarray(subimg, 'RGB')
	#showimg.show()

	white = np.where(subimg == [255, 255, 255])
	black = np.where(subimg == [0, 0, 0])
	blue = np.where(subimg == [0, 0, 255])

	mask = np.ones(subimg.shape)
	mask[white] = 0
	mask[black] = 0
	mask[blue] = 0

	mask = mask[:,:,0]
	mask *= 255
	dot = np.where(mask == 255)

	XZlong = (np.max(dot[1]) + np.min(dot[1])) / 2
	XZlat = (np.max(dot[0]) + np.min(dot[0])) / 2

	mask[int(XZlat), int(XZlong)] = 155

	#showimg = Image.fromarray(mask)
	#showimg.show()
	
	return int(XZlat), int(XZlong)

# ----------------------------------------------


def getYZCoordinates(img):
	subimg = img[100:800, 1050:1700, :]
	xx,yy,zz = subimg.shape
	subimg[108, :, :] = [255,0,0] 
	subimg[xx-45, :, :] = [0,255,0] 
	subimg[:, 44, :] = [0,0,255] 
	subimg[:, yy-37, :] = [100,0,0] 

	subimg = subimg[108:xx-45, 44:yy-37, :]
	
	#print(subimg.shape)
	#showimg = Image.fromarray(subimg, 'RGB')
	#showimg.show()
	
	white = np.where(subimg == [255, 255, 255])
	black = np.where(subimg == [0, 0, 0])
	blue = np.where(subimg == [0, 0, 255])

	mask = np.ones(subimg.shape)
	mask[white] = 0
	mask[black] = 0
	mask[blue] = 0

	mask = mask[:,:,0]
	mask *= 255
	dot = np.where(mask == 255)

	YZlong = (np.max(dot[1]) + np.min(dot[1])) / 2
	YZlat = (np.max(dot[0]) + np.min(dot[0])) / 2

	mask[int(YZlat), int(YZlong)] = 155

	#showimg = Image.fromarray(mask)
	#showimg.show()

	#code.interact(local=dict(globals(), **locals())) 
	return int(YZlat), int(YZlong)










#FOR BOTTOM LEFT GRAPH
def getXYCoordinates(img):
	subimg = img[1072:1600, 94:869, :]
	xx,yy,zz = subimg.shape
	subimg[3, 38, :] = [255,0,0]  #upper left corner
	subimg[xx-3, yy-38, :] = [0,255,0] #lower right corner
	#print(subimg.shape)
	#showimg = Image.fromarray(subimg, 'RGB')
	#showimg.show()

	white = np.where(subimg == [255, 255, 255])
	black = np.where(subimg == [0, 0, 0])
	blue = np.where(subimg == [0, 0, 255])

	mask = np.ones(subimg.shape)
	mask[white] = 0
	mask[black] = 0
	mask[blue] = 0

	mask = mask[:,:,0]
	mask *= 255
	dot = np.where(mask == 255)
	if dot[0].size == 0:
		return -1, -1
	long = (np.max(dot[1]) + np.min(dot[1])) / 2
	lat = (np.max(dot[0]) + np.min(dot[0])) / 2

	mask[int(lat), int(long)] = 155

	#showimg = Image.fromarray(mask)
	#showimg.show()
	#code.interact(local=dict(globals(), **locals())) 
	return int(lat), int(long)





def main():
	folderDir = sys.argv[1]
	pathList = glob.glob(folderDir + '*.png')

	locationDict = {}
	total = len(pathList)
	
	for ii,each in enumerate(pathList):
		img = misc.imread(each)
		print(each + " " + str(ii) + " / " + str(total))
		zVal1, xVal1 = getXZCoordinates(img)
		#print("Z: " + str(zVal1) + " X:" + str(xVal1))
		
		zVal2, yVal1 = getYZCoordinates(img)
		#print("Z: " + str(zVal2) + " Y:" + str(yVal1))
		
		yVal2, xVal2 = getXYCoordinates(img)
		yVal2 = 528 - yVal2
		#print ("Y: " + str(528 - yVal2) + " X:" + str(xVal2))
		
		locationDict[ii] = (os.path.basename(each), zVal1, xVal1, yVal1, zVal2, xVal2, yVal2)
		
	save_obj(locationDict, "locationDictionary")
		
	

if __name__ == "__main__":
	main()
