from setuptools import setup
import os

requirementPath = os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt')

with open(requirementPath) as f:
    install_requires = list(f.read().splitlines())

setup(
  name='logistic_module',
  version= '0.0.2',
  description='Visualization of Mandelbrot fractal in 3D',
  url='https://github.com/hannabacave/Logistic_module',
  author='Cindy Delage, Hanna Bacave, Yassine Mimouni',
  packages=['logistic_module','logistic_module.LogisticEquation','logistic_module.Mandelbrot2D', 'logistic_module.Mandelbrot3D'],
  zip_safe=False,
  install_requires=install_requires
)
