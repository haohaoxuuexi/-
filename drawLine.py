# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:54:56 2018

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
import os  

#img = data.astronaut()
t0 = timeit.default_timer()
path = r'C:\Users\user\Desktop\2018自立课题 坡道数据\data_MatScan' #文件夹目录  
#path = r'C:\Users\user\Desktop\2018自立课题 坡道数据\ceshi'
files= os.listdir(path) #得到文件夹下的所有文件名称  
n=1
t=list()
for file in files:  
    if n not in [4,8,17,19,27]:
    #for i in range(1,11,9):
#file='aizhenjiang.jpg'
    
        
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
        fig, ax = plt.subplots()
        #zs=snake[:, 0] + snake[:, 1]
        #zx=snake[:, 0] - snake[:, 1]
        #ys=snake2[:, 0] - snake2[:, 1]
        #yx=snake2[:, 0] + snake2[:, 1]
        a=np.argmax(snake[:, 1])
        b=np.argmin(snake[:, 1])
        c=np.argmax(snake2[:, 1])
        d=np.argmin(snake2[:, 1])
        #ax.imshow(img, cmap=plt.cm.gray)
        #ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
        ax.plot(snake[a:b, 0], snake[a:b, 1], '-k', lw=3)
        #bos=np.vstack((snake[a:b, 0], snake[a:b, 1])).transpose(1,0)
        #ax.plot(init2[:, 0], init[:, 1], '--r', lw=3)
        #ax.plot(np.hstack((snake2[0:c, 0],snake2[d:, 0])), np.hstack((snake2[0:c, 1],snake2[d:, 1])), '-g', lw=3)
        ax.plot(snake2[d:, 0], snake2[d:, 1], '-k', lw=3)
        ax.plot(snake2[0:c, 0], snake2[0:c, 1], '-k', lw=3)
        #temp=np.vstack((snake2[d:, 0], snake2[d:, 1])).transpose(1,0)
        #temp1=np.vstack((snake2[0:c, 0], snake2[0:c, 1])).transpose(1,0)
        #bos=np.vstack((temp, temp1))
        
        #rr, cc =line(int(snake[a,0]),int(snake[a,1]),int(snake2[c,0]),int(snake2[c,1]))
        #ax.plot(rr, cc, '-k', lw=3)
        ax.plot((snake[a,0],snake2[c,0]), (snake[a,1],snake2[c,1]), '-k', lw=3)
        #bos=np.vstack((rr,cc)).transpose(1,0)
        #bos=np.vstack((bos, temp))
        
        #rr, cc =line(int(snake2[d,0]),int(snake2[d,1]),int(snake[b,0]),int(snake[b,1]))
        #ax.plot(rr, cc, '-r', lw=3)
        ax.plot((snake2[d, 0],snake[b, 0]), (snake2[d, 1],snake[b, 1]), '-k', lw=3)
        #temp=np.vstack((rr,cc)).transpose(1,0)
        #bos=np.vstack((bos, temp))
        
        bos=np.vstack((snake[a:b, 0], snake[a:b, 1])).transpose(1,0)
        temp=np.vstack((snake2[d:, 0], snake2[d:, 1])).transpose(1,0)
        temp1=np.vstack((snake2[0:c, 0], snake2[0:c, 1])).transpose(1,0)
        bos=np.vstack((bos, temp))
        bos=np.vstack((bos, temp1))
        bos=np.vstack((bos, (snake[a,0],snake[a,1])))
        np.save('C:/Users/user/Desktop/bos边界/bos'+ str(n),bos)
        
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis([0, img.shape[1], img.shape[0], 0])
        ax.axis('off')
        bosfig=plt.gcf()
        bosfig.set_size_inches(1647.0/96,1394.0/96)
        #plt.savefig("C:/Users/user/Desktop/bos边界/" + str(n) + ".png")
        bosfig.savefig("C:/Users/user/Desktop/bos边界/" + str(n) + ".png",dpi=96)
        #plt.show()
    
    n+=1
    
elapsed = round(timeit.default_timer() - t0,2)
t.append(elapsed)




# =============================================================================
# fig, ax = plt.subplots()
# ax.set_xticks([]), ax.set_yticks([])
# ax.axis([0, img.shape[1], img.shape[0], 0])
# ax.plot(s[:, 0], s[:, 1], '-k', lw=3)
# plt.show()
# =============================================================================




