#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt

snpfile = open(sys.argv[1])

snps = []

for line in snpfile:
   if line.startswith("#"):
       continue
   row = line.rstrip("\t\n").split()
   frequency_value = row[7].split(";")
   frequency_number = frequency_value[3][3:]
   frequency_split = frequency_number.split(",")
   for frequency in frequency_split:
       snps.append(float(frequency))
       
plt.figure()
plt.hist(snps, bins=100, color="blue")
plt.xlabel('Genomic Location')
plt.ylabel('Frequency')
plt.title('SNP Manhattan Plot')
plt.savefig(sys.argv[2] + ".png")
plt.close()