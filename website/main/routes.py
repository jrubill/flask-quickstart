from flask import render_template, Blueprint
main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def index():
	return "Main"


