import numpy as np  
import plotly
import plotly.graph_objects as go

n = 500
M = 200
dx = -0.6     
dy = 0.0     
L = 1.4  

def f(Z):     
    return np.e**(-np.abs(Z))

x = np.linspace(-L+dx,L+dx,M)    
y = np.linspace(-L+dy,L+dy,M)    
X,Y = np.meshgrid(x,y)     
Z = np.zeros(M)    
W = np.zeros((M,M))
K = np.zeros((M,M))

C = X + 1j*Y   

for k in range(1,n+1):     
    ZZ = Z**2 + C
    Z=ZZ
    W= f(Z)-0.625    

    
fig = go.Figure(data=[go.Surface(z=W, x=X, y=Y,colorscale = 'Reds', showscale = False),
                      go.Surface(z=-W,x=X, y=Y, colorscale = 'Reds',reversescale = True, showscale = False)],
                
               layout=go.Layout(title='Mandelbrot 3D visualization'))

plotly.offline.plot(fig, filename='Mandelbrot3D.html')
#fig.show()