# -*- coding: utf-8 -*-
# Calculation of mathematical constant e
from __future__ import division
a = 0
for i in range(1, 11):
    factorial = 1
    while i != 0:
        factorial *= i
        i -= 1
    a = 1 / factorial
e = 1 + a
print "%.10f" % e
