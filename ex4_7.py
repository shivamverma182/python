# -*- coding: utf-8 -*-
# program that plays the game of “guess the number”
import random

print "I have a number between 1 & 1000"
print "Can you guess the number"

wish = "yes"
correct = "yes"
while wish == "yes":
    a = random.randrange(1, 1001)
    while correct == "yes":
        guess = int(raw_input("Please enter your guess: "))
        if a == guess:
            print "Excellent! You guessed the number!"
            wish = raw_input("do you wish to continue? ")
            break
        elif guess > a:
            print "Too high. Try again"
            continue
        elif guess < a:
            print "Too low. Try again"
            continue
