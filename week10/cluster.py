#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster as sp
from sklearn.cluster import KMeans

df = pd.read_csv('hema_data.txt', delimiter='\t')
df['cluster'] = range(1, len(df) + 1)
data = df.as_matrix()[:,1:].astype(float)
linked_data = sp.hierarchy.linkage(data,method='average',metric='euclidean')
linked_dataT = sp.hierarchy.linkage(data.T,method='average',metric='euclidean')
heatmap_order_idx = sp.hierarchy.leaves_list(linked_data)
ordered_data = data[heatmap_order_idx, :]
dend_labels = ['CFU','poly','unk','int','mys','mid']

kfunction = KMeans(n_clusters = 7, n_init = 50, max_iter = 1000)
kfunction.fit = (data)
data = pd.merge(pd.DataFrame(data), pd.DataFrame(columns = ['cluster']), left_index = True, left_on = ['cluster'])
s.data = pd.DataFrame.set_index(['cluster'])
#s.data = pd.DataFrame.sort(columns=['cluster'],ascending=True)

# labels = KMeans.predict(data)

plt.figure()
plt.pcolor(ordered_data, cmap='seismic')
plt.colorbar()
plt.xticks()
plt.savefig('hema_data_heatmap.png')
plt.close()

plt.figure()
plt.pcolor(s.data, cmap='seismic')
plt.colorbar()
plt.xticks()
plt.savefig('hema_data_k_cluster.png')
plt.close()

plt.figure()
sp.hierarchy.dendrogram(linked_dataT, labels = dend_labels)
plt.savefig('hema_data_dendrogram.png')
plt.close()
