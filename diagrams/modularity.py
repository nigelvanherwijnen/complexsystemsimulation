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


plt.figure(figsize=(20,10))

plt.subplot(231)
e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200]
y = []
for ne in e:
    graph = pickle.load( open( "graph_14_300_"+str(ne)+"_03.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.4 | eps = 0.3")


plt.subplot(232)
e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
y = []
for ne in e:
    graph = pickle.load( open( "graph_16_300_"+str(ne)+"_03.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.6 | eps = 0.3")

plt.subplot(233)
e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
y = []
for ne in e:
    graph = pickle.load( open( "graph_18_300_"+str(ne)+"_03.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.8 | eps = 0.3")

plt.subplot(234)
e = [2400, 2500, 2600, 2700, 2800, 2900, 3000, 3050, 3100, 3200]
y = []
for ne in e:
    graph = pickle.load( open( "graph_14_300_"+str(ne)+"_04.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.4 | eps = 0.4")

plt.subplot(235)
e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
y = []
for ne in e:
    graph = pickle.load( open( "graph_16_300_"+str(ne)+"_04.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.6 | eps = 0.4")

plt.subplot(236)
e = [2400, 2500, 2600, 2650, 2750, 2850]
y = []
for ne in e:
    graph = pickle.load( open( "graph_18_300_"+str(ne)+"_04.p", "rb"))
    part = community.best_partition(graph.G)
    mod = community.modularity(part, graph.G)
    y.append(mod)
plt.scatter(e, y)
plt.xlabel("# edges")
plt.ylabel("modularity")
plt.title("nv=300 | a = 1.8 | eps = 0.4")

plt.tight_layout()
plt.savefig('figures/mod_6.png', bbox_inches='tight')
plt.show()
