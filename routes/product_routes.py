from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.product import Product

product = Blueprint('product', __name__)

# Obtener todos los productos
@product.route('/api/products')
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])

# Agregar un nuevo producto
@product.route('/api/add_product', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data or not all(key in data for key in ['name', 'price', 'stock']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    try:
        print(f"Datos recibidos: {data}")

        new_product = Product(data['name'], data['price'], data['stock'])
        print(f"Creando producto: {new_product.name}, {new_product.price}, {new_product.stock}")

        db.session.add(new_product)
        db.session.commit()

        return jsonify({'message': 'Producto agregado exitosamente', 'product': new_product.serialize()}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'El producto ya existe o hay un conflicto de integridad'}), 400

    except Exception as e:
        db.session.rollback()
        print(f"Error inesperado: {e}")
        return jsonify({'error': 'Error al agregar el producto'}), 500

# Eliminar un producto
@product.route('/api/del_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Producto eliminado exitosamente'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Actualizar un producto (PUT)
@product.route('/api/up_product/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se recibieron datos'}), 400

    product = Product.query.get(id)

    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404

    try:
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            product.price = data['price']
        if 'stock' in data:
            product.stock = data['stock']

        db.session.commit()
        return jsonify({'message': 'Producto actualizado correctamente', 'product': product.serialize()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Actualización parcial de producto (PATCH)
@product.route('/api/update_product/<int:id>', methods=['PATCH'])
def patch_product(id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se recibieron datos'}), 400

    product = Product.query.get(id)

    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404

    try:
        if 'name' in data and data['name']:
            product.name = data['name']
        if 'price' in data and data['price'] is not None:
            product.price = data['price']
        if 'stock' in data and data['stock'] is not None:
            product.stock = data['stock']

        db.session.commit()
        return jsonify({'message': 'Producto actualizado correctamente', 'product': product.serialize()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500