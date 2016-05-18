# -*- coding: utf-8 -*-
# Check if a number is prime number


def prime(number):
    string = "Prime"
    for i in range(2, (number / 2) + 1):
        if number % i == 0:  # divided
            string = "Not Prime"
            break
    print string
n = int(raw_input("enter any number: "))
prime(n)
