#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <samples.csv> <samples_ctab_dir> <replicates.csv> <goi>

- plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

gene = sys.argv[4]

df_samples = pd.read_csv(sys.argv[1])
soi_f = df_samples["sex"] == "female"

fpkms_f = []
for sample in df_samples["sample"][soi_f]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep = "\t")
    roi = df["gene_name"] == gene
    running_average = np.mean(df[roi]["FPKM"])
    fpkms_f.append(running_average)
    
soi_m = df_samples["sex"] == "male"

fpkms_m = []
for sample in df_samples["sample"][soi_m]:
    mname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(mname, sep = "\t")
    roi = df["gene_name"] == gene
    running_average = np.mean(df[roi]["FPKM"])
    fpkms_m.append(running_average)
    
df_replicates = pd.read_csv(sys.argv[3])
soi_rf = df_replicates["sex"] == "female"

fpkms_rf = [None, None, None, None]
for replicate in df_replicates["sample"][soi_rf]:
    rfname = os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(rfname, sep = "\t")
    roi = df["gene_name"] == gene
    running_average = np.mean(df[roi]["FPKM"])
    fpkms_rf.append(running_average)
    

soi_rm = df_replicates["sex"] == "male"

fpkms_rm = [None, None, None, None]
for replicate in df_replicates["sample"][soi_rm]:
    rmname = os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(rmname, sep = "\t")
    roi = df["gene_name"] == gene
    running_average = np.mean(df[roi]["FPKM"])
    fpkms_rm.append(running_average)
    
x1 = fpkms_f
x2 = fpkms_m
x3 = fpkms_rf
x4 = fpkms_rm
y = [str(10), str(11), str(12), str(13), str('14A'), str('14B'), str('14C'), str('14D')]
 
    
plt.figure()
plt.plot(x1, c = "pink")
plt.plot(x2, c = "blue")
plt.plot(x3, 'o', c = "red")
plt.plot(x4, 'o', c = "purple")
plt.ylim(0,200)
plt.xticks(range(len(fpkms_f)), df_samples["stage"])
plt.xlabel("Developmental Stage", fontsize = 12)
plt.ylabel("Relative Expression", fontsize = 12)
plt.title("Gender-Biased Expression of " + str(gene))
art =[]
plt.legend(['females', 'males', 'female_replicates', 'male_replicates'], loc = "center right", bbox_to_anchor = (1.5, 0.5), frameon = False, numpoints = 1)
plt.savefig(sys.argv[4] + "_timecourse.png", additional_artists = art, bbox_inches = "tight")
plt.close()