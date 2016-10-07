import tweepy, operator
from datetime import datetime
from calendar import day_name
import config


def _getTwitterApi():
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True, compression=True)
	return api


def getBestTimeAndDay(userIdOrName):
	resultDict = {"time": -1, "day": ""}
	try:
		api = _getTwitterApi()
		timeMap = {}
		dayMap = {}
		followersCount = config.FOLLOWERS_COUNT
		try:
			for followerObj in tweepy.Cursor(api.followers, userIdOrName).items():
				if followersCount == 0:
					break
				follower = followerObj._json
				if "status" in follower:
					timeStampStr = follower["status"]["created_at"]
					d = datetime.strptime(timeStampStr, '%a %b %d %H:%M:%S +0000 %Y')
					dayNum = d.weekday()
					if d.hour not in timeMap:
						timeMap[d.hour] = 0
					timeMap[d.hour] = timeMap[d.hour] + 1
					if dayNum not in dayMap:
						dayMap[dayNum] = 0
					dayMap[dayNum] = dayMap[dayNum] + 1
					followersCount -= 1
		except tweepy.RateLimitError as e:
			print e
			pass
		if len(timeMap) == 0 or len(dayMap) == 0:
			return resultDict
		timeMax = max(timeMap.iteritems(), key=operator.itemgetter(1))
		dayMax = max(dayMap.iteritems(), key=operator.itemgetter(1))
		resultDict["time"] = timeMax[0]
		resultDict["day"] = day_name[dayMax[0]]
		return resultDict
	except Exception as e:
		print e
		return None


if __name__ == "__main__":
	print getBestTimeAndDay("hitesh28jan")
 	print getBestTimeAndDay(1586015334)
