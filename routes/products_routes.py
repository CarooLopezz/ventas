# cada endpoint realizeun actividad
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models.db import db
from models.products import Product
from models.category import Category

product = Blueprint('product', __name__)

@product.route('/api/add_product', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data or not all(key in data for key in ['name', 'price', 'stock', 'category_id']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    try:
        print(f"Datos recibidos: {data}")  # Ver los datos que llegan

        # Validar que la categoría exista
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'error': 'Categoría no encontrada'}), 404

        # Crear el producto
        new_product = Product(
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            category_id=data['category_id']
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            'message': 'Producto agregado exitosamente',
            'product': new_product.serialize()
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Error de integridad al guardar el producto'}), 400
