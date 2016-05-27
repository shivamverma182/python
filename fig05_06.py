# -*- coding: utf-8 -*-
# Creating and accessing tuples

# get hours, minutes, seconds from user
hours = int(raw_input("Enter hours: "))
minutes = int(raw_input("Enter minutes: "))
seconds = int(raw_input("Enter seconds: "))

currentTime = hours, minutes, seconds  # create tupple

print "The value of currentTime is:", currentTime

# access tuples
print "The number of seconds from midnight is", \
 (currentTime[0] * 3600 + currentTime[1] * 60 + currentTime[2])
