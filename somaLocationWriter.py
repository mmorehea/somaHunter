import cv2
import sys
import glob
from scipy import misc
import code
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import pickle
import csv

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
		
def findminmaxs(locDict):
	#code.interact(local=dict(globals(), **locals())) 
	zs = [i[1][1] for i in locDict.items()]
	xs = [i[1][2] for i in locDict.items()]
	ys = [i[1][3] for i in locDict.items()]
	
	return min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)
def main():
	locDict = load_obj("locationDictionary")
	
	xmin, ymin, zmin, xmax,ymax, zmax = findminmaxs(locDict)
	xtotal = xmax-xmin
	ytotal = ymax-ymin
	ztotal = zmax-zmin
	
	print(xtotal)
	print(ytotal)
	print(ztotal)
	with open('eggs.csv', 'w') as f:
		f.write("index" + ", " + "name" + ", " + "zvalue" + ", " + "xvalue" + ", " + "yvalue" + ' \n')
		for ii,each in enumerate(list(locDict)):
			#locationDict[ii] = (os.path.basename(each), zVal1, xVal1, yVal1, zVal2, xVal2, yVal2)
			name, zVal1, xVal1, yVal1, zVal2, xVal2, yVal2 = locDict[each]
			writeString = str(ii) + ", " + name + ", {:.4f}, {:.4f}, {:.4f} \n".format(zVal1/float(ztotal+1), xVal1/float(xtotal+1), yVal2/float(ytotal+1))
			f.write(writeString)


if __name__ == "__main__":
	main()