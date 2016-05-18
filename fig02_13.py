#!/usr/bin/python
# Figure 02.13: fig02_13.py
# Displaying object's location, type and value.

# prompt the user for input
integer1 = raw_input("Enter integer1:\t")  # read a string
print "Integer1: ", id(integer1), type(integer1), integer1
integer1 = int(integer1)  # convert string into integer
print "Integer1: ", id(integer1), type(integer1), integer1

integer2 = raw_input("Enter integer2:\t") # read a string
print "Integer2: ", id(integer2), type(integer2), integer2
integer2 = int(integer2)  # convert string into integer
print "Integer2: ", id(integer2), type(integer2), integer2

sum = inetger1 + integer2  # assignment of sum
print "Sum is: ", id(sum), type(sum), id(sum)
