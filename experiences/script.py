"""
Petit script pour traiter les expériences de démoulage de petit suisse

"""

import numpy as np
import matplotlib.pyplot as plt

# Lecture des données
date,temps = np.loadtxt('demoulage.txt',unpack=True)


# Affichage et sauvegarde

plt.plot(date,temps,'o',label='Données')
plt.grid()
plt.legend()
plt.savefig('donnees_demoulage.png')
plt.clf()
