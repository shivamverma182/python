# -*- coding: utf-8 -*-
# a program that reads in two integers and determines and prints whether the
# first is a multiple of the second

# promt user for input and convert string into integer
number1 = raw_input("Enter first number: ")
number1 = int(number1)

# promt user for input and convert string into integer
number2 = raw_input("Enter second number: ")
number2 = int(number2)

mod = number2 % number1

if mod == 0:
    print "%d is a multiple of %d" % (number1, number2)

if mod != 0:
    print "%d is not a multiple of %d" % (number1, number2)
