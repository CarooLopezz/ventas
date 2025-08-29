# routes/provider_routes.py
from flask import Blueprint, request, jsonify
from models.provider import Provider
from models.db import db
from sqlalchemy.exc import IntegrityError

provider = Blueprint('provider', __name__)

# GET - Ver todos los proveedores
@provider.route('/api/providers')
def get_providers():
    providers = Provider.query.all()
    return jsonify([p.serialize() for p in providers])

# POST - Agregar proveedor
@provider.route('/api/add_provider', methods=['POST'])
def add_provider():
    data = request.get_json()

    if not data or not all(key in data for key in ['name', 'email', 'phone']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    try:
        new_provider = Provider(data['name'], data['email'], data['phone'])
        db.session.add(new_provider)
        db.session.commit()

        return jsonify({
            'message': 'Proveedor agregado exitosamente',
            'provider': new_provider.serialize()
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'El email ya está registrado'}), 400
