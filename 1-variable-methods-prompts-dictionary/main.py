def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors):")
    computer_choice = input("Enter a choice (Rock, Paper, Scissors):")

    choices = {
        'player': player_choice,
        'computer': computer_choice
    }

    return choices


def greeting():
    return "Hii!"


response = greeting()

print(response)

choices = get_choices()
print(choices)

my_object = {
    'name': 'beau',
    'color': choices
}

