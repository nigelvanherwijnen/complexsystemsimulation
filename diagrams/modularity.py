import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import networkx as nx
from network import Graph
import pickle
import numpy as np
import community


e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, \
        2900, 2950, 3050, 3100, 3200, 3300]

# e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, \
#         2900, 2950, 3000, 3050, 3100, 3200, 3300]

y = []

for ne in e:

    graph = pickle.load( open( "graph_16_300_"+str(ne)+"_04.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)

plt.scatter(e, y)
plt.show()
