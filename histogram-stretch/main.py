import ghs
import simplestretch as ss

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np 

# Testing of the classes
i = input('Enter image path: ')

img = np.asarray(Image.open(i))

x = input("'Enter stetch type. Options: mtf, asinh, ghs, ghs_inverse, ghs_asinh, ghs_asinh_inverse': ")

if x == 'mtf':
    mtf = ss.Mtf(img)
    mtf.plot_mtf()
elif x == 'asinh':
    anh = ss.Stretch(img)
    anh.plot_asinh()
elif x == 'ghs':
    ghs = ghs.Ghs(img)
    ghs.plot()
elif x == 'ghs_inverse':
    ghs_inv = ghs.InverseGhs(img)
    ghs_inv.plot()
elif x == 'ghs_asinh':
    gasinh = ghs.Asinh(img)
    gasinh.plot()
elif x == 'ghs_asinh_inverse':
    gainv = ghs.InverseAsinh(img)
    gainv.plot()
else:
    print("Wrong stetch type. Must be one of the options: mtf, asinh, ghs, ghs_inverse, ghs_asinh, ghs_asinh_inverse")