import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from network import Graph
import pickle
import numpy as np

def plot_iterations(x, graphs, title, subplot):

    nv = 300
    N = 10000

    plt.subplot(subplot)

    if subplot == 233 or subplot == 111 or subplot == 133:
        avg = []
        for g in graphs:
            plt.plot(np.linspace(0, N*len(g.cc), len(g.cc)), g.cc, label=g.n_e)
        plt.legend()
    else:
        avg = []
        for g in graphs:
            plt.plot(np.linspace(0, N*len(g.cc), len(g.cc)), g.cc)

    plt.ylabel("CC")
    plt.xlabel("# iterations")
    plt.title(title)

def plot_6():

    nv = 300
    N = 10000

    plt.figure(figsize=(20,10))

    e = [2400, 2800, 3200]
    graphs_14_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_14_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_14_03.append(graph)
    plot_iterations(e, graphs_14_03, "nv=300 | a = 1.4 | eps = 0.3", 231)


    graphs_16_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_16_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_16_03.append(graph)
    plot_iterations(e, graphs_16_03, "nv=300 | a = 1.6 | eps = 0.3", 232)

    graphs_18_03 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_03.p", "rb"))
        graphs_18_03.append(graph)
    plot_iterations(e, graphs_18_03, "nv=300 | a = 1.8 | eps = 0.3", 233)

    graphs_14_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_14_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_14_04.append(graph)
    plot_iterations(e, graphs_14_04, "nv=300 | a = 1.4 | eps = 0.4", 234)

    graphs_16_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_16_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_16_04.append(graph)
    plot_iterations(e, graphs_16_04, "nv=300 | a = 1.6 | eps = 0.4", 235)

    graphs_18_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_18_04.append(graph)
    plot_iterations(e, graphs_18_04, "nv=300 | a = 1.8 | eps = 0.4", 236)


    plt.tight_layout()
    plt.savefig('diagrams/figures/iter_6.png', bbox_inches='tight')
    plt.show()


def plot_1():

    nv = 300
    N = 10000

    plt.figure()
    e = [2400, 2800, 3200]
    graphs_18_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_18_04.append(graph)
    plot_iterations(e, graphs_18_04, "nv=300 | a = 1.8 | eps = 0.4", 111)

    plt.savefig('diagrams/figures/iter_1.png', bbox_inches='tight')
    plt.show()


def plot_3():

    nv = 300
    N = 10000

    plt.figure(figsize=(20,5))
    e = [2400, 2800, 3200]
    graphs_14_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_14_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_14_04.append(graph)
    plot_iterations(e, graphs_14_04, "nv=300 | a = 1.4 | eps = 0.4", 131)

    graphs_16_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_16_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_16_04.append(graph)
    plot_iterations(e, graphs_16_04, "nv=300 | a = 1.6 | eps = 0.4", 132)

    graphs_18_04 = []
    for ne in e:
        graph = pickle.load(open("pickles_for_plots/graph_18_" + str(nv) + "_" + str(ne) + "_04.p", "rb"))
        graphs_18_04.append(graph)
    plot_iterations(e, graphs_18_04, "nv=300 | a = 1.8 | eps = 0.4", 133)


    plt.tight_layout()
    plt.savefig('diagrams/figures/iter_3.png', bbox_inches='tight')
    plt.show()




# def plot_iterations():
#     for i in range(len(e)):
#         plt.plot(np.linspace(0, N*len(graphs[i].cc), len(graphs[i].cc)), graphs[i].cc, label=e[i])
#
#     plt.title("nv=300 | a = 1.6 | eps = 0.3")
#     plt.xlabel("# iterations")
#     plt.ylabel("CC")
#     plt.legend()
#     plt.show()
