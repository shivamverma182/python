# -*- coding: utf-8 -*-
# conversion of binary to decimal

counter = 0  # number of digits in binary number
decimal = 0  # store decimal conversion
binary = raw_input("Enter any binary number: ")
binary = int(binary)
orignal = binary

# Count number of bits in binary number
while binary != 0:
    binary = binary / 10
    counter += 1

# Calculate decimal number
for i in range(1, counter + 1):
    abc = orignal % 10
    orignal = orignal / 10
    decimal = decimal + abc * (2 ** (i - 1))
print decimal
