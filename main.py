# GUESSING THE NUMBER GAME

import random

print("Welcome to the GUESSSING THE NUMBER GAME!")

number = random.randint(0,100)
Guesses = 5

win = False

while Guesses > 0:
    guess = int(input("Guess: "))

    Guesses -= 1

    if guess > number:
        print("Your guess was too high,you have", Guesses,"remaning")
    elif guess < number:
        print("Your guess was too low,you have", Guesses,"remaining")
    else:
        print("Congrats,you guessed the correct number and won the game")
        win = True
        guess = 0

if win == False:
    print("Sorry,you didn't guess the number, The number was",number)