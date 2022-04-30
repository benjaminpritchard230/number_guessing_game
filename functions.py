def get_winning_number():
    """Chooses a winning number for the player to guess."""
    import random
    winning_number = random.randint(0, 10)
    return winning_number

def get_player_guess():
    """Gets the player's guess and makes sure that it is within range 1-10."""
    while True:
        while True:
            try:
                player_guess = int(input('Please guess a number between 1 and 10.\n'))
            except ValueError:
                print('Please enter a valid guess.')
                continue
            break
        if (player_guess > 10) or (player_guess < 1):
            print('Please select a number between 1 and 10.')
            continue
        else:
            break
    return player_guess

def check_guess(player_guess, winning_number):
    """Checks if the player has guessed the winning number."""
    if player_guess == winning_number:
        return True
    else:
        return False

def gameplay(winning_number):
    """Plays the number guessing game."""
    while True:
        player_guess = get_player_guess()
        if check_guess(player_guess, winning_number) is True:
            print('You guessed correctly!')
            break
        if player_guess < winning_number:
            print('You guessed too low!')
            continue
        else:
            print('You guessed too high!')
            continue
