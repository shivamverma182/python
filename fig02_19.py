# Figure 2.19: fig02_19.py
# Formatting string

integerValue = 4237
print "Integer:\t", integerValue
print "Decimal Integer:\t%d" % integerValue
print "Hexadecimal integer:\t%X" % integerValue

floatValue = 123456.789
print "Float:\t", floatValue
print "Default float:\t%f" % floatValue
print "Default exponential:\t%E" % floatValue

print "Right justify integer (%8d)" % integerValue
print "left justify integer (%-8d)" % integerValue

stringValue = "String formatting"
print "force eight digits in integer %.8d" % integerValue
print "five digits in after decimal in float %.5f" % floatValue
print "Fifteen and five characters allowed in string:"
print "(%.15s) (%.5s)" % (stringValue, stringValue)