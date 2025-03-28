from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

# Obtener la ruta base del proyecto (directorio donde ejecutas `uvicorn`)
BASE_DIR = Path.cwd()
CREDENTIALS_PATH = BASE_DIR / "config" / "firebase_credentials.json"

# Inicializar Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(str(CREDENTIALS_PATH))
    firebase_admin.initialize_app(cred)

# Cliente Firestore
db = firestore.client()
