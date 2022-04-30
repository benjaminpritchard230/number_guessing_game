from functions import *


winning_number = get_winning_number()


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

     