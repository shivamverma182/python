# -*- coding: utf-8 -*-
# re compile code performance test
import re


def run_re():
    pattern = 'kernel'
    re_obj = re.compile(pattern)

    infile = open("test.txt", "r")
    match_count = 0
    lines = 0
    for line in infile:
        match = re_obj.search(line)
        if match:
            match_count += 1
        lines += 1
    return (lines, match_count)

if __name__ == "__main__":
    lines, match_count = run_re()
    print "LINES::", lines
    print "MATCH::", match_count
