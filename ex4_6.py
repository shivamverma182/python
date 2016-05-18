# -*- coding: utf-8 -*-
"""
Computers are playing an increasing role in education. The use of computers in
education isreferred to as computer-assisted instruction (CAI). Write a program
that will help an elementary school student learn multiplication. Use the
random module to produce two positive one-digit integers. The program should
then display a question, such as How much is 6 times 7? The student then types
the answer. Next, the program checks the student’s answer. If it is correct,
print the string "Very good!" on the screen and ask another multiplication
question. If the answer is wrong, display "No. Please try again." and let the
student try the same question again repeatedly until the student finally gets
it right. A separate function should be used to generate each new question.
This method should be called once when the program begins execution and each
time the user answers the question correctly. (Hint: To convert the numbers for
the problem into strings for the question, use function str. For example,
str( 7 ) returns "7".)
"""
import random


def multiply():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    print "How much is %d time %d" % (a, b)
    return a * b

wish = "yes"
correct = "yes"
while wish == "yes":
    multi = str(multiply())
    while correct == "yes":
        ans = raw_input("")
        if multi == ans:
            print "Very Good"
            wish = raw_input("Do you wish to continue? ")
            break
        else:
            print "No. Please try again"
            correct == "no"
