import random
from Card import Card
from Suit import Heart, Club, Diamond, Spade
from MakeCard import MakeCard
from GenDeckOfCards import GenDeckOfCards

class CardGame(object):
    def __init__(self, suits, deckGen, makeCard):
        self.suits = suits
        self.deckGenerator = deckGen
        self.makeCard = makeCard
        self.cards = []
        self.shuffleNum = 52
    
    def start(self):
        cardGen = self.deckGenerator(self.suits, self.makeCard)
        self.cards = cardGen.getDeck()
    
    def shuffle(self):
        for i in range(0, self.shuffleNum):
            card1 = random.randrange(0, 52)
            card2 = random.randrange(0, 52)

            self.cards[card1], self.cards[card2] = self.cards[card2], self.cards[card1]

    def dealOneCard(self):
        try:
            # Since cards are dealt from the top of the deck then use pop()
            return self.cards.pop()
        except IndexError as e:
            return None

# Test
if __name__ == "__main__":
    cardGame = CardGame([Heart, Club, Diamond, Spade], GenDeckOfCards, MakeCard)
    cardGame.start()
    cardGame.shuffle()
    for i in range(55):
        dealCard = cardGame.dealOneCard()
        if dealCard:
            print([dealCard.getVal(), dealCard.getSuitName()])
        else:
            print ("No more cards to deal.")
