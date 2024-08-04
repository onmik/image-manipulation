import ghs

from PIL import Image
import numpy as np 

img = np.asarray(Image.open('linear.tif'))

arcsinh_stretch= ghs.Asinh(img)
imag = arcsinh_stretch.plot()


ghs_stretch = ghs.Ghs(imag)
ghs_stretch.plot()

ghs_inv = ghs.InverseGhs(img)
ghs_inv.plot()