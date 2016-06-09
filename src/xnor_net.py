""" Class and method definition for the layers in XNOR-Net
"""
import theano
import numpy as np
import lasagne
import theano.tensor as T
import time

class BinaryActivLayer(lasagne.layers.Layer):
    """ Binary activation layer as described in XNOR-Net paper.
    This computes the scaling matrix K and the binary input I. Same notaions
    followed.
    """
    def __init__(self, incoming):


class BinaryConvLayer(lasagne.layers.Conv2DLayer):
    """ Binary convolution layer which performs convolution using XNOR and popcount operations.
    This is followed by the scaling with input and weight scaling factors K and alpha respectively.
    """

    def __init__(self, incoming, num_filters, filter_size, **kwargs):
    """
    Parameters
    -----------
    incoming : layer or tuple
        Ipnut layer to this layer. If this is fed by a data layer then this is a tuple representing input dimensions.
    num_filters: int
        Number of 3D filters present in this layer = No of feature maps generated by this layer
    filter_size: tuple
        Filter size of this layer. Leading dimension is = no of input feature maps.
    """
    

    # overriding conv operation from Conv2DLayer implementation
    def convolve(self, input, **kwargs):
    """ Binary convolution. Both inputs and weights are binary (+1 or -1)
    """


class BinaryDenseLayer(lasagne.layers.DenseLayer):
    """Binary version of fully connected layer. XNOR and bitcount ops are used for 
    this in a similar fashion as that of Conv Layer.
    """

    

def xnor_net_find_gradiants(net, loss):
    """ Method to compute gradiants of all layers for back propagation.
    This is similar to the method in BinaryNet implementation.
    """
