# -*- coding: utf-8 -*-
# Calculate factorial of a given number

n = raw_input("Enter any number: ")
n = int(n)
orignal = n
factorial = 1

if n == 0:
    factorial = 1
else:
    while n != 0:
        factorial *= n
        n -= 1
print "Factorial of %d is %d" % (orignal, factorial)
