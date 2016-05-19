# -*- coding: utf-8 -*-
# determines and prints all the prime numbers between 2 and 1,000


def primeNumber(number):
    prime = "Yes"
    for i in range(2, (number / 2) + 1):
        if number % i == 0:
            prime = "No"
            break
    return prime

for i in range(2, 1001):
    abc = primeNumber(i)
    if abc == "Yes":
        print "%d is prime number" % i
