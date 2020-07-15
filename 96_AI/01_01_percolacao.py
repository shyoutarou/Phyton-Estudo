import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import random as rd


def grille(n, p):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if rd.random() < p:
                grille[i, j] = 1
    return grille


echelle = ListedColormap(['gray', 'aqua', 'white'])


def affiche_grille(grille):
    plt.clf()
    plt.imshow(grille, cmap=echelle)


def propage(grille, i, j):
    n = len(grille)
    g = max(0, j - 1)
    d = min(n - 1, j + 1)
    h = max(0, i - 1)
    b = min(n - 1, i + 1)
    if grille[i, j] == 1 and (grille[i, g] == .5 or grille[i, d] == .5 or grille[h, j] == .5 or grille[b, j] == .5):
        grille[i, j] = .5
    return 0


def percolation(grille):
    n = len(grille)
    affiche_grille(grille)
    plt.show()
    for j in range(n):
        grille[0, j] = min(.5, grille[0, j])
    affiche_grille(grille)
    plt.draw();
    plt.pause(.1)
    for i in range(1, n):
        for j in range(n):
            propage(grille, i, j)
        affiche_grille(grille)
        plt.draw();
        plt.pause(.1)

    plt.title("Percolacao")
    plt.savefig("plot_percolacao_example.png")
    return 0

grille = grille(5, 5)
percolation(grille)