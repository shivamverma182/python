# -*- coding: utf-8 -*-
# Craps.

import random


def rollDice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    workSum = die1 + die2
    print "Worksum of %d and %d is %d" % (die1, die2, workSum)
    return workSum


sum = rollDice()

if sum == 7 or sum == 11:
    gameStatus = "WON"
elif sum == 2 or sum == 3 or sum == 11:
    gameStatus = "LOST"
else:
    gameStatus = "CONTINUE"
    myPoint = sum
    print "Point is %d" % myPoint

while gameStatus == "CONTINUE":
    sum = rollDice()
    if sum == myPoint:
        gameStatus = "WON"
    elif sum == 7:
        gameStatus = "LOST"

if gameStatus == "WON":
    print "Player wins"
else:
    print "Player loses"
