#!/usr/bin/env python

import sys
import pandas as pd

# Telling the program that our file is tab delimited, not comma delimited
df = pd.read_csv(sys.argv[1], sep="\t")

# Defining our desired output columns
coi = ["chr", "promoter_start", "promoter_end", "t_name"]

# Creating a new column called "width" that consists of other columns 
roi_pos = df["strand"] == "+"
roi_neg = df["strand"] == "-"

for strand in df["strand"][roi_pos]:

    df["promoter_start"] = df["start"] - 499
    df["promoter_end"] = df["start"] + 501

for strand in df["strand"][roi_neg]:

    df["promoter_start"] = df["end"] - 499
    df["promoter_end"] = df["end"] + 501
    
num = df._get_numeric_data()
num[num<0] = 0

df[coi].to_csv(sys.argv[2], sep = "\t", index = False, header = False)