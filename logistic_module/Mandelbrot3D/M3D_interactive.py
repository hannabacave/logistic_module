import numpy as np  
import plotly
import plotly.graph_objects as go
import warnings
import time
from Mandelbrot3D import Interactive

warnings.filterwarnings("ignore")

start = time.time()

p = Interactive(200,200,1.4,-0.6,0)

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
   
 
plotly.offline.plot(fig, filename='Mandelbrot3D_interactive.html')

end = time.time()

print("Time spent to modelize the Mandelbrot set in 3D:  {0:.5f} s.".format(end - start))