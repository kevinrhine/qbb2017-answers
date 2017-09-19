#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tsv = open(sys.argv[1])

c_length = 0
contigs_seen = []

plt.figure()
for i in tsv:
    fields = i.split("\t")
    current_contig = fields[5]
    if "start" in i:
        continue
    else:
        plt.plot([(c_length+float(fields[1])),(c_length+float(fields[3]))],[(int(fields[0])),(int(fields[2]))])
        c_length += int(fields[4])
        contigs_seen.append(fields[5])
plt.xlabel("Contig Position")
plt.ylabel("Genomic Position")
plt.title(str(sys.argv[2]))      
plt.savefig((sys.argv[2]) + ".png")
plt.close()


"""
1. keep a running count on the x axis of contig length and add for each new contig
2. actually use the contig lengths
3. ignore if contig has already been seen
4. match by name (it's already sorted this way)

"""