import cv2
import numpy as np
import sys

def cartoonize_image(img, ds_factor=4, sketch_mode=False):
	# Convert image to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# Apply median filter to the grayscale image
	img_gray = cv2.medianBlur(img_gray, 7)
	
	# Detect edges in the image and threshold it
	edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
	ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

	# 'mask' is the sketch of the image
	if sketch_mode:
		return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

	# Resize the image to a smaller size for faster computation
	img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
	num_repetitions = 10
	sigma_color = 5
	sigma_space = 7
	size = 5

	# Apply bilateral filter the image multiple times
	for i in range(num_repetitions):
		img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space)

	img_output = cv2.resize(img_small, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)

	dst = np.zeros(img_gray.shape)

	# Add the thick boundary lines to the image using 'AND' operator
	dst = cv2.bitwise_and(img_output, img_output, mask=mask)
	return dst

if __name__=='__main__':
	
	#ap = argparse.ArgumentParser()
	#ap.add_argument("-i", "--image", required = True, help = "Path to the image to be scanned")
	#args = vars(ap.parse_args())

	while True:

		frame = cv2.imread(sys.argv[1])
		frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

		out=sys.argv[1][:-4]+'p.jpg'
		cv2.imwrite(out, cartoonize_image(frame, sketch_mode=False))
		
		cv2.destroyAllWindows()
#Deconstructing th

