import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
from matplotlib import cm

def imshow(X, width, height):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git
    repo.
    """
    myImage.close()
    X=np.uint8(cm.gist_earth(myarray)*255)
    myImage = Image.fromarray(X)
    myImage.reszize((width,height))
    Image.open(myImage)


interact(imshow, width=(1,5,2000), height=(1, 5, 2000));