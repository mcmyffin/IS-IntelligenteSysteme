#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ISP 3: Lineare Regression mit Stochastic Gradient Descent (SGD)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from helper import *
import numpy as np
    
class LinearRegression(object):
    """Linear Regression Model

    Diese Klasse trainiert ein lineares Regressionsmodell mittels SGD
    """

    def __init__(self, random_seed=1):
        self.random_seed = random_seed


    def fit(self, X, y, alpha=0.001, iterations=1000):
        """Training des Modells anhand gegebener Trainingsdaten

        Args:
          X: Matrix der Trainingsdaten in der Form [n_samples, n_features]
          y: Vektor der Zielvariablen in der Form [n_samples]
          alpha: Lernrate des Gradientenverfahrens
          iterations: Anzahl der Iterationen von SGD über die Daten X

        Returns:
          self: Modell mit trainierten Gewichten
        """
        # Erweitern der Dimension von X falls X nur ein Feature beinhaltet
        # [n_samples] -> [n_samples, 1]
        if len(np.shape(X)) < 2:
            X = np.reshape(X, (np.shape(X)[0], 1))

        # m Samples mit n Attributen (exclusive Bias)
        m, n = np.shape(X)

        # X um Bias-Term ergänzen
        # damit sollte X die Form [n_samples, n_features + 1] bekommen
        X = add_bias(X)

        # Initialisierung der Gewichte (inklusive Bias-Term)
        # self.weights in der Form [n_features + 1]
        self.weights = calc_theta_closed_form(X, y)

        # Array zum Speichern des Errors für jeden SGD-Schritt
        self.cost = []

        # SGD Schleife über Iterationen
        for _ in range(iterations):
            # Schleife über Datensätze
            for i in range(m):

                # Update der Gewichte
                # Schleife über Parameter (n+1 durch Bias-Term)
                for j in range(n+1):
                    temp = y[i] - calc_hypothesis(self.weights, X[i])
                    self.weights[j] = self.weights[j] + alpha * temp * X[i][j]

            # Berechne SSE des SGD-Schritts mit den aktuallisierten Gewichten
            self.cost = self.cost + [calc_sum_of_squared_errors(self.weights, X, y)]

        return self
    
    def predict(self, X):
        """Vorhersage der Zielvariable

        Args:
          X: Matrix der Attribute pro Datensatz in der Form [n_samples, n_features]
        Returns:
          Array der vorhergesagten Zielvariablen in der Form [n_samples]
        """
        # X um Bias-Term ergänzen
        # damit sollte X die Form [n_samples, n_features + 1] bekommen
        X = add_bias(X)
        
        # Berechnen der Zielvariablen über die Hypothese
        return calc_hypothesis(self.weights, X)
