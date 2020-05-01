Mandelbrot set 
=====================

What's the Mandelbrot set ?
-----------------------------

The Mandelbrot set is a fractal defined as the set of points c of the complex plane 
for which the sequence of complex numbers defined by recurrence by : 

.. math::  

    \begin{cases}
    z_0=0\\
    z_{n+1}=z_n^2+c
    \end{cases}

is bounded.

Thanks to the bifurcation diagram, we were able to go from the deterministic world to chaos. And now, since we are
in the chaos domain, we're going to zoom into the deepest aspects of the Mandelbrot set.


So, in this part the user will be able to see (and code) :

- The Mandelbrot set in 2D ;

- An animation zooming into the set ;

- An interactive vizualisation of the Mandelbrot set in 3D.

- An animation rotating the 3D fractal to show the link between the Mandelbrot set and the bofurcation diagram. 

Mandelbrot in 2D 
-------------------

The class to plot :   
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: logistic_module.Mandelbrot2D.Mandelbrot2D.Mandelbrot_2D
    :members:

A zoom into the Mandelbrot set in two ways :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: logistic_module.Mandelbrot2D.Mandelbrot2DAnimation.animate

.. autofunction:: logistic_module.Mandelbrot2D.Inside_Mandelbrot.Inside_the_set
 
A method to recognize some patterns into the Mandelbrot set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: logistic_module.Mandelbrot2D.Plot_pattern.plot_patterns
    :members:


Mandelbrot in 3D 
---------------------

Interactive vizualisation :  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: logistic_module.Mandelbrot3D.Mandelbrot3D.Mand_3D
    :members:


Rotation of the 3D Mandelbrot set :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
