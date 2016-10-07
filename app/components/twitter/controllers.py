# Import flask dependencies
from flask import Blueprint, jsonify, request, send_from_directory
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
twitterComponent = Blueprint('auth', __name__, url_prefix='/twitter')


# Set the route and accepted methods
@twitterComponent.route('/', methods=['GET'])
def index():
	return send_from_directory("templates/twitter", "index.html")


@twitterComponent.route('/api/bestTimeAndDay', methods=['POST'])
def getBestTimeAndDay():
	responseData = {}
	requestData = json.loads(request.get_data())

	if (requestData["userId"] == "" and requestData["userName"] == "") or (
			requestData["userId"] != "" and requestData["userName"] != ""):
		return jsonify({"success": False, "error": {"message": "Invalid Input", "code": 102}})

	responseData = {
		"time": "09:00-09:59",
		"day": "Sunday"
	}

	return jsonify({"success": True, "data": responseData})
