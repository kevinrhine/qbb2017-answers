#!/usr/bin/env python

"""
Usage:
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import statsmodels.api as sm

fpkms = []
df = pd.read_csv(sys.argv[1], sep="\t")
fpkms = df["FPKM"].values.tolist()

histone_mean = []
fh = open(sys.argv[2])

for line in fh:
    fields = line.rstrip("\r\n").split()
    histone_mean.append(float(fields[4]))

print len(histone_mean)
print len(fpkms)

model = sm.OLS(histone_mean, fpkms)
results = model.fit()



#plt.figure()
#plt.savefig()
#plt.close()