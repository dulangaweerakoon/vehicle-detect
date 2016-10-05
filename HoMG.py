import numpy as np
import cv2 
import math
#sd
def normalize(img): 
	strips = []
	height, width = img.shape[:2]
	#a = 0.005;
	for i in range(height):
		rowWidth = getRowWidth(i); 
		#rowWidth = math.floor(rowWidth);
		if ((i+rowWidth)<height):
			strips.append(img[i:i+rowWidth,:,:]);
		else:
			break;
	
	return strips;
	
def getRowWidth(i):
	a = 0.005;
	rowWidth = 1 + 15*(1-math.exp(-1*a*i));
	rowWidth = math.floor(rowWidth);
	return rowWidth;

def getSobelDerivative(strips):
	N = 10;
	sobelX = [];
	sobelY =[];
	orientation = [];
	magnitude = [];
	
	for strip in strips:
		x_deri = cv2.Sobel(strip,cv2.CV_64F,1,0,ksize=5)
		y_deri = cv2.Sobel(strip,cv2.CV_64F,1,0,ksize=5)
		
		sobelX.append(x_deri);
		sobelY.append(y_deri);
		
		O = N*(np.arctan2(y_deri,x_deri) + math.pi)/(2*math.pi);
		orientation.append(O);
		
		M = np.sqrt(x_deri**2+y_deri);
		magnitude.append(M);
		
		
	return sobelX,sobelY,orientation,magnitude;


# def computeOrientation(sobelX,sobelY):
	# orientations = [];
	# N = 10;
	# i =0;
	# for x in sobelX:
		# y = sobelY[i];
		# O = N*(np.arctan2(y,x) + math.pi)/(2*math.pi);
		# i = i + 1;
	

def computeMovingGradient(img,keyframes):
	T1 = 1; #Tune these variables
	T2 = 1;	##""
	
	stripsImg = normalize(img);
	keyframeStrips = [];
	sobelX_img,sobelY_img = getSobelDerivative(stripsImg);
	
	sobel_img = np.sqrt(sobelX_img**2+sobelY_img**2);
	
	for frame in keyframes:
		strips = normalize(frame);
		keyframeStrips.append(strip);
		
	
		
		
		
		
		
		
		
	
	
	
	
#Main Program Starts here........

#Constants..........
s = 1;
wp = 3;
#...................

	
img = cv2.imread('1.bmp');
strips = normalize(img);

sobelX,sobelY,orientation,magnitude = getSobelDerivative(strips);
#computeOrientation(sobelX,sobelY)


# height, width = img.shape[:2];


