#!/bin/bash

# Définition de l'environnement Python si nécessaire
source venv/bin/activate  # Active l'environnement virtuel (si utilisé)

# Exécution du script d'entraînement
python train.py

# Désactive l'environnement virtuel après l'exécution (si nécessaire)
deactivate
