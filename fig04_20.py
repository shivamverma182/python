# -*- coding: utf-8 -*-
# Using default argument


def boxValue(length=1, width=1, height=1):
    return length * width * height

print "The default box volume is: ", boxValue()
print "\nThe volume of a box with length 10,"
print "width 1 and height 1 is: ", boxValue(10)
print "\nThe volume of a box with length 10,"
print "width 5 and height 1 is: ", boxValue(10, 5)
print "\nThe volume of a box with length 10,"
print "width 5 and height 2 is: ", boxValue(10, 5, 2)
