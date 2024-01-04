import random

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors):")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print('Player chose ' + player_choice)
    print('Computer chose ' + computer_choice)

    print(f'Player chose: {player_choice} AND Computer chose: {computer_choice}')

    choices = {
        'player': player_choice,
        'computer': computer_choice
    }

    winner = check_winner(choices['player'], choices['computer'])
    return winner


def check_winner(player, computer):
    if player == computer:
        return 'tie'

    if player == 'rock':
        if computer == 'scissors':
            return 'player'
        if computer == 'paper':
            return 'computer'

    if player == 'paper':
        if computer == 'rock':
            return 'player'
        if computer == 'scissors':
            return 'computer'

    if player == 'scissors':
        if computer == 'paper':
            return 'player'
        if computer == 'rock':
            return 'computer'

    return 'Both players must select an option'


winner = get_choices()
print(f'Winner is {winner}')
