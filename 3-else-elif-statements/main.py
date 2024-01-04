import random

def can_drink(age):
    if age >= 18:
        return 'Can Drink!'
    else:
        return 'Cannot Drink!'


def can_drink_complex(age):
    if 18 <= age < 20:
        return 'Can not drink more than 0.2'
    elif 20 <= age <= 25:
        return 'Can not drink more than 0.4'
    elif age > 25:
        return 'Can drink'


can_person_drink_17 = can_drink(17)
can_person_drink_21 = can_drink(21)

print(f'The person with age of 17 is {can_person_drink_17} where as the person with age of 21 is {can_person_drink_21}');

can_person_drink_complex_17 = can_drink_complex(17)
can_person_drink_complex_18 = can_drink_complex(18)
can_person_drink_complex_23 = can_drink_complex(23)
can_person_drink_complex_27 = can_drink_complex(27)

print(f'The person with age of 17 is {can_person_drink_complex_17}')
print(f'The person with age of 18 is {can_person_drink_complex_18}')
print(f'The person with age of 23 is {can_person_drink_complex_23}')
print(f'The person with age of 27 is {can_person_drink_complex_27}')


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
