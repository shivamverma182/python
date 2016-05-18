# -*- coding: utf-8 -*-
# Class average program with counter-controlled repetition.

# Initialization Phase
from __future__ import division
total = 0
counter = 1

# Processing Phase
while counter <= 10:  # loop 10 times
    grade = raw_input("Enter grade: ")  # get one grade
    grade = int(grade)  # convert string to integer
    total = total + grade
    counter = counter + 1

# Terminating Phase
avg = total / 10
print "Class average is %f" % avg
raw_input("Press enter to terminate")
