from datetime import datetime
import firebase_admin
from firebase_admin import credentials,db
from typing import Dict, Any

class FirebaseSender:
    def __init__(self, credentials_path: str, db_url: str):
        #costruttore
        try:
            cred = credentials.Certificate(credentials_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': db_url
            })
            print("Firebase inizializzato con successo.")
        except Exception as e:
            print(f"Errore durante l'inizializzazione di Firebase: {e}")
            raise

    def send_gps_data(self, data: Dict[str, Any]):
        #usa timestamp come chiave
        try:
            ref = db.reference('gps_data')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ref.child(timestamp).set(data)
            print(f"Dati GPS inviati con successo alle {timestamp}.")
        except Exception as e:
            print(f"Errore durante l'invio dei dati a Firebase: {e}")