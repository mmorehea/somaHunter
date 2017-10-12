#code.interact(local=dict(globals(), **locals())) 

from scipy import misc
import glob
import code
from PIL import Image
import numpy as np
import sys
from matplotlib import pyplot as plt


# TOP LEFT
def getXZCoordinates(img):
	subimg = img[100:800, 94:869, :]
	xx,yy,zz = subimg.shape
	subimg[90, :, :] = [255,0,0] # upper left corner
	subimg[xx-50, :, :] = [0,255,0] # lower right corner

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
	subimg[xx-45, :, :] = [255,0,0] 
	subimg[:, 44, :] = [255,0,0] 
	subimg[:, yy-37, :] = [255,0,0] 
	showimg = Image.fromarray(subimg, 'RGB')
	showimg.show()

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
	print(xx-45, 108)
	code.interact(local=dict(globals(), **locals())) 
	return int(YZlat), int(YZlong)










#FOR BOTTOM LEFT GRAPH
def getXYCoordinates(img):
	subimg = img[1072:1600, 94:869, :]
	xx,yy,zz = subimg.shape
	subimg[3, 38, :] = [255,0,0]  #upper left corner
	subimg[xx-3, yy-38, :] = [0,255,0] #lower right corner

	showimg = Image.fromarray(subimg, 'RGB')
	showimg.show()

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

	long = (np.max(dot[1]) + np.min(dot[1])) / 2
	lat = (np.max(dot[0]) + np.min(dot[0])) / 2

	mask[int(lat), int(long)] = 155

	#showimg = Image.fromarray(mask)
	#showimg.show()
	code.interact(local=dict(globals(), **locals())) 
	return int(lat), int(long)





def main():
	folderDir = sys.argv[1]
	pathList = glob.glob(folderDir + '*.png')
	
	for each in pathList:
		image_path = each
		img = misc.imread(image_path)
		print(each)
		zVal1, xVal1 = getXZCoordinates(img)
		print("Z: " + str(zVal1) + " X:" + str(xVal1))
		
		zVal2, yVal1 = getYZCoordinates(img)
		print("Z: " + str(zVal2) + " Y:" + str(yVal1))
		
		yVal2, xVal2 = getXYCoordinates(img)
		print ("Y: " + str(655 - yVal2) + " X:" + str(xVal2))
		
	

if __name__ == "__main__":
	main()
