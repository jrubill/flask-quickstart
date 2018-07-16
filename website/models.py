from site import db, login_manager
from flask_login import UserMixin

# required by the login manager
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Sample user class
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.column(db.String(40), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return "User({}, {})".format(self.id, self.username)
