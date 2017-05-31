#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ISP 3: Hilfsfunktionen
"""

import numpy as np

vertical_axis = 0
horizontal_axis = 1

def to_array(M):
    return np.array(M)
    
def get_dimensions(M):
    return np.shape(M)

def add_bias(M):
    # np.insert(input, index, value, axis)
    return np.insert(M, 0, 1, horizontal_axis)

def multiply(M1, M2):
    return np.dot(M1, M2)
    
def transpose(M):
    return np.transpose(M)

def inverse(M):
    return np.linalg.inv(M)

def calcWeightsClosedForm(X, y):
    XT = transpose(X)
    result = multiply(XT, X)
    result = inverse(result)
    result = multiply(result, XT)
    result = multiply(result, y)
    return result

def calcPrediction(theta, X):
    thetaT = transpose(theta)
    result = multiply(X, thetaT)
    return result