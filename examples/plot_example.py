"""
Bifurcation diagram example
=============================
This example will show the bifurcation diagram
"""

import .logistic_module

visu = Visualization( r0=0.05, n=40, p=10000, ci=0.05, frames=82, threshold = 100)

visu.bifurcation_diagram()