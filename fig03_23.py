# -*- coding: utf-8 -*-
# Calculating compound interest.

# Initialization Phase
principal = 1000.0  # Starting Principal
rate = 0.05  # Interest Rate
constant = 1.00 + rate
print "%s%21s" % ("Year", "Amount on deposite")

# Processing Phase
for year in range(1, 11):
    amount = principal * (constant) ** year
    print ("%4d%21.2f") % (year, amount)
