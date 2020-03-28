from setuptools import setup
from logistic_module import __version__ as current_version

setup(
  name='logistic_module',
  version=current_version,
  description='Visualization of Mandelbrot fractal in 3D',
  url='https://github.com/hannabacave/Logistic-map',
  author='xxxxxxxxxxx',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['logistic_module.LogisticEquation','logistic_module.Mandelbrot2D','logistic_module.Mandelbrot3D'],
  zip_safe=False
)
