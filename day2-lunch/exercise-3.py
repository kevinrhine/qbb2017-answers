#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

total = 0
one_location = "NH:i:1"

for line in fh:
    if one_location in line:
        total = total + 1
    else: 
        continue

print total

