import os
from pymongo import MongoClient
from dotenv import load_dotenv
def obtener_historial_de_archivos():
        load_dotenv()
        MONGO_URI = os.getenv("MONGO_URI")
        MONGO_DB = os.getenv("MONGO_DB")

        if not all([MONGO_URI, MONGO_DB]):
            raise ValueError("❌ Falta la URI o el nombre de la base de datos de MongoDB")
    # 🔹 Conexión a MongoDB
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]
        colecciones = [c for c in db.list_collection_names() if c not in ["Employee", "AdminUsers"]]
        return colecciones

if __name__ == "__main__":
    colecciones = obtener_historial_de_archivos()
    print("Colecciones disponibles (excluyendo 'Employee' y 'AdminUsers'):")
    for coleccion in colecciones:
        print(f"- {coleccion}")