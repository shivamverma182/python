# -*- coding: utf-8 -*-
# a program that reads in the radius of a circle and prints the circle’s
# diameter, circumference and area. Use the constant value 3.14159 for π.

# prompt user for radius and convert to integer
radius = raw_input("Enter the radius of circle: ")
radius = float(radius)

diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius * radius

print "diameter: %f" % diameter
print "circumference: %f" % circumference
print "area: %f" % area
