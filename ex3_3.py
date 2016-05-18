# -*- coding: utf-8 -*-
# Calculation of mileage obtained by their automobiles

from __future__ import division
# Initialization Phase
totalGallons = 0  # Total Gallons of fuel used
totalMiles = 0  # Total Miles of distance covered
counter = 0  # Number of gallons entered

gallons = raw_input("Enter the gallons used (-1 to end): ")
gallons = float(gallons)

# Processing Phase
while gallons != -1:
    miles = raw_input("Enter the miles driven: ")
    miles = float(miles)
    avg = miles / gallons
    print "The miles / gallon for this tank was %.4f" % avg
    totalGallons += gallons
    totalMiles += miles
    counter += 1
    gallons = raw_input("Enter the gallons used (-1 to end): ")
    gallons = float(gallons)

# Termination Phase
mileage = float(totalMiles) / float(totalGallons)
print "The overall average miles/gallon was %.4f" % mileage
