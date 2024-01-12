class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank["rank"]} of {str(self.suit)}"


card1 = Card("hearts", {"rank": "2", "value": 2})
print(card1)