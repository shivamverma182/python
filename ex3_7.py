# -*- coding: utf-8 -*-
# print various pattern
for i in range(1, 11):
    print "*" * i

print "\n"

for j in range(10, 0, -1):
    print "*" * j

print "\n"

for a in range(0, 10):
    print " " * a,
    for b in range(10 - a, 0, -1):
        print "*" * b
        break

print "\n"

for c in range(10, 0, -1):
    print " " * c,
    for d in range(11 - c, 11):
        print "*" * d
        break

raw_input("")
