#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

total = 0

for line in fh:
    if line.startswith("@"):
        continue
    else: 
        total = total + 1

print total