import random

# config
low = 1
high = 100

import math
limit = math.ceil(math.log(high - low + 1, 2))



# helper functions
def show_start_screen():
    print(" _____                               _   _                 _               ")
    print("|  __ \                             | \ | |               | |              ")
    print("| |  \/_   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ ")
    print("| | __| | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
    print("| |_\ \ |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   ")
    print(" \____/\__,_|\___||___/___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|  ")

print()

def show_credits():
    print("This awesome game was created by Coop Dogg, but was made better by Kenneth Alexander.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print()
    print()
    print("Think carefully because you only get " + str(limit) + " chances to guess the correct the right number. ")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You must have paid attention in school, YOU WIN!")
    else:
        print("You are such a loser, you must be a Carolina fan! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()
print() 
playing = True

while playing:
    play()
    playing = play_again()

show_credits()



