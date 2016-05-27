# -*- coding: utf-8 -*-
# Creating, accessing an modifying a dictionary

# Create and print empty dictionary
emptyDictionary = {}
print "The value of empty string is: ", emptyDictionary

# Create and print dictionary with initial value
grades = {"Shivam": 90, "Manoj": 89, "Gourav": 88}
print "\nAll grades", grades

# Accessing and modifying an existing dictionary
print "\nShivam's grade: ", grades["Shivam"]

grades["Manoj"] = 85
print "Manoj's new grade", grades["Manoj"]

# Add to an existing dictionary
grades["Ankit"] = 80
print "\nGrades after addition: ", grades

# Removing entry from grade
del grades["Gourav"]
print "\nGrades after removing: ", grades
