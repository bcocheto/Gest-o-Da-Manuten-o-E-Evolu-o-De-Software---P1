from .Player import Player

class Game:

    def __init__(self, score, playerOne, playerTwo):
        self._player = Player # exemplo
        self._playerOne = Player # input do usuário
        self._playerTwo = Player # input do usuário
        self._score = score

    def score(self):
        self.getAdvantageWinner()
        self.getPlayerWithTheMostPoints()
        self.getPlayerWithTheMostSets()
        

    def getScoreName(self):
    
        switch(self._player.getPlayerSets()){
            case 2:
                return "Fifteen"
            case 3:
                return "Thirthy"
            case 4:
                return "All"
            default:
                return "Love"
        }

    def getPlayerWithTheMostPoints(self):
        return self._playerOne if self._playerOne.getPlayerPoints()>self._playerTwo.getPlayerPoints() else self._playerTwo

    def getPlayerWithTheMostSets(self):
        return self._playerOne if self._playerOne.getPlayerSets()>self._playerTwo.getPlayerSets() else self._playerTwo

    def getAdvantageWinner(self):
        return "Advantage" + self.getPlayerWithTheMostSets if self._player.getPlayerSets()>=4 else "Not a winner"

    def getWinner(self):
        return "Win for " + self.getPlayerWithTheMostSets()