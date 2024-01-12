from deck import Deck
from hand import Hand


class Game:
    def play(self):
        self.game_number = 0
        self.games_to_play = 0

        while self.games_to_play <= 0:
            try:
                self.games_to_play = int(input("How many games would you like to play?"))
            except:
                print("You must enter an number")



        print(f"You will play {self.games_to_play} games");

        while self.game_number < self.games_to_play:
            self.game_number += 1

            print("Creating deck...")
            deck = Deck()
            print("Shuffling deck...")
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print("*" * 30)
            print(f"Game {self.game_number} of {self.games_to_play}...")
            print("*" * 30)

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()

                while choice not in ["h", "hit", "s", "stand"]:
                    choice = input("Please choose 'Hit' or 'Stand': ").lower()
                    print()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Player Hand Value:", player_hand_value)
            print("Dealer Hand Value:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over: bool = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You're busted, Dealer wins!!! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted, You wins! 😃")
                return True
            elif player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
                print("Both players have a Blackjack! Tie")
                return True
            elif player_hand.get_value() == 21:
                print("You have a blackjack. You win!")
                return True
            elif dealer_hand.get_value() == 21:
                print("Dealer has a blackjack. Dealer wins!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif dealer_hand.get_value() == player_hand.get_value():
                print("Tie")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Dealer wins!")
            return True

        return False


g = Game()
g.play()
