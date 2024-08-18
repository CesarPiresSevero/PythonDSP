##########################################################################
#                                                                        #
#                          Image Editing                                 #
#                                                                        #
##########################################################################

"""
Basic image editing script showing how to read, edit, plot and save an 
image. An execution time profiling comparing a pure Python implementation 
with Numpy matrix algebra implementation is also available.

"""

############################### Imports ##################################
from matplotlib import image as img
from matplotlib import pyplot as plt
import numpy as np
import time

############################## Varibles ##################################
image_filename = "../Data/Images/landscape.jpg"
output_name = "img_output.jpg"

############################# Functions ##################################
def get_image(filaname):
	image = img.imread(filaname)
	return image

def grayscale_filter(image):
	## Only Python
	# Not efficent code using only python (~ 5150ms)
	if(False):
		x = 1/3
		start_time = time.time()
		y = []
		for row in image:
			x = []
			for pixel in row:
				# Just averaging each color
				x.append(pixel[0]/3+pixel[1]/3+pixel[2]/3)
			y.append(x)	
		delta_time = time.time()-start_time
		print ("# Process time = {}".format(delta_time))
		return np.asarray(y)

	## Numpy matrix functions
	# Efficient code using numpy (~ 75ms)
	start_time = time.time()
	r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
	# Just averaging each color
	gray_img = r/3 + g/3 + b/3
	# Weighting each color differently (NTSC/PAL implementation)
	# gray_img = 0.2989 * r + 0.5870 * g + 0.1140 * b
	delta_time = time.time()-start_time
	print ("# Process time = {}".format(delta_time))
	return gray_img

def edit_image(image):
	return grayscale_filter(image)


############################## Execution #################################
if __name__ == '__main__':
	print("### Image Editing Example ###")
	# Reading image
	print("# Fetching image")
	image = get_image(image_filename)
	# Calling editing function
	print("# Editing image...")
	grey_img = edit_image(image)
	# Creating image with high resolution and grayscale support
	plt.figure(dpi=1000)
	plt.imshow(grey_img, cmap='gray', vmin=0, vmax=255)
	# Removing all margins and axis info
	plt.margins(0,0)
	plt.axis('off')
	# Saving image file
	print("# Done!")
	plt.savefig(output_name,bbox_inches='tight', pad_inches=0)
	plt.show()
