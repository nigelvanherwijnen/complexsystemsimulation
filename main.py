import pickle
import networkx as nx
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, 'diagrams')
from network import Graph
from cc_draw import plot_phases, plot_cc_e
from iterations_draw import plot_1, plot_3, plot_6
from peaks_plot import plot_chance_connected, peak_plot

if __name__ == '__main__':

    plot_cc_e()
    plot_1()
    plot_3()
    plot_6()
    peak_plot()
