from flask import Blueprint, jsonify, request, send_from_directory
from app.utils import TwitterHelper
import json

# Define the blueprint: 'twitterComponent', set its url prefix: /twitter
twitterComponent = Blueprint('twitterComponent', __name__, url_prefix='/twitter')


# Set the route and accepted methods
@twitterComponent.route('/', methods=['GET'])
def index():
	return send_from_directory("templates/twitter", "index.html") #this is our frontend file, taking inputs, hitting our api through ajax


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

		if timeAndDay is None or ("time" not in timeAndDay and "day" not in timeAndDay) or (
				timeAndDay["time"] == -1 and timeAndDay["day"] == ""):
			raise Exception("Problem in fetching tweeter data")

		responseData = {
			"time": str(timeAndDay["time"]) + ":00-" + str(timeAndDay["time"]) + ":59",
			"day": timeAndDay["day"]
		}
		return jsonify({"success": True, "data": responseData})
	except Exception as e:
		return jsonify({"success": False, "error": {"message": "Internal Server Error: " + str(e), "code": 101}})
