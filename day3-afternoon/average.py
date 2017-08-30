#!/usr/bin/env python

import sys

fh = open( sys.argv[1] )

sum = 0
count = 0

for line in fh:
    line = line.rstrip()
    sum = int(line) + sum
    count = count + 1

average = sum / count
print "There are %s genes with an average gene length of %s" % (count, average)