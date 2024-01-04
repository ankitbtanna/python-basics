import random

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors):")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    choices = {
        'player': player_choice,
        'computer': computer_choice
    }

    return choices


choices = get_choices()
print(choices)

food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)
print(dinner)

