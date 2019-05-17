'''
JDoe_JSmith_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'tina.jpg')
# Read the image data into an array
img = plt.imread(filename)


###
# pink eyeshadow
###
  
height = len(img)
width = len(img[0])
for r in range(190):
    for c in range(width):
        if sum(img[r][c])>600: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
            
#blue eyeshadow    
height = len(img)
width = len(img[0])
for r in range(190):
    for c in range(width):
        if sum(img[r][c])>600: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,255,255] # R + B = magenta


  
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
