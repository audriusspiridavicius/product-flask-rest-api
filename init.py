from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///./products.db"

db.init_app(app)
migrate.init_app(app,db)

from model.product import Product






