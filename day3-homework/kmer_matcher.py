#!/usr/bin/env python

"""
This script aligns k_mers within a query sequence to a target library.

Usage: ./kmer_matcher.py < query.fa > < target.fa > < k >
"""

import sys
import fasta

# Assigning values from Unix shell input
query = open(sys.argv[1])
target = open(sys.argv[2])
k = int(sys.argv[3])

target_kmer = {}
target_ident = {}
count = 0
count_2 = 0

for ident, sequence in fasta.FASTAReader(target):

    # Remove identifier for repetitive sequences i.e. lowercase letters
    sequence = sequence.upper() 
    
    # Our cycling loop looking for kmers
    for i in range(0,len(sequence) - k):
        
        # This sets our kmer equal to our range
        kmer_t = sequence[i:i+k]
        
        # Counting the position
        count = count + 1
        
        c_i = (ident, i)
        
        #index = []
        
        if kmer_t not in target_kmer:
            
            index = c_i
            
            target_kmer[kmer_t] = [index]
        
        else:
            
            target_kmer[kmer_t].append(c_i)

q_ident, q_sequence = fasta.FASTAReader(query).next()

        # Our cycling loop looking for kmers
for i in range(0,len(q_sequence) - k):
        
            # Counting the position
    count_2 += 1
        
    q_kmer = q_sequence[i:i+k]
        
            # Add kmer to dictionary with corresponding index number
    if q_kmer in target_kmer.keys():
        
        for line in target_kmer[q_kmer]:
            
            print "Target Name: ", target_kmer[q_kmer]
            print "Query Position: ", count_2
            print "kmer: ", q_kmer
            print ""

    else:
        continue