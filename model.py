import re
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from db import fetch_tweets

def preprocess_text(text):
    text = text.lower() 
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  
    text = re.sub(r"\@\w+|\#", "", text)  
    text = re.sub(r"[^\w\s]", "", text)  
    text = re.sub(r"\d+", "", text)  
    text = text.strip()
    return text

def load_data():
    data = fetch_tweets()
    df = pd.DataFrame(data)
    if df.empty:
        return None, None
    df["text"] = df["text"].apply(preprocess_text)
    X = df["text"]
    y = df["positive"]  
    return X, y

def train_model():
    X, y = load_data()
    if X is None:
        print("Aucune donnée trouvée pour l'entraînement.")
        return
    
    vectorizer = TfidfVectorizer(max_features=5000)
    X_tfidf = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Précision du modèle : {accuracy:.2f}")

    joblib.dump(model, "sentiment_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("Modèle et vectorizer sauvegardés.")

def load_model():
    try:
        model = joblib.load("sentiment_model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
        return model, vectorizer
    except FileNotFoundError:
        print("Modèle non trouvé. Veuillez l'entraîner en exécutant train_model().")
        return None, None

if __name__ == "__main__":
    train_model()  
