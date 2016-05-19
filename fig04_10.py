# -*- coding: utf-8 -*-
# Scoping Example

x = 1  # global variable


# Alters the local variable x and shadows the global variable
def a():
    x = 25
    print "\nlocal x in a is", x, "After entering a"
    x += 1
    print "local x in a is", x, "After exiting a"


def b():
    global x
    print "\nglobal x in b is", x, "After entering b"
    x *= 10
    print "global x is", x, "on exiting b"

x = 7
print "global x is", x
a()
b()
a()
b()
