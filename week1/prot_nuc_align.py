#!/usr/bin/env python

"""

"""

import sys
import itertools
import fasta

prot = open(sys.argv[1])
nuc = open(sys.argv[2])
alignment = open(sys.argv[3],"w")

for (nucIdent, nucSeq), (protIdent, protSeq) in itertools.izip(fasta.FASTAReader(nuc), fasta.FASTAReader(prot)):
    alignment.write(">"+nucIdent+"\n")
    for amino in protSeq:
        if amino == "-":
            alignment.write("---")
        else:
            alignment.write(nucSeq[:3])
            nucSeq = nucSeq[3:]
    alignment.write("\n")