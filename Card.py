
class Card(object):

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
    
    def getVal(self):
        return self.val
    
    def getSuit(self):
        return self.suit
    
    def getSuitName(self):
        return self.suit.getName()