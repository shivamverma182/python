# -*- coding: utf-8 -*-
# Class average program with sentinel-controlled repetition.

from __future__ import division

# Initialization Phase
total = 0
counter = 0

# Processing Phase
grade = raw_input("Enter grade, -1 to end: ")
grade = int(grade)

while grade != -1:
    total = total + grade
    counter = counter + 1
    grade = raw_input("Enter grade, -1 to end: ")
    grade = int(grade)

# Terminating Phase
if counter != 0:
    avg = total / counter
    print "Average is %5.3f" % avg
else:
    print "No input was entered"
