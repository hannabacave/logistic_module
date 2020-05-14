"""
Mandelbrot set 3D
============================
In this setion, you can see how to plot the Mandelbrot set in 3D.
"""

import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.figure as fg
from matplotlib import cm    
import numpy as np  
import warnings

warnings.filterwarnings("ignore")

n,M,L,dx,dy = 20,200,1.4,-0.6,0.0

def f(Z):     
    return np.e**(-np.abs(Z))

x = np.linspace(-L+dx,L+dx,M)    
y = np.linspace(-L+dy,L+dy,M)    
X,Y = np.meshgrid(x,y)     
Z = np.zeros(M)    
W = np.zeros((M,M))  
C = X + 1j*Y   

for k in range(1,n+1):     
    ZZ = Z**2 + C
    Z=ZZ
    
W= f(Z)

# Vers le haut
fig = plt.figure()  
plt.subplot(211) 
ax =  fig.add_subplot(111, projection= '3d')
ax.view_init(azim=120,elev=60)  
ax.dist = 4.5  
ax.set_facecolor([0.0,0.0,0.0]) 

ax.set_xlim(dx-L,dx+L)     
ax.set_zlim(dy-L,dy+L)    
ax.set_zlim(-L,1.5*L)         
ax.axis("off")   
ax.contourf3D(X, Y, -W, 2*n, cmap="hot")   


# Vers le bas
fig = plt.figure()  
plt.subplot(212) 
ax =  fig.add_subplot(111, projection= '3d')
ax.view_init(azim=120,elev=60)  
ax.dist = 5  
ax.set_facecolor([0.0,0.0,0.0]) 

ax.set_xlim(dx-L,dx+L)     
ax.set_zlim(dy-L,dy+L)    
ax.set_zlim(-0.5*L,1.5*L)         
ax.axis("off")   
ax.contourf3D(X, Y, W, 2*n, cmap="hot")   

plt.show() 