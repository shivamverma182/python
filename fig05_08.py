# -*- coding: utf-8 -*-
# Slicing sequences

# Creating slices
sliceString = "abcdefghij"
sliceList = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
sliceTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Print sequences
print "sliceString: ", sliceString
print "sliceList: ", sliceList
print "sliceTuple: ", sliceTuple

# get slices
start = int(raw_input("Enter start: "))
end = int(raw_input("Enter end: "))

# print slices
print "\nSlicedString[", start, ":", end, "] = ", sliceString[start:end]
print "\nSlicedList[", start, ":", end, "] = ", sliceList[start:end]
print "\nSlicedTuple[", start, ":", end, "] = ", sliceTuple[start:end]
