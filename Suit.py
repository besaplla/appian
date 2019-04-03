from abc import ABCMeta, abstractmethod

class Suit(ABCMeta):
    @abstractmethod
    def getName():
        raise NotImplementedError('Needs to be defined in the child class')

class Heart(Suit):
    name = "Hearts"

    @staticmethod
    def getName():
        return Heart.name

class Spade(Suit):
    name = "Spades"

    @staticmethod
    def getName():
        return Spade.name

class Club(Suit):
    name = "Clubs"

    @staticmethod
    def getName():
        return Club.name

class Diamond(Suit):
    name = "Diamonds"

    @staticmethod
    def getName():
        return Diamond.name
