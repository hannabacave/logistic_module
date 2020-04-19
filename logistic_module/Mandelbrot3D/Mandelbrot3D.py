import numpy as np
import plotly.graph_objects as go


class Interactive():
    
    
    def __init__(self,n,M,L,dx,dy):
        self.n = n
        self.M = M
        self.L = L
        self.dx = dx
        self.dy = dy
        
    
    def grid(self):
        x = np.linspace(-self.L+self.dx,self.L+self.dx,self.M)    
        y = np.linspace(-self.L+self.dy,self.L+self.dy,self.M)
        X,Y = np.meshgrid(x,y)
        return X,Y
    
 
    def mand(self):
        X,Y = self.grid()
        C = X + 1j*Y   
        Z = C
        for k in range(1,(self.n)+1):     
            ZZ = Z**2 + C
            Z = ZZ
        W = np.e**(-np.abs(Z)) - 0.625
        W[W>0] = W[W>0]*0.0001
        return W
