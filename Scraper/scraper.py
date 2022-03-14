import datetime
import urllib.request
from bs4 import BeautifulSoup
import json


def buildURL(dateObject):
	# https://www.sports-reference.com/cbb/boxscores/index.cgi?month=03&day=11&year=2022
	baseURL = "http://www.sports-reference.com/cbb/boxscores/index.cgi?"
	monthString = str(dateObject.month)
	if len(monthString) < 2:
		monthString = "0" + monthString
	dayString = str(dateObject.day)
	if len(dayString) < 2:
		dayString = "0" + dayString
	yearString = str(dateObject.year)

	suffix = "month=" + monthString + "&day=" + dayString + "&year=" + \
			 yearString
	return baseURL + suffix

with open("games.json") as file:
	gameHistory = json.load(file)

startMonth = 11 
startDay = 9
startYear = 2021
endDate = datetime.date(2022, 3, 13)
currentDate = datetime.date(startYear, startMonth, startDay)
oneDay = datetime.timedelta(days=1)

while currentDate <= endDate:
	try:
		dataExists = gameHistory['dates'][str(currentDate)]['finished']
	except KeyError:
		dataExists = False

	if  dataExists:
		print("{0:%B} {0:%d}, {0:%Y}: Previously completed.".format(currentDate))
		currentDate += oneDay
	else:
		print("{0:%B} {0:%d}, {0:%Y}: Fetching games.".format(currentDate))
		url = buildURL(currentDate)
		# Requesting HTML form from site
		with urllib.request.urlopen(url) as response:
			html = response.read()

		# Creating the BeautifulSoup object and then parsing it to isolate
		# the game summaries
		soup = BeautifulSoup(html, 'html5lib')
		games = soup.find_all("div", "game_summary")

		# Within each game summary I'm finding the winning team and
		# losing team
		gameObjectList = []
		for game in games:
			if len(game.find_all("tr", "winner")) > 0:
				losingTeam = game.find_all("tr", "loser")[0].a.contents[0]
				winningTeam = game.find_all("tr", "winner")[0].a.contents[0]
				gameDict = {"loser": losingTeam, "winner": winningTeam}
				gameObjectList.append(gameDict)

		# Adding the games to my gameHistory object and then writing
		# that to a file
		gameHistory["dates"][str(currentDate)] =  {"games": gameObjectList, "finished": True}
		json_string = json.dumps(gameHistory)
		with open('games.json', 'w') as file:
			file.write(json_string)

		currentDate += oneDay