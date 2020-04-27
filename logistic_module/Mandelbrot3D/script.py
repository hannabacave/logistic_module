"""Modelize an interactive representation of the Mandelbrot set in 3D and compute the time spent to do it.
   Use the Mand_3D class from Mandelbrot3D
   
   ..seealso:: plotly.graph_projects for figure reference and Mand_3D documentation
   ..warning:: The modelization may take some time depending of each computer.
   ..note:: The decrease of the n and/or M parameters can speed up the processus.
   """

import warnings
import time
import plotly
from Mandelbrot3D import Mand_3D

warnings.filterwarnings("ignore")

start = time.time()

def init_param():
   
   """ Initialize the parameters for the modelization with asked input for :
         - n : number of iteration of the Mandelbrot equation
         - M : numer of pixels   """

   n = int(input("Enter a value for n :"))
   M = int(input("Enter a value for M :"))
   L = 1.4
   dx = -0.6
   dy = 0.0

   fig = Mand_3D(n,M,L,dx,dy)

   return fig 

fig = init_param()
plotly.offline.plot(fig.interact(), filename='Mandelbrot3D_interactive.html')

end = time.time()
print("Time spent to modelize the Mandelbrot set in 3D:  {0:.5f} s.".format(end - start))