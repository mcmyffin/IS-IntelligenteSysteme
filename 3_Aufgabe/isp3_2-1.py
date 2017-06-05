#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ISP 3: Lineare und logistische Regression

# Aufgabe 2.1 - Logistische Regression mit SGD

Dieses Skript beinhaltet einen Dummy-Datensatz Trainieren und Testen
eines Regressions-Modells.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from helper import *
import numpy as np
import matplotlib.pyplot as plt

from logistic_regression import LogisticRegression

# Configure classes
classes = [
    [0, "ro" , "Reds"],
    [1, "go" , "Greens"]
]


# Load Dataset
data = np.loadtxt("./data/classify.txt", delimiter=",")

X = data[:,:2]
y = data[:,2]


# Plot Dataset
def plot_dataset(number, color, color_map):
    plt.plot([X[i,0] for i in range(len(X)) if y[i] == number], [X[i,1] for i in range(len(X)) if y[i] == number], color)

print("Plotting dataset...")
for number, color, color_map in classes:
    plot_dataset(number, color, color_map)
plt.show()


for _class in classes:
    # Training des Modells
    number, color, color_map = _class
    _y = np.vectorize(lambda t: 1 if t == number else 0)(y)
    
    model = LogisticRegression()
    model.fit(X, _y, alpha=0.01, iterations=100)
    
    _class.append(model)
    
    
    # Plot der Error-Kurve über das Training
    print("Plotting error for class '" + str(number) + "'...")
    plt.plot(model.cost, 'r')
    plt.show()


# Plot der Klassifikation mit Decision-Boundary
print("Plotting classifying...")
f, ax = plt.subplots(figsize=(8.0 + len(classes) * 1.5, 6.0))

for number, color, color_map, model in classes:
    # Testdaten zur Visualisierung der Decision-Boundary
    xx, yy = np.mgrid[-10:10:.01, -10:10:.01]
    grid = np.c_[xx.ravel(), yy.ravel()]
    probs = model.predict(grid).reshape(xx.shape)
    
    
    # Plot der Klassifikation mit Decision-Boundary
    contour = ax.contourf(xx, yy, probs, 25, cmap=color_map, vmin=0, vmax=1, alpha = 1.0 / len(classes))
    ax_c = f.colorbar(contour)
    ax_c.set_label("$P(y = " + str(number) + ")$")
    ax_c.set_ticks([0, .25, .5, .75, 1])
    ax.set(xlim=(-3.5, -0.5), ylim=(-6, 6),
           xlabel="$X_1$", ylabel="$X_2$")
    ax.plot(alpha = 1.0 / len(classes))
    plot_dataset(number, color, color_map)
    
plt.show()
