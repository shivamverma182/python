# -*- coding: utf-8 -*-
# Creating and manipulating objects of class Time.

from Time1 import Time  # import class defination from file

time1 = Time()  # create object of class time

# Access object's attribute
print "The attribute of time1 are: "
print "time1.hour: ", time1.hour
print "time1.minute: ", time1.minute
print "time1.second: ", time1.second

# access object's method
print "\nCalling method printMilitary: ", time1.printMilitary()


print "\nCalling method prinStandard: ", time1.printstandard()

# change value of object's attributes
print "\n\nChanging time1's hour attribute..."
time1.hour = 25
print "Calling method printMilitary after alteration: ", time1.printMilitary()
