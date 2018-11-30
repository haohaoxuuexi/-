# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:51:41 2018

@author: user
"""

import timeit
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
#from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from PIL import Image
from skimage.draw import line 
from skimage import io

#img = data.astronaut()

import os  
path = r'C:\Users\user\Desktop\2018自立课题 坡道数据\data_MatScan' #文件夹目录  
#path = r'C:\Users\user\Desktop\2018自立课题 坡道数据\ceshi'
files= os.listdir(path) #得到文件夹下的所有文件名称  
n=1
t=list()
#for file in files:  
    #for i in range(1,11,9):
file='aizhenjiang.jpg'
t0 = timeit.default_timer()
#print("fixed")       
img=io.imread('C:/Users/user/Desktop/2018自立课题 坡道数据/data_MatScan/'+file)
#io.imshow(img)
img = rgb2gray(img)  


s = np.linspace(0, 2*np.pi, 400)
x = 400 + 550*np.cos(s)
y = 700 + 1000*np.sin(s)
init = np.array([x, y]).T    

x2 = 1250 + 550*np.cos(s)
y2 = 700 + 1000*np.sin(s)
init2 = np.array([x2, y2]).T 

snake = active_contour(gaussian(img, 3),init, alpha=0.015, beta=0.1,w_line=1, gamma=0.001, bc='periodic') 
snake2 = active_contour(gaussian(img, 3),init2, alpha=0.015, beta=0.1,w_line=1, gamma=0.001, bc='periodic') 
#print(-i)
fig, ax = plt.subplots(figsize=(7, 7))
#zs=snake[:, 0] + snake[:, 1]
#zx=snake[:, 0] - snake[:, 1]
#ys=snake2[:, 0] - snake2[:, 1]
#yx=snake2[:, 0] + snake2[:, 1]
#a=np.argmax(zs)
#b=np.argmax(zx)
#c=np.argmin(ys)
#d=np.argmin(yx)
#rr, cc =line(int(snake[a,0]),int(snake[a,1]),int(snake2[c,0]),int(snake2[c,1]))
#ax.plot(rr, cc, '-k', lw=3)
#rr, cc =line(int(snake[b,0]),int(snake[b,1]),int(snake2[d,0]),int(snake2[d,1]))
#ax.plot(rr, cc, '-k', lw=3)

#ax.imshow(img, cmap=plt.cm.gray)
ax.imshow(img)
#ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
ax.plot(snake[:, 0], snake[:, 1], '-k', lw=3)
#ax.plot(init2[:, 0], init[:, 1], '--r', lw=3)
ax.plot(snake2[:, 0], snake2[:, 1], '-k', lw=3)



ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])
#plt.savefig("C:/Users/user/Desktop/二值脚印轮廓/" + str(n) + ".png")
#plt.imsave("C:/Users/user/Desktop/二值脚印轮廓/" + str(n) + ".png")
plt.show()
n+=1

elapsed = round(timeit.default_timer() - t0,2)
t.append(elapsed)



