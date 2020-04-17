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

 
fig = go.Figure(data = [go.Surface(z=W, x=X, y=Y,
                                   colorscale = 'Reds',
                                   showscale = False,
                                   hoverinfo = "none",
                                   contours = dict(x = dict(highlight = False),
                                                   y = dict(highlight = False),
                                                   z = dict(highlight = False))),
                        go.Surface(z=-W,x=X, y=Y,
                                   colorscale = 'Reds',
                                   reversescale = True,
                                   showscale = False,
                                   hoverinfo = "none",
                                   showlegend = False)],                       
                
               layout = go.Layout(title='Mandelbrot 3D visualization',
                                  width = 700,
                                  height = 700,
                                  hovermode= 'closest',
                                  template = "plotly_dark",
                                  scene = dict(xaxis = dict(visible = False, spikesides = False),
                                               yaxis = dict(visible = False),
                                               zaxis = dict(visible = False),
                                               hovermode = False,
                                               camera = dict(eye=dict(x=0, y=-0.8, z=2.5),
                                                             center=dict(x=0, y=0, z=0)) 
                                               
                                             )))
                                                    
plotly.offline.plot(fig, filename='Mandelbrot3D.html')