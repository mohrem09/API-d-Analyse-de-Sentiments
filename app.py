from flask import Flask, request, jsonify
import joblib
import numpy as np
from model import preprocess_text 

app = Flask(__name__)


model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl") 

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:

        data = request.get_json()
        
        if not data or "tweets" not in data:
            return jsonify({"error": "Données invalides, liste de tweets requise"}), 400
        
        tweets = data["tweets"]
        
        if not isinstance(tweets, list) or len(tweets) == 0:
            return jsonify({"error": "Liste de tweets vide ou invalide"}), 400
        
        processed_tweets = [preprocess_text(tweet) for tweet in tweets]
        
        
        X_tfidf = vectorizer.transform(processed_tweets)  

        
        predictions = model.predict(X_tfidf)
        scores = model.predict_proba(X_tfidf)[:, 1]  

        
        response = {
            tweets[i]: {
                "score": float(scores[i]),
                "sentiment": "positif" if scores[i] >= 0.5 else "négatif"
            }
            for i in range(len(tweets))
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    try:
        
        data = request.get_json()
        
        if not data or "tweets" not in data:
            return jsonify({"error": "Données invalides, liste de tweets requise"}), 400
        
        tweets = data["tweets"]
        
        if not isinstance(tweets, list) or len(tweets) == 0:
            return jsonify({"error": "Liste de tweets vide ou invalide"}), 400
        
        
        processed_tweets = [preprocess_text(tweet) for tweet in tweets]
        
        
        X_tfidf = vectorizer.transform(processed_tweets)  

        
        predictions = model.predict(X_tfidf)
        scores = model.predict_proba(X_tfidf)[:, 1]  

        
        response = {tweets[i]: float(scores[i]) for i in range(len(tweets))}
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
