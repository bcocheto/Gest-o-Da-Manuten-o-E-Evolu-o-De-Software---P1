from .Player import Player

ADVANTAGE = 3
WIN = 4
MINIMAL_POINTS_DIFFERENCE_SET = 2
SCORES = {
    0: 'Love',
    1: 'Fifteen',
    2: 'Thirty',
    3: 'Forty'
}


class Game:
    def __init__(self, playerOneName, playerTwoName):
        self.playerOne = Player(playerOneName)
        self.playerTwo = Player(playerTwoName)

    def wonPoint(self, playerName):
        if playerName == self.playerOne.getPlayerName():
            self.playerOneScore()
        else:
            self.playerTwoScore()

    def score(self):
        if self.isBreakEven():
            result = self.getBreakEvenScore(self.playerOne.getPlayerPoints())

        elif self.isPlayerOneAdvantage():
            result = "Advantage " + self.playerOne.getPlayerName()

        elif self.isPlayerTwoAdvantage():
            result = "Advantage " + self.playerTwo.getPlayerName()

        elif self.playerSetPoint(self.playerOne.getPlayerPoints()) and self.isGameWin(self.getPlayerOnePlayerTwoDifference()):
            result = "Win for " + self.playerOne.getPlayerName()

        elif self.playerSetPoint(self.playerTwo.getPlayerPoints()) and self.isGameWin(self.getPlayerTwoPlayerOneDifference()):
            result = "Win for " + self.playerTwo.getPlayerName()
        else:
            playerOneScore = self.getScore(self.playerOne.getPlayerPoints())
            playerTwoScore = self.getScore(self.playerTwo.getPlayerPoints())
            result = playerOneScore + "-" + playerTwoScore

        return result

    def isGameWin(self, difference):
        return difference >= MINIMAL_POINTS_DIFFERENCE_SET

    def getPlayerOnePlayerTwoDifference(self):
        return self.playerOne.getPlayerPoints() - self.playerTwo.getPlayerPoints()

    def getPlayerTwoPlayerOneDifference(self):
        return self.playerTwo.getPlayerPoints() - self.playerOne.getPlayerPoints()

    def playerSetPoint(self, points):
        return points >= WIN

    def isPlayerTwoAdvantage(self):
        return self.playerTwo.getPlayerPoints() > self.playerOne.getPlayerPoints() >= ADVANTAGE

    def isPlayerOneAdvantage(self):
        return self.playerOne.getPlayerPoints() > self.playerTwo.getPlayerPoints() >= ADVANTAGE

    def isBreakEven(self):
        return self.playerOne.getPlayerPoints() == self.playerTwo.getPlayerPoints() and self.playerOne.getPlayerPoints() < ADVANTAGE

    def getBreakEvenScore(self, points):
        if points >= ADVANTAGE:
            return "Deuce"
        result = self.getScore(points)
        result += "-All"

        return result

    def getScore(self, points):
        return SCORES[points]

    def setPlayerOneScore(self, number):
        for i in range(number):
            self.playerOnePoints()

    def playerTwoPoints(self):
        self.playerTwo.setPlayerPoints(self.playerTwo.getPlayerPoints() + 1)

    def setPlayerTwoScore(self, number):
        for i in range(number):
            self.playerTwoPoints()

    def playerOnePoints(self):
        self.playerOne.setPlayerPoints(self.playerOne.getPlayerPoints() + 1)
