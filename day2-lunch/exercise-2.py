#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

total = 0
perfect_match = "MD:Z:40"

for line in fh:
    if perfect_match in line:
        total = total + 1
    else: 
        continue

print total

