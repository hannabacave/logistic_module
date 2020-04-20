"""Modelize an interactive representation of the Mandelbrot set in 3D and compute the time spent to do it.
   Use the Mand_3D class from Mandelbrot3D
   
   ..seealso:: plotly.graph_projects for figure reference and Mand_3D documentation
   ..warning:: The modelization may take a bit of time depending of each computer (approximately 15s observed).
   ..note:: The decrease of the n and/or M parameters can speed up the processus.
   """


import numpy as np  
import plotly
import plotly.graph_objects as go
import warnings
import time
from Mandelbrot3D import Mand_3D



warnings.filterwarnings("ignore")
start = time.time()

def interact(n,M,L,dx,dy):
    
    """Return an interactive representation of the Mandelbrot set in 3D using the Mand_3D class."""

    p = Mand_3D(n,M,L,dx,dy)

    fig = go.Figure(data = [go.Surface(z=p.mand(), x=p.grid()[0], y=p.grid()[1],                                   
                                       colorscale = 'Reds', 
                                       showscale = False,
                                       connectgaps = False,
                                       hoverinfo = "none",
                                       contours = dict(x = dict(highlight = False),
                                                       y = dict(highlight = False,
                                                                show = True,
                                                                start = -2,
                                                                end = 2,
                                                                size = 1,
                                                                color = "yellow"),
                                                       z = dict(highlight = False))), 

                            go.Surface(z=-p.mand(), x=p.grid()[0], y=p.grid()[1],
                                       colorscale = 'Reds',
                                       reversescale = True,
                                       showscale = False,
                                       connectgaps = False,
                                       hoverinfo = "none",
                                       showlegend = False,
                                       contours = dict(x = dict(highlight = False),
                                                       y = dict(highlight = False,
                                                                show = True,
                                                                start = -2,
                                                                end = 2,
                                                                size = 1,
                                                                color = "yellow"),
                                                       z = dict(highlight = False)))],                       
                
                    layout = go.Layout(title='Mandelbrot 3D interactive visualization',
                                       width = 600,
                                       height = 600,
                                       hovermode= 'closest',
                                       template = "plotly_dark",
                                       scene = dict(xaxis = dict(visible = False),
                                                    yaxis = dict(visible = False),
                                                    zaxis = dict(visible = False),
                                                    hovermode = False,
                                                    camera = dict(eye=dict(x=0, y=-0.8, z=2.5) ))))
    
    return fig
   

n = 200
M = 200
L = 1.4
dx = -0.6
dy = 0    
    
fig = interact(n,M,L,dx,dy)    
    
plotly.offline.plot(fig, filename='Mandelbrot3D_interactive.html')

end = time.time()

print("Time spent to modelize the Mandelbrot set in 3D:  {0:.5f} s.".format(end - start))