def makeNewRating(loserRating, winnerRating, K=32):
	expectedLoser = 1/(1 + 10**((winnerRating - loserRating)/400))
	expectedWinner = 1/(1 + 10**((loserRating - winnerRating)/400))

	newRatingLoser = loserRating + K*(0-expectedLoser)
	newRatingWinner = winnerRating + K*(1-expectedWinner)

	return (newRatingLoser, newRatingWinner)

def findWinProbability(ratingOne, ratingTwo, K=32):
	expectedOne = 1/(1 + 10**((ratingTwo - ratingOne)/400))
	expectedTwo = 1/(1 + 10**((ratingOne - ratingTwo)/400))

	return (expectedOne, expectedTwo)