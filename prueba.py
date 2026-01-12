from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bcrypt
import getpass

load_dotenv()

# Conexión a MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
MONGO_DB = os.getenv("MONGO_DB")  # Nombre de tu base de datos
db = client[MONGO_DB]
collection = db["AdminUsers"]

def crear_usuario():
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")

    if not email or not password:
        print("❌ Email y password son obligatorios")
        return

    # Verificar si el usuario ya existe
    if collection.find_one({"email": email}):
        print("⚠️ El usuario ya existe")
        return

    # 🔐 Hashear contraseña
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Guardar en MongoDB
    user = {
        "email": email,
        "password": hashed_password.decode("utf-8")
    }

    collection.insert_one(user)
    print("✅ Usuario creado correctamente")

if __name__ == "__main__":
    crear_usuario()
