from Card import Card

class MakeCard(object):

    @staticmethod
    def newCard(val, suit):
        return Card(val, suit)