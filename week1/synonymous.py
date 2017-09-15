#!/usr/bin/env python

"""
Usage: ./synonymous.py <input-file.fa>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import math
import numpy as np

# Making a codon table for iterating through list
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

# Opening the alignment file
alignment = open(sys.argv[1])

# Storing sequences in a list
sequences = []

for DNAIdent, DNASeq in fasta.FASTAReader(alignment):
    sequences.append(DNASeq)

print len(sequences[1])

# Identifying that the query sequence is the first sequence while all other sequences are targets
query_seq = sequences[:1]
target_seq = sequences[1:]

# An list of zeroes to store our counts for synonymous and non-synonymous mutations at each position
dN = []
dS = []

codon_length = 4871

for i in range(codon_length):
    dN.append(0)
    dS.append(0)

# Iterating through each sequence and checking whether the codon is equal or not and then classifying whether the amino acid output was different or not. A codon count is used to position the dN and dS lists while the count is used to position in the DNA sequence
for n in range(len(target_seq)):
    count = 0
    codon_count = 0
    
    while count < 14610:
        query_codon = query_seq[count:count+3]
        target_codon = target_seq[count:count+3]
        
        if "-" in query_codon or target_codon:
            count += 3
            codon_count += 1
            
        elif query_codon != target_codon:
            if codon_table[query_codon] != codon_table[target_codon]:
                dN[codon_count] += 1
                count += 3
                codon_count += 1
                
            elif codon_table[query_codon] == codon_table[target_codon]:
                dS[codon_count] += 1
                count += 3
                codon_count += 1
                
            else:
                pass
                
        elif query_seq == target_seq:
            count += 3
            codon_count += 1
        
        else:
            print 'Error'

# Calculating the difference between non-synonymous and synonymous mutations        
dN_dS = [int(n) - int(s) for n,s in zip(dN, dS)]

# Calculating the z-score
z_score = []

mean_dN_dS = np.mean(dN_dS)
stdev_dN_dS = np.std(dN_dS)

for i in dN_dS:
    z_score.append(float((dN_dS[i]) - 0)/stdev_dN_dS)
 
# Determining whether the z_score is significant and storing that as a 1. If not significant, value is stored as a 0.  
z_score_sig = []

for i in z_score:
    if float(z_score[i]) > 1.96:
        z_score_sig.append(str(1))
    else:
        z_score_sig.append(str(0))
        
print dN
print dS
print z_score
print z_score_sig
            
            
            
        
        