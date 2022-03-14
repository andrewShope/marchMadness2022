import math
from Team import Team

class Bracket:
	def __init__(self, teamList):
		# teamList should be a list of Team objects which will contain
		# the teams starting position in the bracket
		assert math.log(len(teamList), 2) % 1 == 0, "The number of teams \
													must be a power of 2"
		self.teamList = teamList
		self.teamSize = len(teamList)
		self.roundList = []
		self.currentRound = 0
		self.currentGame = 0
		self.totalRounds = int(math.log(self.teamSize))
		self.N = self.teamSize/2
		self.buildBracket()
		self.champion = None

	def buildBracket(self):
		# Build the round list. Each index in the round list is a game
		# to be played in that round. First round = len(32), second
		# round = len(16), etc
		for i in range(int(math.log(self.teamSize, 2))):
			matchList = []
			for j in range(int(self.teamSize/(2**(i+1)))):
				matchList.append(Match(i, j))
			self.roundList.append(matchList)

		# Enter the first round of teams
		for team in self.teamList:
			self.roundList[0][team.startingNode - 1].addTeam(team)

	def updateBracket(self, game, winner):
		if game.roundNumber >= 5:
			self.champion = winner
		else:
			if game.matchNumber % 2 == 0:
				nextGameIndex = game.matchNumber//2
			else:
				nextGameIndex = (game.matchNumber - 1)//2
			self.roundList[game.roundNumber + 1][nextGameIndex].addTeam(winner)

	def __iter__(self):
		return self

	def __next__(self):
		if self.currentRound > int(math.log(self.teamSize, 2) - 1):
			self.currentGame = 0
			self.currentRound = 0
			raise StopIteration()
		thisGame = self.roundList[self.currentRound][self.currentGame]

		#Update to next game
		self.currentGame += 1
		if self.currentGame >= len(self.roundList[self.currentRound]):
			self.currentGame = 0
			self.currentRound += 1

		return thisGame


class Match:
	def __init__(self, roundNumber, matchNumber):
		self.teamOne = None
		self.teamTwo = None
		self.roundNumber = roundNumber
		self.matchNumber = matchNumber

	def addTeam(self, teamObject):
		if self.teamOne == None:
			self.teamOne = teamObject
		else:
			self.teamTwo = teamObject



if __name__ == '__main__':
	teamList = []
	for i in range(32):
		teamList.append(Team("a name", i, 3))
		teamList.append(Team("a name", i, 3))
	x = Bracket(teamList)
	for i in range(len(x.roundList)):
		print(len(x.roundList[i]))
	
	for game in x:
		print(game.teamOne.teamName + " vs. " + game.teamTwo.teamName)
