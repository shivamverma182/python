# -*- coding: utf-8 -*-
# Using the break statement to avoid repeating code in the class-average
# program.

from __future__ import  division
# Initialization Phase
total = 0  # number of grade entered
counter = 0  # number of grade entered

# Processing Phase
while 1:
    grade = raw_input("Enter grade, -1 to end: ")
    grade = int(grade)
    # exit if user inputs -1
    if grade == -1:
        break
    total += grade
    counter += 1

# Terminate Phase
if counter != 0:
    avg = total / counter
    print "Class average is %.3f" % avg
else:
    print "No grades were entered"
