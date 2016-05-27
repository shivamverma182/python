# -*- coding: utf-8 -*-
# unpacking a sequence

# Creating sequences
aString = "abc"
aList = [1, 2, 3]
aTuple = "a", "A", 1

# unpacking sequences to variable
print "Unpacking string"
first, second, third = aString
print "String values are: ", first, second, third

# unpacking list to variables
print "Unpacking List"
first, second, third = aList
print "List values are: ", first, second, third

# unpackinf tuple to variables
print "Unoacking variables"

first, second, third = aTuple
print "Tuple values are: ", first, second, third
