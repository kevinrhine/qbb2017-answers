#!/usr/bin/env python

import sys

f = open(sys.argv[1])

for line in f:
    fields = line.rstrip("\r\n").split("\t")
    fields[1].replace("-","")
    print ">" + fields[0] + "\n" + fields[1]