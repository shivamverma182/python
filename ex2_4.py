# -*- coding: utf-8 -*-
from __future__ import division
# This program requests the user to enter two numbers and prints the sum,
# product, difference and quotient of the two numbers

# Prompt user for first string and convert string to integer
number1 = raw_input("Enter first number: ")
number1 = int(number1)

# Prompt user for second string and convert string to integer
number2 = raw_input("Enter second number: ")
number2 = int(number2)

add = number1 + number2
sub = number1 - number2
multipy = number1 + number2
quotient = number1 // number2

print "Sum is %d" % add
print "sub is %d" % sub
print "multiply is %d" % multipy
print "quotient is %d" % quotient