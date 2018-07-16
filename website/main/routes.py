from flask import render_template, Blueprint
main = Blueprint('main', __name__)

@main.route("/main", methods=['GET'])
def home():
	return "Main"


