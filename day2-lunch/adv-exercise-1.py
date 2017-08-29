#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

count_pos = 0
count_neg = 0

for line in fh:
    if line.startswith("@"):
        continue
    else:
        for line in fh:
            fields = line.split("\t")
            binary = int(fields[1])
            mask = 0b10000
            if mask & binary > 0:
                count_pos = count_pos + 1
            else:
                count_neg = count_neg + 1

print "Positive Strand Reads:", count_pos
print "Negative Strand Reads:", count_neg