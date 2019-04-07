# -*- coding: utf-8 -*-
"""
Created on Wed May 02 15:16:13 2018

@author: user
"""


import shutil
import time
from PIL import Image

import matplotlib.image as mpimg # mpimg 用于读取图片
import math  
import numpy as np  

#from ij import IJ
import imagej 
import json 

import matplotlib.pyplot as plt
import os
import sys
import math
#import matplotlib.pyplot
import numpy as np
import array



img=mpimg.imread('hct_ex_test.tif')
imgplot = plt.imshow(img)