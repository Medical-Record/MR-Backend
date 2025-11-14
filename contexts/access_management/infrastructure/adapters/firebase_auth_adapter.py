import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar variables de entorno
load_dotenv()

# Obtener la ruta del archivo de credenciales desde el .env
CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")

if not CREDENTIALS_PATH:
    raise ValueError("FIREBASE_CREDENTIALS_PATH no está configurado en .env")

# Inicializar Firebase si no está ya inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)

# Cliente Firestore
db = firestore.client()
