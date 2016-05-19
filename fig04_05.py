# -*- coding: utf-8 -*-
# Finding the maximum of three integers.


def maximumValue(a, b, c):
    maximum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c
    return maximum

n1 = int(raw_input("Enter fisrt integer: "))
n2 = int(raw_input("Enter second integer: "))
n3 = int(raw_input("Enter third integer: "))
print "maximum value is %d" % maximumValue(n1, n2, n3)
print

f1 = float(raw_input("Enter first float: "))
f2 = float(raw_input("Enter second float: "))
f3 = float(raw_input("Enter third float: "))
print "Maximum value is %f" % maximumValue(f1, f2, f3)
print

s1 = raw_input("Enter firsr string: ")
s2 = raw_input("Enter second string: ")
s3 = raw_input("Enter third string: ")
print "Maximum value is %s" % maximumValue(s1, s2, s3)
print
