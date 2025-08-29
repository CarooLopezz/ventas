from flask import Flask
from config.config import DATABASE_CONNECTION_URI
from models.db import db
from models.client import Client
from models.category import Category
from models.products import Product
from models.provider import Provider
from models.sales import Sale
from routes.client_routes import client
from routes.products_routes import product
from routes.provider_routes import provider
from routes.sales_routes import sales


app = Flask(__name__)# con isntancia app levanta el servidor  para utilizar los objetos pip manejador de paquete

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(client)
app.register_blueprint(product)
app.register_blueprint(provider)
app.register_blueprint(sales)

with app.app_context():
    from models.client import Client
    from models.products import Product
    from models.sales import Sale
    from models.provider import Provider
    from models.category import Category
    
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003,debug=True) 