# Ready to Deploy Flask Application

This is meant to serve as a **_starting point_** for rapid development of somewhat complex Flask Applications.

## What Comes Pre-Configured:
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-Bcrypt](http://flask-bcrypt.readthedocs.io/en/latest/)
- [Flask-Migrate](http://flask-migrate.readthedocs.io/en/latest/)
- [Flask-Script](http://flask-script.readthedocs.io/en/latest/)

## What You'll Need:
1. Depending on what type of database you use, you'll probably need the correct Python extension in order to use it (unless you're using sqlite).
2. Please change the secret key in the config.py, and on deployment, turn the debug flag off.

