#!/usr/bin/env python

"""
Usage: ./02-stratify.py <ctab-1> <ctab-2 <prefix> <x-axis name> <y-axis name>

- Find FPKM values for two files
- Convert them to log values
- 
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

file1_d = {}
fpkm_match_1 = []
fpkm_match_2 = []
fpkm_match_1_log = []
fpkm_match_2_log = []

# Opening the file and telling pandas that it needs to read by tab delimiter
df1 = pd.read_csv (sys.argv[1], sep="\t")

# Telling pandas that I'm only interested in entries with an FPKM > 0
roi = df1["FPKM"] != 0.000000

fpkm = df1["FPKM"]
t_name = df1["t_name"]
 
for i in range(len(fpkm)):
    file1_d[t_name[i]] = fpkm[i]

df2 = pd.read_csv (sys.argv[2], sep="\t")

roi_2 = df2["FPKM"] != 0.000000

fpkm_2 = df2["FPKM"]
t_name_2 = df2["t_name"]

for i in range(len(fpkm_2)):
    if t_name_2[i] in file1_d:
        fpkm_match_2.append(fpkm_2[i])
        fpkm_match_1.append(file1_d[t_name_2[i]])

print fpkm_match_1[:10]
print fpkm_match_2[:10]

for i in reversed(range(len(fpkm_match_1) - 1)):
    if int(fpkm_match_1[i]) == 0 or int(fpkm_match_2[i]) == 0:
        fpkm_match_1.pop(i)
        fpkm_match_2.pop(i)
        
print fpkm_match_1[:10]
print fpkm_match_2[:10]
        
for i in range(len(fpkm_match_1) - 1):
    fpkm_match_1_log.append(math.log10(fpkm_match_1[i]))
    fpkm_match_2_log.append(math.log10(fpkm_match_2[i]))

print fpkm_match_1_log[:10]
print fpkm_match_2_log[:10]

x = np.array(fpkm_match_1_log)
y = np.array(fpkm_match_2_log)

m, b = np.polyfit(x, y, 1)


plt.figure()
plt.scatter(x, y, c = "Red", alpha = 0.3, s = 1)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xlabel("log expression of " + str(sys.argv[4]), fontsize = 10)
plt.ylabel("log expression of " + str(sys.argv[5]), fontsize = 10)
plt.grid(True)
plt.title("Expression Correlation between " + str(sys.argv[4]) + "and " + str(sys.argv[5]))
plt.plot(x, m * x + b, '-', c = "m")
plt.savefig(sys.argv[3] + ".png")
plt.close()
        

        
    

