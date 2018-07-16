import sys 
from website import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
	manager.run()
