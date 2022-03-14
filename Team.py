class Team:
	def __init__(self, teamName, startingNode, rank, elo):
		self.teamName = teamName
		self.startingNode = startingNode
		self.elo = round(elo)
		self.rank = rank
