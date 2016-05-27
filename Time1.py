# -*- coding: utf-8 -*-
# Simple definition of class Time.

class Time:
    """Time abstract data type (ADT) defination"""

    def __init__(self):
        """Initialize hours,minutes and seconds to zero"""

        self.hour = 0  # 0-23
        self.minute = 0  # 0-59
        self.second = 0  # 0-59

    def printMilitary(self):
        """Prints object of class Time in military format"""

        print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)


    def printstandard(self):
        """Prints object of class Time in standard format"""

        standardTime = ""

        if standardTime == 0 or standardTime == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self.hour % 12)

        standardTime += "%.2d:%.2d" % (self.minute, self.hour)

        if self.hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"

        print standardTime,

