import timeit
import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import line 
from skimage import io
import pandas as pd
import os  

n=1
bos=np.load('C:/Users/user/Desktop/bos边界/bos'+ str(n)+'.npy')
df = pd.read_excel("com.xls")
com = df.iloc[:, 2:4]  #3:6

img=io.imread('C:/Users/user/Desktop/bos边界/'+ str(n) + '.png')
#r=np.array([int(com.loc[0,'com_x']),int(com.loc[1,'com_x']),int(com.loc[2,'com_x'])])
#c=np.array([int(com.loc[0,'com_y']),int(com.loc[1,'com_y']),int(com.loc[2,'com_y'])])
r1, c1 =line(int(com.loc[0,'com_x']),int(com.loc[0,'com_y']),int(com.loc[1,'com_x']),int(com.loc[1,'com_y']))
r2, c2 =line(int(com.loc[1,'com_x']),int(com.loc[1,'com_y']),int(com.loc[2,'com_x']),int(com.loc[2,'com_y']))


fig = plt.figure()
ax = plt.gca() 
ax.invert_yaxis()
#plt.imshow(img)
plt.plot(bos[:,0], bos[:,1], '-k', lw=3)
plt.plot(com.loc[:,'com_x'], com.loc[:,'com_y'], '-r', lw=3)
#plt.plot(r1, c1, '-r', lw=3)
#plt.plot(r2, c2, '-r', lw=3)
plt.show()








