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

def concatenate(M1, M2):
    return np.concatenate([M1, M2], axis = horizontal_axis)

def create_bias(M):
    m, n = get_dimensions(M)
    return np.ones((m,1))
    
def add_bias(M):
    bias = create_bias(M)
    return concatenate(bias, M)
    
def multiply(M1, M2):
    return np.dot(M1, M2)
    
def transpose(M):
    return np.transpose(M)

def inverse(M):
    return np.linalg.inv(M)

def calc_hypothesis(theta, X):
    thetaT = transpose(theta)
    result = multiply(X, thetaT)
    return result
    
def calc_theta_closed_form(X, y):
    XT = transpose(X)
    result = multiply(XT, X)
    result = inverse(result)
    result = multiply(result, XT)
    result = multiply(result, y)
    return result

def initialize_theta(X):
    m, n = get_dimensions(X)
    return np.ones((n))
    
def calc_sum_of_squared_errors(w, X, y):
    m, n = get_dimensions(X)
    result = 0
    for i in range(1, m):
        result += (y[i] - calc_hypothesis(w, X[i])) ** 2
    result = result / 2
    return result

def standardize(data):
    mean = np.mean(data)
    standard_diviation = np.std(data)
    
    for x in range(len(data)):
        data[x] = (data[x] - mean) / standard_diviation



# =========================================================================== #
# HELPER FOR DOCUMENTATION ================================================== #
# =========================================================================== #

def latex_column(name, x, column):
    x = to_array(x)
    x = x[:, column]
    latex_matrix(name, x)

def latex_matrix(name, x):
    x = to_array(x)
    dimensions = get_dimensions(x)
    m = dimensions[0]
    try:
        n = dimensions[1]
    except IndexError:
        n = -1
    
    print(name + " = \\begin{pmatrix}")
    for i in range(m):
        temp = ""
        
        if n == -1:
            temp = temp + str(x[i])
        else:
            for j in range(n):
                if j == (n - 1):
                    temp = temp + str(x[i][j])
                else:
                    temp = temp + str(x[i][j]) + " && "
            

        if i == (m - 1):
           print(temp)
        else:
           print(temp + " \\\\")

    print("\\end{pmatrix}")
    print("")
