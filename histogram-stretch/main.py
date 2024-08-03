import ghs
import ghs_2
from PIL import Image
import numpy as np 

img = np.asarray(Image.open('linear.tif'))

arcsinh_stretch= ghs.Asinh(img)
imag = arcsinh_stretch.plot()
#print(arcsinh_stretch.ghs.__code__.co_argcount)

ghs_stretch = ghs.Ghs(img)
imaag = ghs_stretch.plot()
#print(ghs_stretch.ghs.__code__.co_argcount)

stretch = ghs_2.Ghs(img)
imag = stretch.plot()