# Figure 2.22: fig02_22.py
# Compare integers using if structures, relational operators, and equality
# operators

print "Enter two integers and i will tell you the relationship they satisfy."

# read the first string and convert to integer
integer1 = raw_input("Please enter first integer number:\t")
integer1 = int(integer1)

# read the second string and convert to interger
integer2 = raw_input("Please enter second integer number:\t")
integer2 = int(integer2)

# check if the numbers are equal
if integer1 == integer2:
    print "%d is equal to %d" % (integer1, integer2)

# check if numbers are not equal
if integer1 != integer2:
    print "%d is not equal to %d" % (integer1, integer2)

# check if first number is less than second number
if integer1 < integer2:
    print "%d is less than %d" % (integer1, integer2)

# check if first number is grater than second number
if integer1 > integer2:
    print "%d is greater than %d" % (integer1, integer2)

# check if first number is greater than or equal to second number
if integer1 >= integer2:
    print "%d is greater than or equal to %d." % (integer1, integer2)

# check if first number is less than or equal to second number
if integer1 <= integer2:
    print "%d is less than or equal to %d." % (integer1, integer2)