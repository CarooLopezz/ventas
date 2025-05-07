from flask import Blueprint, jsonify, request
from models.sales import Sale, SaleItem
from models.db import db
from datetime import datetime

sales = Blueprint('sales', __name__)

@sales.route('/api/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    return jsonify([sale.serialize() for sale in sales])

@sales.route('/api/sales', methods=['POST'])
def add_sales():
    data = request.get_json()
    required_fields = ['client_id', 'date', 'discount', 'total_amount', 'items']
    if not data or not all (key in data for key in required_fields):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    try:
        date = datetime.strptime(data["date"], "%Y-%m-%d")

        sale = Sale(
            client_id=data["client_id"],
            date=date,
            discount=data["discount"],
            total_amount=data["total_amount"],
        )
        for Item_data in data['items']:
            item= SaleItem(
                sale=sale,
                product_name=Item_data['product_name'],
                unit_price=Item_data['unit_price'],
                quantity=Item_data['quantity']
            )
            db.session.add(item)

        db.session.add(sale)
        db.session.commit()
        return jsonify(sale.serialize()),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify ({"error": str(e)}), 500