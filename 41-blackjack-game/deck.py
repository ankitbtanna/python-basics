import random
from card import Card


class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        self.suits = ["spades", "clubs", "hearts", "diamonds"]
        self.ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]

        # prepare the cards
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

        print("Number of cards: ", len(self.cards))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number_of_cards: int):
        cards_dealt: list = []

        if len(self.cards) > 0:
            for x in range(number_of_cards):
                card = self.cards.pop()
                cards_dealt.append(card)
            return cards_dealt
        else:
            return []

    def cards_left(self):
        return len(self.cards)


deck1 = Deck()
deck1.shuffle()
print(deck1.cards)
cards = deck1.deal(2)
print(cards)
