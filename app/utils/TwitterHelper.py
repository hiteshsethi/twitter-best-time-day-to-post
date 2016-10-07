import tweepy, operator
from datetime import datetime
from calendar import day_name
import config

#This function is a helper func which will return api obj of tweepy
def _getTwitterApi():
	auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
	auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True, compression=True)
	return api

#this is our main function, takes one arg(can be userId, userName) and return dict(day,time) or None in case of overall error
def getBestTimeAndDay(userIdOrName):
	resultDict = {"time": -1, "day": ""}
	try:
		api = _getTwitterApi()
		timeMap = {} #declaring timeMap, key will be timeHour, value will be count of tweets in that hour
		dayMap = {} #declaring dayMap, key will be weekDayNum, value will be count of tweets on that day
		followersCount = config.FOLLOWERS_COUNT #picking up default followers count from config
		try:
			#api.followers of api https://dev.twitter.com/rest/reference/get/followers/list and contains last tweet made by followers, and that's what we need!!
			for followerObj in tweepy.Cursor(api.followers, userIdOrName).items():
				if followersCount == 0:
					break

				follower = followerObj._json #getting dict from that obj

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
			print e #can't do anything(one option is to wait but who waits!), just log it
		if len(timeMap) == 0 or len(dayMap) == 0:
			return resultDict
		timeMax = max(timeMap.iteritems(), key=operator.itemgetter(1))
		dayMax = max(dayMap.iteritems(), key=operator.itemgetter(1))
		resultDict["time"] = timeMax[0]
		resultDict["day"] = day_name[dayMax[0]]
		return resultDict
	except Exception as e:
		print e # can't do anything, just log it
		return None


if __name__ == "__main__":
	print getBestTimeAndDay("hitesh28jan")
 	print getBestTimeAndDay(1586015334)
