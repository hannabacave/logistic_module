from logistic_module.LogisticEquation.Visualization import Visualization
import time
viz = Visualization()

start = time.time()
viz.start_animation()
end = time.time()
print("Time ellapsed to excute animation : {0:.5f} s.".format(end - start))

start = time.time()
viz.bifurcation_diagram()
end = time.time()
print("Time ellapsed to make bifurcation diagram : {0:.5f} s.".format(end - start))
