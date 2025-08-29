# routes/client_routes.py

import os  # <--- agregado para poder ubicar el archivo
from flask import Blueprint, request, jsonify
from models.db import db
from models.client import Client
from sqlalchemy.exc import IntegrityError

client = Blueprint('client', __name__)

@client.route('/api/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients])

