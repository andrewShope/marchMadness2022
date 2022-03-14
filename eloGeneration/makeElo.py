import datetime
from Elo import makeNewRating
from sortedcontainers import SortedDict
import json

class Team:
	def __init__(self, name):
		self.name = name
		self.rating = None
		self.wins = 0
		self.losses = 0

def updateElo(team, newElo, teamsDict):
	teamsDict["Teams"][team]["elo"] = newElo

startingElo = 1600
iterationNumber = 200

startDate = datetime.date(2021, 11, 9)
endDate = datetime.date(2022, 3, 13)
oneDay = datetime.timedelta(days=1)


gameHistoryPath = "C:\\Users\\andre\\Documents\\marchMadness\\Scraper\\games.json"
with open(gameHistoryPath, 'r') as file:
	gameHistory = json.load(file)

teamsDict = {}
gameHistory = gameHistory['dates']

# Loop through all the games, assigning updated Elo for each sample
for i in range(iterationNumber):
	currentDate = startDate
	while currentDate < endDate:
		gameList = gameHistory[str(currentDate)]['games']
		for game in gameList:
			winner = game["winner"]
			loser = game["loser"]

			# Check to see if they've been initialized in my Elo list yet
			if winner not in teamsDict.keys():
				teamsDict[winner] = Team(winner)
				teamsDict[winner].rating = startingElo
			if loser not in teamsDict.keys():
				teamsDict[loser] = Team(loser)
				teamsDict[loser].rating = startingElo

			loserRating = teamsDict[loser].rating
			winnerRating = teamsDict[winner].rating

			newLoserElo, newWinnerElo = makeNewRating(loserRating, winnerRating)

			teamsDict[loser].rating = newLoserElo
			teamsDict[winner].rating = newWinnerElo
			teamsDict[loser].losses += 1
			teamsDict[winner].wins += 1
		currentDate += oneDay

newDict = {}
for team in teamsDict.keys():
	newDict[team] = teamsDict[team].rating
json_string = json.dumps(newDict)
with open('teamsAndElo.json', 'w') as file:
	file.write(json_string)
