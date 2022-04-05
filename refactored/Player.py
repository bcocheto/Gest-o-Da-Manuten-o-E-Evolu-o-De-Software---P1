class Game:

    def __init__(self, player1Name, player2Name):
        self.playerOneName = playerOneName
        self.playerTwoName = playerTwoName
        self.playerOnePoints = 0
        self.playerTwoPoints = 0

    def setPlayerOneName (self,name):
        self.playerOneName = name
    
    def setPlayerTwoName (self,name):
        self.playerTwoName = name

    def setPlayerOnePoints(self,points):
        self.playerOnePoints += points

    def setPlayerTwoPoints(self,points):
        self.playerTwoPoints += points

    def getPlayerOneName (self):
        return self.playerOneName
    
    def getPlayerTwoName (self):
        return self.playerTwoName

    def getPlayerOnePoints(self):
        return self.playerOnePoints

    def getPlayerTwoPoints(self):
        return self.playerTwoPoints

    
    