from .Player import Player

class Game:

    def __init__(self, score, playerOne, playerTwo):
        self._playerOne = Player # input do usuário
        self._playerTwo = Player #input do usuário
        self._score = score

    def setGainPoints(self, points):
        self._player.setPlayerPoints(points)

    def score(self):

    def getPlayerWithTheMostPoints(self):
        return self._playerOne.getPlayerPoints() if self._playerOne.getPlayerPoints()>self._playerTwo.getPlayerPoints() else self._playerTwo.getPlayerPoints()
        