# -*- coding: utf-8 -*-
# Creating, accessing and changing a list

aList = []  # creating an empty list

# Adding elements to list
for number in range(1, 11):
    aList += [number]

print "The vale of aList is: ",  aList


# Acessing list values by iteration
print "\nAccessing values by iteration"

for item in aList:
    print item,

print


# Accessing list by index
print "\nAccessing values by index:"
print "Subscript\tvalue"

for i in range(len(aList)):
    print "%-9d\t%-5d" % (i, aList[i])


# Modifying list
print "\nModifying the values of list"
print "\nValues befor modification", aList
aList[0] = 100
aList[-1] = 200
print "\n Values after modification", aList
