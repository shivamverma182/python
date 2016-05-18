# -*- coding: utf-8 -*-
# Check whether a five-digit number is palindrome or not

orignalNumber = raw_input("Enter any five-digit number: ")
number = int(orignalNumber)  # convert string to integer

a = number % 10
a = str(a)
number = number / 10  # left 4 digits


b = number % 10
b = str(b)
number = number / 10  # left 3 digits

c = number % 10
c = str(c)
number = number / 10  # left 2 digits

d = number % 10
d = str(d)
number = number / 10  # left only one digit

e = number % 10
e = str(e)
number = number / 10  # no digit left

inverted = a + b + c + d + e

if inverted == orignalNumber:
    print "%s is a palindrome" % orignalNumber
else:
    print "%s is not a palindrome" % orignalNumber

raw_input("\nPress any key to continue")
