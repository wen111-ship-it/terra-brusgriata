import matplotlib.pyplot as plt
import numpy as np
import pytest as pt

rng = np.random.default_rng()  # Crée un générateur de nombres aléatoires
def creer_foret(hauteur, largeur, densite, rng):
    """Renvoie une grille où chaque case est ARBRE avec une probabilité densite, VIDE sinon."""
    foret = np.zeros((hauteur, largeur), dtype=int)  # Crée une grille vide
    for i in range(hauteur):
        for j in range(largeur):
            if rng.random() < densite:
                foret[i, j] = 1  # Place un arbre
    return foret
foret = creer_foret(10, 10, 0.3, rng)
print(foret)