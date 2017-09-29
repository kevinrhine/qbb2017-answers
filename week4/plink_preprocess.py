#!/usr/bin/env python

import sys

pheno = open(sys.argv[1])
pheno_processed = open((sys.argv[2]), 'w')

for line in pheno:
    if line.startswith("\t"):
        pheno_processed.write("FID")
        pheno_processed.write("\t")
        pheno_processed.write("IID")
        pheno_processed.write(line)
        pheno_processed.write("\n")
    else:
        fields = line.split("\t")
        sfields = fields[0].split("_", 1)
        pheno_processed.write(sfields[0])
        pheno_processed.write("\t")
        pheno_processed.write(sfields[1])
        pheno_processed.write("\t")
        pheno_processed.write("\t".join(fields[1:]))
        
        