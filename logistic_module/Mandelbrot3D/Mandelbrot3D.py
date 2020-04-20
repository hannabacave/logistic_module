import numpy as np


class Mand_3D():
    
    """Class containing two functions to plot the Mandelbrot set in 3D with X,Y and Z axis following :  
        
         - Square area observed formed by X and Y axis
         
         - Matrix of elevation value of the Mandelbrot set in 2D as Z parameter"""
    
    
    def __init__(self,n,M,L,dx,dy):
        
        """Initialization of the parameters of the class  
          
        :param n: Number of iteration of the Mandelbrot equation  
        :type n: int  
          
        :param M: Number of pixels
        :type M: int  
        
        :param L: Length of the square area observed  
        :type L: float  
        
        :param dx: Shift of the square area origin along the x axis compared to (0,0)  
        :type dx: float  
        
        :param dy: Shift of the square area origin along the y axis compared to (0,0)  
        :type dy: float
        """
        
        self.n = n
        self.M = M
        self.L = L
        self.dx = dx
        self.dy = dy
        
    
    def grid(self):
        
        """Set the square area observed : 
        
            - Define two numpy arrays X and Y with the following characteristics : 
            
              - Index of the middle element : dx/dy respectively
              - length 2*L
              - M elements
              
           Return a grid formed by X and Y."""
        
                
        x = np.linspace(-self.L+self.dx,self.L+self.dx,self.M)    
        y = np.linspace(-self.L+self.dy,self.L+self.dy,self.M)
        X,Y = np.meshgrid(x,y)
        
        return X,Y
    
 
    def mand(self):
        
        """Set the matrix of elevation values :  
         
            1) Initialize the elements of the Mandelbrot equation
            2) Compute n iteration of the Mandelbrot equation on a (M,M) shaped 2D-array  
            3) Apply an elevation function on this 2D-array
            4) Filter the element of the 2D-array
            
           Return a 2D-array with the elevated 2D Mandelbrot set."""
        
        X,Y = self.grid()
        C = X + 1j*Y   
        Z = C
        
        for k in range(1,(self.n)+1):     
            ZZ = Z**2 + C
            Z = ZZ
            
        W = np.e**(-np.abs(Z)) - 0.625
        W[W>0] = W[W>0]*0.0001
        
        return W
