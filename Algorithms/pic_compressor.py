#################################################################################
#                                                                               #
#                          Picture Compression                                  #
#                                                                               #
#################################################################################


"""
Tests 
"""

################# Imports #########################
from matplotlib import image as img
from matplotlib import pyplot as plt
import numpy as np

################ Variables ########################
img_name="../Data/Images/dog.jpg"
img_name="../Data/Images/people.jpg"
img_name="../Data/Images/landscape.jpg"
img_title="Dog"

################## Script ######################### 
image = img.imread(img_name)

# Greyscale
y = []
for row in image:
	x = []
	for pixel in row:
		x.append(pixel[0]/3+pixel[1]/3+pixel[2]/3)
	y.append(x)
y = np.asarray(y)
# plt.imshow(y, cmap='gray', vmin=0, vmax=255)

# Test comb compression
comb_size = 1
y = []
img_avg=np.mean(image)
comb_val = np.uint8(img_avg)
for i,row in enumerate(image):
	x = []
	counter=0
	for j,pixel in enumerate(row):
		if(i%2 == 0):
			counter+=1
			if(counter<comb_size):
				x.append([comb_val,comb_val,comb_val])
			elif(counter> 2*comb_size):
				counter=0
				x.append([comb_val,comb_val,comb_val])
				
			else:
				x.append(pixel)

		else:
			counter+=1
			if(counter<comb_size):
				x.append(pixel)
			elif(counter> 2*comb_size):
				counter=0
				x.append(pixel)
			else:
				x.append([comb_val,comb_val,comb_val])
	y.append(x)
# y = np.asarray(y)
# plt.figure(figsize=(1.944, 2.592), dpi=1000)
# plt.imshow(y)
# plt.margins(0,0)
# plt.axis('off')
# plt.savefig('output.tiff',bbox_inches='tight', pad_inches=0)

# Test half pic
comb_size = 1
y = []
img_avg=np.mean(image)
comb_val = np.uint8(img_avg)
skip=True
for i,row in enumerate(image):
	x = []
	skip= not skip
	for j,pixel in enumerate(row):
		if(i%2 == 0):
			if(skip):
				if(j%2==0): x.append(pixel)
			else:
				if(j%2!=0): x.append(pixel)		
	if(i%2 == 0): y.append(x)
y = np.asarray(y)

# plt.figure(figsize=(1.944/2, 2.592/2), dpi=1000)
plt.imshow(y)
plt.margins(0,0)
plt.axis('off')
plt.savefig('output.tiff',bbox_inches='tight', pad_inches=0)
plt.show()
