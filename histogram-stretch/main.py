import ghs
import simplestretch as ss

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np 

# Testing of the classes
img = np.asarray(Image.open('../img/linear.tif'))
"""
stretch = ghs.Ghs(img)
Ghs = stretch.ghs( 50, 10, 0, 0, 1)
plt.imshow(Ghs)
"""
arcsinh_stretch= ghs.Asinh(img)
imag = arcsinh_stretch.plot()


ghs_stretch = ghs.Ghs(imag)
img = ghs_stretch.plot()
"""
ghs_inv = ghs.InverseGhs(imag)
ghs_inv.plot()
"""
"""
anh = ss.Stretch(img)
imag = anh.plot_asinh()

mtf = ss.Mtf(imag)
mt = mtf.plot_mtf()
"""