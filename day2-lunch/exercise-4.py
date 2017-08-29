#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

count = 1

for line in fh:
    if line.startswith("@"):
        continue
    else:
        for line in fh:
            if count > 10:
                break
            elif line:
                fields = line.split("\t")
                if fields[2] == str("*"):
                    continue
                else:
                    print str(fields[2])
                    count = count + 1