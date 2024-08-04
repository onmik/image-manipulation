import ghs
import simplestretch as ss

from PIL import Image
import numpy as np 

img = np.asarray(Image.open('../img/linear.tif'))

arcsinh_stretch= ghs.Asinh(img)
imag = arcsinh_stretch.plot()


ghs_stretch = ghs.Ghs(imag)
imag = ghs_stretch.plot()

ghs_inv = ghs.InverseGhs(imag)
ghs_inv.plot()

anh = ss.Stretch(img)
imag = anh.plot_asinh()

mtf = ss.Mtf(imag)
mt = mtf.plot_mtf()