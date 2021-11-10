import numpy as np
from ipywidgets import interact, fixed
from PIL import Image



def imshow(X,width, height):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git
    repo.
    """
    myImage = Image.fromarray(X)
    myNewImage = myImage.resize((width,height))
    print("Image size: {}".format(myNewImage.size))
    myNewImage.show()

    #np.random.rand(100,100)
    interact(imshow,X=fixed(X), width=(1,2000,5), height=(1, 2000, 5));