#!/usr/bin/env python

import sys

#so we can ref later
fh = sys.stdin

for line in fh:
    #start and end are in columsn 3 and 4
    if line.startswith("t_id"):
        continue
    fields = line.split("\t")
    print int(fields[4]) - int(fields[3])