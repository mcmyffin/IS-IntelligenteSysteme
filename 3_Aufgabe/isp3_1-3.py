#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ISP 3: Lineare und logistische Regression

# Aufgabe 1.3: Vorhersage von Immobilienpreisen

Dieses Skript läd einen Datensatz zur Vorhersage von Immobilienpreisen
mittels linearer Regression.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from helper import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Laden des Datensatzes als Pandas DataFrame
df = pd.read_csv("./data/immo.txt", sep=",", dtype="float64")

# Plot der Daten
sc = plt.scatter(df["size"], df["price"], c=df["rooms"], cmap="Reds")
cb = plt.colorbar(sc)
cb.set_label("Bedrooms")
cb.set_ticks(range(1,6))
plt.xlabel("Size in $ft^2$")
plt.ylabel("Price in $USD$")
plt.show()


# Standartisierung der Daten
df_norm = np.copy(df)
standardize(df["size"])
standardize(df["rooms"])
standardize(df["price"])
df_norm = np.array(df)

# Trainingsdaten und Zielvariablen definieren
y = df_norm[:,2]
X = np.delete(df_norm, 2, axis = horizontal_axis)

# Training des Modells
from linear_regression_sgd import LinearRegression
model = LinearRegression()
model = model.fit(X,y, alpha=0.01, iterations=100)


# Plot der Error-Kurve über das Training
plt.plot(model.cost, 'r')
plt.show()

# Approximation der Daten
y_approx = model.predict(X)

# Plot der Daten
sc = plt.scatter(X[:,0], y, c=X[:,1], cmap="Reds")
cb = plt.colorbar(sc)
cb.set_label("Bedrooms")
# cb.set_ticks(range(1,6))
plt.xlabel("Size")
plt.ylabel("Price")
plt.plot(X[:,0], y_approx, "bo")
plt.show()
