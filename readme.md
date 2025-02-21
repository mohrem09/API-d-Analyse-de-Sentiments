# Sentiment Analysis API

## Description
Cette application Flask analyse le sentiment des tweets en utilisant un modèle de machine learning basé sur la régression logistique. Elle comprend plusieurs modules :

- **`app.py`** : API Flask qui reçoit des tweets, les prétraite et renvoie leur score de sentiment.
- **`db.py`** : Gestion de la base de données MySQL pour stocker et récupérer les tweets annotés.
- **`model.py`** : Entraînement et gestion du modèle de machine learning.
- **`train.py`** : Script pour entraîner le modèle à partir des données stockées en base.

---

## Installation et Configuration

### Prérequis
- Python 3.x
- Flask
- MySQL
- scikit-learn
- pandas
- joblib

### Installation des dépendances
```bash
pip install flask mysql-connector-python scikit-learn pandas numpy joblib
```

### Configuration de la base de données

1. Assurez-vous d'avoir un serveur MySQL en cours d'exécution.
2. Modifiez `DB_CONFIG` dans `db.py` pour correspondre à vos identifiants MySQL.
3. Exécutez :
   ```bash
   python db.py
   ```
   Cela créera la table nécessaire dans votre base de données.

---

## Utilisation

### 1. Entraînement du modèle
Exécutez la commande suivante pour entraîner le modèle :
```bash
python train.py
```
Cela va :
- Récupérer les tweets annotés depuis la base de données.
- Nettoyer et vectoriser les données.
- Entraîner un modèle de régression logistique.
- Sauvegarder le modèle et le vectorizer.

### 2. Lancement de l'API Flask
Démarrez le serveur Flask avec :
```bash
python app.py
```
Par défaut, l'API tourne sur `http://127.0.0.1:5000`.

### 3. Analyse des sentiments
Envoyez une requête POST à `/analyze` avec une liste de tweets :
```json
{
  "tweets": ["J'adore ce produit !", "Ce service est horrible."]
}
```
Réponse :
```json
{
  "J'adore ce produit !": {"score": 0.85, "sentiment": "positif"},
  "Ce service est horrible.": {"score": 0.20, "sentiment": "négatif"}
}
```

---

## Structure du Projet

```
.
├── app.py        # API Flask
├── db.py         # Gestion de la base de données
├── model.py      # Modèle ML et préprocessing
├── train.py      # Script d'entraînement
├── sentiment_model.pkl  # Modèle entraîné
├── vectorizer.pkl       # Vectorizer entraîné
```

---

## Améliorations Futures
- Ajouter une interface utilisateur pour la visualisation des résultats.
- Implémenter un système de feedback pour améliorer le modèle.
- Intégrer un pipeline de déploiement avec Docker et CI/CD.

---

## Auteur
Développé par : [Mohamed REMMACHE](https://mohamed-remmache-portfilio.netlify.app/)
