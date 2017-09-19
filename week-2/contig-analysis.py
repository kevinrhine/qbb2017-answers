#!/usr/bin/env python



import fasta
import sys
import numpy as np

fasta_file = open(sys.argv[1])

nuc_sequences = []

for ident,sequences in fasta.FASTAReader(fasta_file):
    nuc_sequences.append(sequences)

nuc_sequences.sort()

nuc_length = []

for i in range(len(nuc_sequences)):
    nuc_length.append(len(nuc_sequences[i]))
    
nuc_length.sort()

nuc_mean = np.mean(nuc_length)
    
for i in range(len(nuc_length)):
    string_len = sum(nuc_length)
    string_len_2 = string_len / 2

count = 0
for i in nuc_length:
    if count < string_len_2:
        count += i
    else:
        nuc_ND50 = str(i)
        break

print "Max Contig = " + str(max(nuc_length))
print "Min Contig = " + str(min(nuc_length))
print "Mean Contig = " + str(nuc_mean)
print "ND50 = " + str(nuc_ND50)
    