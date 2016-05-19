# -*- coding: utf-8 -*-
# Roll a six-sided die 6000 times.

import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for i in range(1, 6001):  # roll dice 6 times
    face = random.randrange(1, 7)

    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1
    else:
        print "Should never get here"
print "Face %13s" % "Frequency"
print "   1 %13s" % frequency1
print "   2 %13s" % frequency2
print "   3 %13s" % frequency3
print "   4 %13s" % frequency4
print "   5 %13s" % frequency5
print "   6 %13s" % frequency6
