# -*- coding: utf-8 -*-
# Function implementation of Fahrenheit
from __future__ import division


def fahrenheit(celsius):
    return 9 / 5 * celsius + 32

print "Fehrenheit    Celsius"
for i in range(0, 101):
    abc = float(fahrenheit(i))
    print "%10.1f    %7d" % (abc, i)
