"""
Mandelbrot set in 3D
============================

In this setion, you can see how to plot the Mandelbrot set in 3D.
"""
import plotly
from logistic_module.Mandelbrot3D.Mandelbrot3D import Mand_3D


n,M = Mand_3D.init_param()
L = 1.4
dx = -0.6
dy = 0.0

fig = Mand_3D(n,M,L,dx,dy)

fig.interact().show()