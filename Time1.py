# -*- coding: utf-8 -*-
# Simple definition of class Time.

class Time:
    """Time abstract data type (ADT) defination"""

    def __init__(self):
        """Initialize hours,minutes and seconds to zero"""

        self.hour = 11     # 0-23
        self.minute = 30  # 0-59
        self.second = 0   # 0-59

    def printMilitary(self):
        """Prints object of class Time in military format"""

        print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second),


    def printstandard(self):
        """Prints object of class Time in standard format"""

        standardTime = ""

        if self.hour == 0 or self.hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self.hour % 12)

        standardTime += "%.2d:%.2d" % (self.minute, self.second)

        if self.hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"

        print standardTime,

