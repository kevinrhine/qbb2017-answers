#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

sum = 0
total = 0

for line in fh:
    if line.startswith("@"):
        continue
    else:
        for line in fh:
            total = total + 1
            fields = line.split("\t")
            sum = sum + int(fields[4])

average = sum / total
print average