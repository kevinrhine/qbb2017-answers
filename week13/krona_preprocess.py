#!/usr/bin/env python

import sys

kraken = open(sys.argv[1])

krona_dict = {}

for line in kraken:
    fields = line.rstrip("\r\n").split("\t")
    if fields[1] in krona_dict:
        krona_dict[fields[1]] += 1
    else:
        krona_dict[fields[1]] = 1
        
for k, v in krona_dict.iteritems():
    print str(v) + "\t", k