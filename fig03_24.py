# -*- coding: utf-8 -*-
# Using the break statement in a for structure.
for x in range(1, 11):
    if x == 5:
        break
    print x,
print "\nBroke out loop at x = %d" % x
