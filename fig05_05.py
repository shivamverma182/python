# -*- coding: utf-8 -*-
# Creating a histogram from a list of values

values = []  # create an empty list

# input 10 values from user
print "Enter 10 integers"

for i in range(10):
    newValue = int(raw_input("Enter integer %d: " % (i + 1)))
    values += [newValue]

# Create histogram
print "\nCreating a histogram from values:"
print "%s %s %s" % ("Element", "Values", "Histogram")

for i in range(len(values)):
    print "%-7d %-6d %-9s" % (i, values[i], "*" * values[i])
