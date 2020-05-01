"""
Logistic_module's examples
============================

In this setion, you can show some static examples of our package.
"""

# %%
# Bifurcation diagram
# ------------------------
# This function show the bifurcation diagram

from logistic_module.LogisticEquation.Bifurcation import Visualization_bifurcation
viz = Visualization_bifurcation()

viz.bifurcation_diagram()

# %%
# Bifurcation diagram
# ------------------------
# This function show the bifurcation diagram

import matplotlib.pyplot as plt

from logistic_module.Mandelbrot2D.Mandelbrot2D import Mandelbrot_2D
Z = Mandelbrot_2D(hauteur=500, largeur=500, max_iteration=100,
                  xmin=-2, xmax=0.5, ymin=-1.25, ymax=1.25)

fig = plt.figure()
fig.suptitle("Mandelbrot set")
im = plt.imshow(Z.Mandelbrotset, cmap='magma')
plt.colorbar()
plt.show()

