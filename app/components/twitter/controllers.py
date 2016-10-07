# Import flask dependencies
from flask import Blueprint, jsonify, request, send_from_directory
from app.utils import TwitterHelper
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
twitterComponent = Blueprint('auth', __name__, url_prefix='/twitter')


# Set the route and accepted methods
@twitterComponent.route('/', methods=['GET'])
def index():
	return send_from_directory("templates/twitter", "index.html")


@twitterComponent.route('/api/bestTimeAndDay', methods=['POST'])
def bestTimeAndDay():
	try:
		requestData = json.loads(request.get_data())

		if (requestData["userId"] == "" and requestData["userName"] == "") or (
						requestData["userId"] != "" and requestData["userName"] != ""):
			return jsonify({"success": False, "error": {"message": "Invalid Input", "code": 201}})

		userIdOrName = requestData["userId"]
		if userIdOrName == "":
			userIdOrName = requestData["userName"]

		timeAndDay = TwitterHelper.getBestTimeAndDay(userIdOrName)

		if timeAndDay is None or ("time" not in timeAndDay and "day" not in timeAndDay):
			raise Exception("Problem in fetching tweeter data")

		responseData = {
			"time": str(timeAndDay["time"]) + ":00-" + str(timeAndDay["time"]) + ":59",
			"day": timeAndDay["day"]
		}
		return jsonify({"success": True, "data": responseData})
	except Exception as e:
		return jsonify({"success": False, "error": {"message": "Internal Server Error: " + str(e), "code": 101}})
