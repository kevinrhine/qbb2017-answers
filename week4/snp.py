#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

vcf = open( sys.argv[1] )

allele_freqs = []

for line in vcf:
    if line.startswith( '#' ):
        pass
    else:
        segs = line.rstrip('\r\n').split('\t')
        freqs = segs[7].lstrip('AF=').split(',')
        for freq in freqs:
            allele_freqs.append(float(freq))

plt.figure()
plt.hist( allele_freqs, bins=100 )
plt.xlabel( 'Alleles' )
plt.ylabel( 'Counts' )
plt.title( 'SNPs' )
plt.savefig( sys.argv[2] )
plt.close()