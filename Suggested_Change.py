# Number Guessing Game
# Date created: 2-09-2023
# Author: Miriam Asare-Baiden

import random

# List to store the number of attempts for each game
attempts_list = []


# Function to display the current high score
def show_score():
    if not attempts_list:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print(f'The current high score is {min(attempts_list)} attempts')


# Function to start the game
def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print("That's cool, Thanks!")
        exit()
    else:
        show_score()

    # Main game loop
    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError('Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input('Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print("That's cool, have a good one!")
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print("It's lower")
                elif guess < rand_num:
                    print("It's higher")

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()
#CODE REVIEW COMMENTS
'''
STRUCTURE, DESIGN AND COMMENTING

1. Overall this code is neat, well structured and easy to follow. 

2. The README.md file and LICENSING information is present which gives clarity to usability and 

3. I believe the function comments can be a but more descriptive. For example, this function does xyz. 
This could also be achieved by leaving in-line comments thorughout the code about import lines or blocks

4. It may also be beneficial to leave a comment on your exception handeler

5. Code is clean and not text heavy

FUNCTIONALITY

1. Code runs without error and executes smoothly

2. Formatting the output may be a bit helpful for readability purposes. For example, you may consider
adding a new line between the prompt and the user work
'''
