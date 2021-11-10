from distutils.core import setup
from setuptools import find_packages


setup(name='ys60efaj',
      version='0.1',
      author='Paul Borutta',
      author_email='Paul.Borutta@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])