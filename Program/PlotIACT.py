# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:25:25 2018

@author: user
"""
import array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pylab
import numpy as np
import os
current_path = os.getcwd()


defm_v= current_path +'\\Result\\iact.img'
f = open(defm_v, 'rb')
nImages =47
height =128
width = 128
I = np.fromfile(f,dtype='f4',count=nImages*height*width)   
f.close()

data=np.array([I])
b=np.reshape(data,(47,128,128))
print b
s79=b[:,79,:]
news79=np.flipud(s79)


fig = plt.figure()


plt.axis('off')
plt.imshow(news79,cmap = plt.cm.gray)
plt.hlines(15, 0, 127, colors = "c")