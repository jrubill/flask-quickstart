from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from website.config import Config 
from flask_migrate import Migrate

migrate = Migrate() # Perform migrations on our db
db = SQLAlchemy() # our connection to our db

bcrypt = Bcrypt() # Encryption
login_manager = LoginManager() # Managing logins

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	migrate.init_app(app, db)

	from website.main.routes import main

	app.register_blueprint(main)

	return app
