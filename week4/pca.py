#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy

pca = open(sys.argv[1])

pc_1 = []
pc_2 = []

for line in pca:
    fields = line.split(" ")
    pc_1.append(fields[3])
    pc_2.append(fields[4])
    
plt.figure()
plt.scatter(pc_1, pc_2)
plt.savefig("pca.png")
plt.close()    