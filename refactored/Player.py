class Player:

    def __init__(self, name, points, score):
        self._name = name
        self._points = points
        self._score = score

    def setPlayerName (self,name):
        self._name = name

    def setPlayerScore(self):
        self._score += 1

    def getPlayerScore(self):
        return self._score
    
    def setPlayerPoints (self,points):
        self._points = points
    
    def getPlayerName (self):
        return self._name

    def getPlayerPoints (self):
        return self._points

    def getPlayerSets(self):
        return round(self._points/15) if round(self._points/15)>0 else 0   

