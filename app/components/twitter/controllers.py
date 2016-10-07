# Import flask dependencies
from flask import Blueprint, jsonify, request, send_from_directory

# Define the blueprint: 'auth', set its url prefix: app.url/auth
twitterComponent = Blueprint('auth', __name__, url_prefix='/twitter')


# Set the route and accepted methods
@twitterComponent.route('/', methods=['GET'])
def index():
	return send_from_directory("templates/twitter", "index.html")


@twitterComponent.route('/api/getBestTimeAndDay', methods=['POST'])
def getBestTimeAndDay():
	responseData = {}
	return jsonify({"success": True, "data": responseData})
