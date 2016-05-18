# -*- coding: utf-8 -*-
# check whether a number is prime or not using sqrt of numer
from math import sqrt


def prime(number):
    string = "Prime"
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:  # divided
            string = "Not Prime"
            break
    print string
n = int(raw_input("enter any number: "))
prime(n)
