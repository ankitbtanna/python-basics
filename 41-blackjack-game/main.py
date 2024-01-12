import random

# cards
cards: list[list] = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = [
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
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

print("Number of cards: ", len(cards))


def shuffle():
    random.shuffle(cards)


def deal(number_of_cards: int):
    cards_dealt:list = []

    for x in range(number_of_cards):
        card = cards.pop()
        cards_dealt.append(card)

    return cards_dealt


def cards_left():
    return len(cards)


# Shuffle the cards
shuffle()
print(cards)

card = deal(1)[0]

print(card[1]["value"])

# suit = suits[2]
# rank = "K"
# value = 10
#
# print(f"Your card is: {rank} of {suit}")
#
# suits.append("snakes")

############

# deal a card
# cards_dealt = deal(2)
# print(cards_dealt)
#
# first_card = cards_dealt[0]
# second_card = cards_dealt[1]
#
# first_card_rank = first_card[1]
# second_card_rank = second_card[1]
#
# if first_card_rank == "A":
#     value = 11
# elif first_card_rank == "J" or first_card_rank == "Q" or first_card_rank == "K":
#     value = 10
# else:
#     value = int(first_card_rank)
#
# rank_dict = {"rank": first_card_rank, "value": value}
#
# print(rank_dict["rank"], rank_dict["value"])
#
# print(first_card)
# print(second_card)
#
# print(cards_left())
