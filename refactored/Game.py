from .Player import Player

class Game:

    def __init__(self):
        self._player = Player

    def setGainPoints(self, points):
        self._player.setPlayerPoints(points)
        