import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from network_nigel import Graph
import pickle
import numpy as np

def plot_phases(x, graphs, title, subplot):

    avg = []
    for g in graphs:
        avg.append(np.mean(g.cc[80:]))

    plt.subplot(subplot)
    plt.plot(x, avg)
    plt.ylabel("CC")
    plt.xlabel("# edges")
    plt.title(title)


def plot_cc_e():

    nv = 300
    N = 10000
    a = 1.6
    eps = 0.3

    plt.figure(figsize=(20,10))

    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
    graphs_14_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_14_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_14_03.append(graph)
    plot_phases(e, graphs_14_03, "nv=300 | a = 1.4 | eps = 0.3", 231)


    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
    graphs_16_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_16_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_16_03.append(graph)
    plot_phases(e, graphs_16_03, "nv=300 | a = 1.6 | eps = 0.3", 232)

    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
    graphs_18_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_18_03.append(graph)
    plot_phases(e, graphs_18_03, "nv=300 | a = 1.8 | eps = 0.3", 233)

    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 3000, 3050, 3100, 3200, 3300]
    graphs_14_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_14_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_14_04.append(graph)
    plot_phases(e, graphs_14_04, "nv=300 | a = 1.4 | eps = 0.4", 234)

    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200, 3300]
    graphs_16_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_16_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_16_04.append(graph)
    plot_phases(e, graphs_16_04, "nv=300 | a = 1.6 | eps = 0.4", 235)

    e = [2400, 2500, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3200]
    graphs_18_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_18_04.append(graph)
    plot_phases(e, graphs_18_04, "nv=300 | a = 1.8 | eps = 0.4", 236)


    plt.tight_layout()
    plt.savefig('diagrams/figures/cc_6.png', bbox_inches='tight')
    plt.show()
