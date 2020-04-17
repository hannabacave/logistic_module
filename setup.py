from setuptools import setup
from logistic_module import __version__ as current_version

setup(
  name='logistic_module',
  version=current_version,
  description='Visualization of Mandelbrot fractal in 3D',
  url='https://github.com/hannabacave/Logistic_module',
  author='Cindy Delage, Hanna Bacave, Yassine Mimouni',
  license='MIT',
  packages=['logistic_module'],
  zip_safe=False
)
