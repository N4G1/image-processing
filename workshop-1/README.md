## # 1 - Convert color image into a grayscale mosaic

![image](https://github.com/N4G1/image-processing/assets/10486712/5a051ddc-0e33-4a90-a850-01ab3689ca4e)

Image sensor in a digital camera is actually monochrome, and can only measure light intensity falling on it in each pixel.
In order to create color images, a mosaic of color filters is placed over it, so that in each pixel only one of the color channels is measured ex. R,G,B.
And out of the sensor comes a mosaic of gray tones.
Such filters are called Color Filter Arrays (CFA) and are made of repeating pattern of NxN elements.
This particular CFA that you can see on the picture is called Bayer filter.

Your task in this section is to convert a color image into a grayscale mosaic.
Follow the steps in this section and fill the function `mosaic` in the `main.py` file with the required code. 

```python
def mosaic(image):
```

### # 1.1

Start by allocating space for those 3 separate channels (R,G,B).
Numpy has a lot of built-in functionality for that.
You can for example use `np.zeros((rows, cols))`

### # 1.2

Fill each allocated space in the previous step with separate color information from the image.
Remember that we are basing our mosaic on Bayer filter, hence the color information has to be calculated accordingly.
- you can either use for loop to achieve that
- or python built-in **slice notation** check [this link](https://sparkbyexamples.com/python/python-slice-notation-explain/) to learn more

### #1.3

Combine the separated color channels into one image, and return it from the `mosaic` function.
Now you can display the image and check that everything is in order.

## # 2 - Demosaicing (Linear)

The task of a demosaicing algorithm is to reconstruct a color image out of such a grayscale mosaic.
One way to do this is to first move the information found in the mosaic into the correct channels in a color image,
and then fill in the missing information by interpolating the data in each channel individually.
After interpolation of each channel we need to stitch the individual channels into a one coherent image.

Your task in this section is to convert a grayscale mosaic into a color image.
Follow the steps in this section and fill the function `demosaic` in the `main.py` file with the required code.

```python
def demosaic(mosaic):
```

### # 2.1

Allocate space and separate the mosaic into separate color channels.

### # 2.2

![image](https://github.com/N4G1/image-processing/assets/10486712/b3ae6d7e-e6b9-4243-bf5f-6bfdc24fe8be)

Fill in the missing information in each color channel, use the supplied helper functions.

### # 2.2.1

Interpolate the Red channel

### # 2.2.2

Interpolate the Blue channel

### # 2.2.3

Interpolate the Green channel

### # 2.3

Stitch the interpolated channels into one coherent image and return it from the `demosaic` function.

## # 3 - Compare the results

For the *landscape* image (and other horizontal images) you can use the following code to compare the results with the original side by side
```python
fig, axe = plt.subplots(nrows=2, ncols=1, figsize=(13.5, 11))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0)

axe[0].imshow(original_image)
axe[0].axis('off')
axe[1].imshow(your_image)
axe[1].axis('off')

plt.show()
```

For comparison of results of *lighthouse* image (and other vertical images) use this code instead:
```python
fig, axe = plt.subplots(nrows=1, ncols=2, figsize=(13, 10))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0)

axe[0].imshow(original_image)
axe[0].axis('off')
axe[1].imshow(your_image)
axe[1].axis('off')

plt.show()
```