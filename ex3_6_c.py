# -*- coding: utf-8 -*-
# Calculation of mathematical constant e ** x
from __future__ import division
x = 4
a = 0
for i in range(1, 11):
    factorial = 1
    while i != 0:
        factorial *= i
        i -= 1
    a = (x ** i) / factorial
    print a
e = 1 + a
print "%.10f" % e
