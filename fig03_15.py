# -*- coding: utf-8 -*-
# Analysis of examination results.

# Initialize variables
counter = 1
passes = 0
fails = 0

# Processing Phase
while counter <= 10:
    result = raw_input("Enter result (1=pass, 2=fail): ")
    if result == '1':
        passes = passes + 1
        counter = counter + 1
    elif result == '2':
        fails = fails + 1
        counter = counter + 1
    else:
        print "wrong input, please try again"

# Termination Phase
print "Number of 1's entered is %d" % passes
print "Number of 2's entered is %d" % fails

print "Number of pass students is %d" % passes
print "Number of fail students is %d" % fails

if passes > 8:
    print "Raise tuition."
