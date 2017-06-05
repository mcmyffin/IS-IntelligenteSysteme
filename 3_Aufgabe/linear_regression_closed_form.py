#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ISP 3: Lineare Regression mit abgeschlossener Lösung
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from helper import *
import numpy as np

class LinearRegression(object):
    """Linear Regression Model

    Diese Klasse trainiert ein lineares Regressionsmodell mittels abgeschlossener Lösung
    """

    def fit(self, X, y):
        """Training des Modells anhand gegebener Trainingsdaten

        Args:
          X: Matrix der Trainingsdaten in der Form [n_samples, n_features]
          y: Vektor der Zielvariablen in der Form [n_samples]

        Returns:
          self: Modell mit trainierten Gewichten
        """
        # Erweitern der Dimension von X falls X nur ein Feature beinhaltet
        # [n_samples] -> [n_samples, 1]
        if len(np.shape(X)) < 2:
            X = np.reshape(X, (np.shape(X)[0], 1))

        # X um Bias-Term ergänzen
        # damit sollte X die Form [n_samples, n_features + 1] bekommen   
        X = add_bias(X)
        
        # Bestimmung der Gewichte mittels abgeschlossener Lösung
        # self.weights in der Form [n_features + 1]
        self.weights = calc_theta_closed_form(X, y)
        
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
