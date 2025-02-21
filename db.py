import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",  
    "password": "root",  
    "database": "sentiment_db"
}

def create_connection():
    """ Établit la connexion avec MySQL """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Erreur de connexion à MySQL : {e}")
        return None

def create_table():
    """ Crée la table tweets si elle n'existe pas """
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tweets (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    text TEXT NOT NULL,
                    positive TINYINT(1),
                    negative TINYINT(1)
                )
            """)
            conn.commit()
            print("Table 'tweets' créée avec succès !")
        except Error as e:
            print(f"Erreur lors de la création de la table : {e}")
        finally:
            cursor.close()
            conn.close()

def insert_tweet(text, positive, negative):
    """ Insère un tweet annoté dans la base de données """
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tweets (text, positive, negative) VALUES (%s, %s, %s)",
                (text, positive, negative)
            )
            conn.commit()
            print("Tweet inséré avec succès !")
        except Error as e:
            print(f"Erreur lors de l'insertion du tweet : {e}")
        finally:
            cursor.close()
            conn.close()

def fetch_tweets():
    """ Récupère les tweets annotés pour entraîner le modèle """
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT text, positive, negative FROM tweets")
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur lors de la récupération des tweets : {e}")
            return []
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_table()  
