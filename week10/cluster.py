#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster as sp

df = pd.read_csv('hema_data.txt', delimiter='\t')
data = df.as_matrix()[:,1:].astype(float)
linked_data = sp.hierarchy.linkage(data,method='average',metric='euclidean')
linked_dataT = sp.hierarchy.linkage(data.T,method='average',metric='euclidean')
heatmap_order_idx = sp.hierarchy.leaves_list(linked_data)
ordered_data = data[heatmap_order_idx, :]
dend_labels = ['CFU','poly','unk','int','mys','mid']

plt.figure()
plt.pcolor(ordered_data, cmap='seismic')
ax = plt.gca()
ax.set_facecolor('black')
plt.xticks()
plt.savefig('hema_data_heatmap.png')
plt.close()

plt.figure()
sp.hierarchy.dendrogram(linked_dataT, labels = dend_labels)
plt.savefig('hema_data_dendrogram.png')
plt.close()
