# -*- coding: utf-8 -*-
# Check if a given number is perfect number


def perfect(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total

for i in range(1, 1001):
    if i == perfect(i):
        print "%d is perfect number" % i
    # else:
    #     print "%d is not perfect number" % i
