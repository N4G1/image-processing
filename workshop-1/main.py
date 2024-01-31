import numpy as np
import matplotlib.pyplot as plt
from imageio.v3 import imread


# Simulating CFA behavior, we are basing us off of the Bayer filter.
def mosaic(image):
    pass

# Creating a demosaicing algorithm
def demosaic(mosaic):
    pass

# Helper functions
def linear_r(im):
    pass

def linear_g(im):
    pass

def linear_b(im):
    pass

# Reading the images
original = imread("landscape.jpg").astype(float) / 255
custom = imread("landscape.jpg").astype(float) / 255

# Matplotlib adjustments, removing borders and showing images closer together for better comparison
fig, axe = plt.subplots(nrows=2, ncols=1, figsize=(13.5, 11))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0)

axe[0].imshow(original)
axe[0].axis('off')
axe[1].imshow(custom, cmap='gray')
axe[1].axis('off')

plt.show()
