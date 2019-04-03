from MakeCard import MakeCard

class GenDeckOfCards(object):
    options = ['Ace']
    options += map(lambda c: str(c), range(2, 11))
    options += ['Jack', 'Queen', 'King']

    def __init__(self, suits, makeCard):
        self.suits = suits
        self.makeCard = makeCard
        self.cards = []
    
    def genDeck(self, numDecks=1):
        for i in range(0, numDecks):
            for option in GenDeckOfCards.options:
                for suit in self.suits:
                    self.cards.append(self.makeCard.newCard(option, suit))

    def getDeck(self):
        self.genDeck()
        return self.cards
