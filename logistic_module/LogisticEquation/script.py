from logistic_module.LogisticEquation.Visualization import Visualization
from logistic_module.LogisticEquation.Bifurcation import Visualization_bifurcation
import time
viz = Visualization()
bif = Visualization_bifurcation()

start = time.time()
viz.start_animation()
end = time.time()
print("Time ellapsed to excute animation : {0:.5f} s.".format(end - start))

start = time.time()
bif.bifurcation_diagram()
end = time.time()
print("Time ellapsed to make bifurcation diagram : {0:.5f} s.".format(end - start))

