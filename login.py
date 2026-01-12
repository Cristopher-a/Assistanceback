from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bcrypt
import getpass

load_dotenv()

# Conexión a MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
MONGO_DB = os.getenv("MONGO_DB")
db = client[MONGO_DB]
collection = db["AdminUsers"]

def verificar_usuario(email, password): 

    if not email or not password:
        print("❌ Email y password son obligatorios")
        return

    # Buscar usuario por email
    user = collection.find_one({"email": email})
    if not user:
        print("❌ Usuario no encontrado")
        return

    # Comparar contraseña usando bcrypt
    if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        print(f"✅ Login exitoso. Bienvenido {email}!")
        # Aquí puedes retornar user, generar token, etc.
        return True
    else:
        print("❌ Contraseña incorrecta")
        return False

if __name__ == "__main__":
    email1 = input("Email: ").strip()
    password1 = getpass.getpass("Password: ")
    verificar_usuario(email1, password1)
