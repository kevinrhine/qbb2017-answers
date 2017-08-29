#!/usr/bin/env python

import sys

fh = open( sys.argv[1] )


for the_line in fh:
    if "DROME" in the_line:
        fields = the_line.rstrip("\r\n").split()
        if len(fields) == 4:
            print fields[3], fields[2]
        else:
            continue