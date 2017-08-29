#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

total = 0

for line in fh:
    if line.startswith("@"):
        continue
    else:
        for line in fh:
            fields = line.split("\t")
            if fields[2] == "2L" and int(fields[3]) <= 20000 and int(fields[3]) >= 10000:
                total = total +1
            else:
                continue
                
print "Reads in chromosome 2L starting between the 10000th and 20000th base:", total