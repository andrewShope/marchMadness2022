from Bracket import Bracket
from Team import Team
import json
from eloGeneration.Elo import findWinProbability

def expectedValue(game):
	# Finds the EV of each team winning. Input is a Match object which
	# includes Team objects for each team in the game
	teamOne = game.teamOne
	teamTwo = game.teamTwo
	probOne, probTwo = findWinProbability(teamOne.elo, teamTwo.elo)
	roundPoints = 2**game.roundNumber
	pointsOne = roundPoints
	pointsTwo = roundPoints
	if teamOne.rank > teamTwo.rank:
		pointsOne += (teamOne.rank - teamTwo.rank)
	if teamTwo.rank > teamOne.rank:
		pointsTwo += (teamTwo.rank - teamOne.rank)

	ev1 = pointsOne*probOne
	ev2 = pointsTwo*probTwo
	return (ev1, ev2)

def simulate(game):
	print("Round {0} Game {1}".format(game.roundNumber + 1, game.matchNumber + 1))
	print("{0.teamName} ({0.elo}) vs. {1.teamName} ({1.elo})".format(game.teamOne, game.teamTwo))
	winProbOne, winProbTwo = findWinProbability(game.teamOne.elo, game.teamTwo.elo)
	print("{0}% vs. {1}%".format(round(100*winProbOne), round(100*winProbTwo)))

	ev1, ev2 = expectedValue(game)
	print("{0:.2f}pts vs. {1:.2f}pts".format(ev1, ev2))

	if ev1 > ev2:
		winner = game.teamOne
	else:
		winner = game.teamTwo

	print("Best choice: {0}".format(winner.teamName))
	return winner

# Open my JSON file which has the list of teams in the tournament and
# their rank and position in the bracket
with open('teams.json') as file:
	teamDict = json.load(file)
teamDict = teamDict["Teams"]

with open('teamsAndElo.json') as file:
	eloDict = json.load(file)

# Create a Team object for each team in my dictionary and append it
# to my list containing all teams
teamList = []
for team in teamDict.keys():
	teamList.append(Team(team, teamDict[team]["node"], 
					teamDict[team]["rank"], eloDict[team]))

# Create the bracket
tournament = Bracket(teamList)

for game in tournament:
	winner = simulate(game)
	tournament.updateBracket(game, winner)
	input("")

# This code can be ran after the tournament has been simulated to 
# view it again
# for count, game in enumerate(tournament):
# 	print("#" + str(count + 1) + ": " + game.teamOne.teamName + " vs. " + game.teamTwo.teamName)
# print("Champion: " + tournament.champion.teamName)