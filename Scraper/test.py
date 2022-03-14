import datetime
import urllib.request
from bs4 import BeautifulSoup

class Game:
	def __init__(self, losingTeam, winningTeam):
		self.losingTeam = losingTeam
		self.winningTeam = winningTeam

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


startMonth = 11 
startDay = 9
startYear = 2021
endDate = datetime.date(2022, 3, 13)

currentDate = datetime.date(startYear, startMonth, startDay)
url = buildURL(datetime.date(2022, 3, 11))
with urllib.request.urlopen(url) as response:
	html = response.read()
soup = BeautifulSoup(html, 'html5lib')
games = soup.find_all("div", "game_summary")
gameObjectList = []
for game in games:
	losingTeam = game.find_all("td")[0].a.contents[0]
	winningTeam = game.find_all("td")[3].a.contents[0]
	gameObjectList.append(Game(losingTeam, winningTeam))