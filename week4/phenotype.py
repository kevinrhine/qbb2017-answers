#!/usr/bin/env python

import sys

for line in open(sys.argv[1]):
    if 'Caffeine' in line:
        name = ['fid', 'iid'] + line.rstrip('\r\n').split('\t')[1:]
        print ('\t').join(name)
    else:
        line = line.rstrip('\r\n').split('\t')
        ids = [line[0].split('_')[0], line[0].split('_')[0]]
        new_line = ids + line[1:]
        print ('\t').join(new_line)