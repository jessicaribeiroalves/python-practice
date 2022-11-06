import random
import copy

order = {
    "H": 0,
    "D": 1,
    "C": 2,
    "S": 3
}


class Deck:
    def __init__(self):
        self.cards = []
        self.values = ["2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["D", "H", "C", "S"]
        for value in self.values:
            for suit in self.suits:
                self.cards.append(value + suit)

    def shuffle(self):
        random.shuffle(self.cards)
        print('after shuffling', self.cards)

    def deal(self, n):
        slice = self.cards[len(self.cards) - n: len(self.cards)]
        del self.cards[len(self.cards) - n: len(self.cards)]
        return slice

    def sort_by_suit(self):
        self.cards.sort(key=lambda card: order[card[-1]])

    def contains(self, card):
        return card in self.cards

    def copy(self):
        return copy.deepcopy(self)

    def get_cards(self):
        return self.cards[:len(self.cards)]

    def __len__(self):
        return len(self.cards)


deck = Deck()
deck.shuffle()
deck.sort_by_suit()
