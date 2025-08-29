import os
import json
from datetime import datetime
from app import app
from models.db import db
from models.client import Client
from models.sales import Sale
from models.products import Product
from models.provider import Provider  # 👈 Import del modelo

DATA_DIR = 'data'

def populate_clients(data):
    created = 0
    for item in data:
        name = item.get('name')
        email = item.get('email')
        phone = item.get('phone')

        if not name or not email or not phone:
            print("Faltan datos en cliente, se salta.")
            continue

        exists = Client.query.filter(
            (Client.email == email) | (Client.phone == phone)
        ).first()

        if exists:
            print("Ya existe cliente, se salta:", email)
            continue

        client = Client(name=name, email=email, phone=phone)
        db.session.add(client)
        created += 1

    return created

def populate_sales(data):
    created = 0
    for item in data:
        if not all(k in item for k in ['client_id', 'date', 'discount', 'total_amount']):
            print("Faltan campos en venta, se salta.")
            continue

        try:
            date = datetime.strptime(item["date"], "%Y-%m-%d")
        except:
            print("Formato de fecha inválido")
            continue

        sale = Sale(
            client_id=item["client_id"],
            date=date,
            discount=item["discount"],
            total_amount=item["total_amount"]
        )
        db.session.add(sale)
        created += 1

    return created

def populate_products(data):
    created = 0
    for item in data:
        if not all(k in item for k in ['name', 'price', 'stock', 'category_id']):
            print("Faltan campos en producto, se salta.")
            continue

        product = Product(
            name=item['name'],
            price=item['price'],
            stock=item['stock'],
            category_id=item['category_id']
        )
        db.session.add(product)
        created += 1

    return created

def populate_providers(data):  # 👈 Nuevo loader para Provider
    created = 0
    for item in data:
        name = item.get('name')
        email = item.get('email')
        phone = item.get('phone')

        if not name or not email or not phone:
            print("Faltan datos en proveedor, se salta.")
            continue

        exists = Provider.query.filter(
            (Provider.email == email) | (Provider.phone == phone)
        ).first()

        if exists:
            print("Ya existe proveedor, se salta:", email)
            continue

        provider = Provider(name=name, email=email, phone=phone)
        db.session.add(provider)
        created += 1

    return created

# loader para decidir qué función usar por archivo
loaders = {
    'clients': populate_clients,
    'sales': populate_sales,
    'products': populate_products,
    'providers': populate_providers  # 👈 Agregado aquí
}

def populate_all():
    with app.app_context():
        print("Entrando en el contexto de la app...")
        for filename in os.listdir(DATA_DIR):
            if not filename.endswith('.json'):
                print(f"Archivo ignorado: {filename}")
                continue

            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print(f"Datos cargados desde {filename}")

            loaded = False
            for key, func in loaders.items():
                if key in filename:
                    created = func(data)
                    print(f"{created} registros cargados desde {filename}")
                    loaded = True
                    break

            if not loaded:
                print(f"Archivo sin loader definido: {filename}")

        print("Haciendo commit a la base de datos...")
        db.session.commit()

if __name__ == '__main__':
    populate_all()
