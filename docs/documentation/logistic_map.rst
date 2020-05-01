Logistic map
===============

What's a logistic map ?
------------------------

The logistic map is a sequence defined by the following recurrence formula :

.. math::

   x_{n+1}=rx_n(1-x_n)

where :

- r is the growth ratio and is defined and r :math:`r \in [0, 4]`

- :math:`x_0 \in [0, 1]`

This sequence allows us to simulate the population growth. Indeed, r is the coefficient 
by which the increasing of population : x  is multiplicated. But, just increasing poluation isn't 
realistic, so we introduce the factor : 1 - x representing the decrease of it. So, with this equation we 
can observe the evolution of some animal species like the rabbits. 


But, what's the link between fractals and logistic map ? 
When, we plotting the logistic map, when :math:`r > 3.45` we can note the logistic map split up in two same curves. 
Besides, when :math:`r > 3.75` this is the chaos. The graph which permite to see this is called *Bifurcation diagram*.


In this part, you'll see how to calculate and represent the logistic map, and how to represent the bifurcation diagram. 

The classes 
-------------

The class to calculate and vectorize logistic_map :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: logistic_module.LogisticEquation.Logistic_and_vectorization.Logistic_equation
    :members:

The class to create animation of logistic map :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: logistic_module.LogisticEquation.Visualization.Visualization
    :members:

The class to show Bifurcation diagram :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: logistic_module.LogisticEquation.Bifurcation.Visualization_bifurcation
    :members:


