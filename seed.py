import os
import json
from app import app
from models.db import db
from models.client import Client

DATA_DIR = 'data'

def populate_clients(data):
    created = 0
    for item in data:
        name = item.get('name')
        email = item.get('email')
        phone = item.get('phone')

        if not name or not email or not phone:
            continue

        exists = Client.query.filter(
            (Client.email == email) | (Client.phone == phone)
        ).first()

        if exists:
            continue

        client = Client(name=name, email=email, phone=phone)
        db.session.add(client)
        created += 1

    return created

def populate_all():
    with app.app_context():
        print("Entrando en el contexto de la app...")
        for filename in os.listdir(DATA_DIR):
            print(f"Revisando archivo: {filename}")
            if not filename.endswith('.json'):
                print(f"Archivo ignorado: {filename}")
                continue

            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print(f"Datos cargados desde {filename}: {data}")

            if 'clients' in filename:
                created = populate_clients(data)
                print(f'{created} clientes cargados desde {filename}')
            else:
                print(f'Se ignoró el archivo {filename}, tipo desconocido.')

        print("Haciendo commit a la base de datos...")
        db.session.commit()


if __name__ == '__main__':
    populate_all()
