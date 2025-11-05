import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import json

load_dotenv()
cred = credentials.Certificate(os.getenv('FIREBASE_PATH_NAME'))
app = firebase_admin.initialize_app(cred)
db_gps = db.reference("/") #All data to be stored must be in JSON format

def pushToDatabase():
