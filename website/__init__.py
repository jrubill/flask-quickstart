from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.config import Config 
from flask_migrate import Migrate

migrate = Migrate() # Perform migrations on our db
db = SQLAlchemy() # our connection to our db

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	migrate.init_app(app, db)

	from website.main.routes import main

	app.register_blueprint(main)

	return app
