# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 00:07:20 2017
@author: Cesar Alvarez
"""

import pylab
import numpy as np

x = np.linspace(0, 20, 1000)  # 100 evenly-spaced values from 0 to 50
g1 = np.linspace(0, 20, 1000)  # 100 evenly-spaced values from 0 to 50
g2 = np.linspace(0, 20, 1000)  # 100 evenly-spaced values from 0 to 50


g1 = 13*x
g2 = x**13

pylab.plot(x, g1)
pylab.plot(x, g2)
#pylab.xlim(5, 15)
#pylab.ylim(-1.2, 1.2)