import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import numpy as np
import scipy as sp
import random
import itertools
from pydash import at
import cProfile
import re
from numba import jitclass
from numba import int32, float32
import pickle
import math


class Graph:

    def __init__(self, n_v, n_e, a=1.7, eps=0.4):
        """
        @n_v: number of nodes (int)
        @n_e: number of edges (int)
        @a: control parameter of logistic map (float)
        @eps: coupling strength (float)

        Initializes a random network.
        """

        # Save parameters
        self.n_v = n_v
        self.n_e = n_e
        self.a = a
        self.eps = eps

        # Define arrays to store CC and CPL
        self.cc = []
        self.cpl = []

        # Set seed for testing
        # np.random.seed(1337)

        # Initialize random network
        self.G = nx.gnm_random_graph(n_v, n_e)

        # Compute initial value for each node
        init_values = np.random.uniform(-1, 1, n_v)
        init_attr = dict()
        for i in range(n_v):
            init_attr[i] = {'value': init_values[i]}

        # Set initial value for each node
        nx.set_node_attributes(self.G, init_attr)

        print('Graph initialized')

    def timestep(self, t):
        """
        @t: number of timesteps to be made (int)

        Performs a number of rewiring timesteps
        """

        # Perform t iterations
        for i in range(t):

            # Update values in nodes
            self.update_attr()

            # Determine pivot, candidate and outcast
            pivot, candidate, outcast = self.pivot()

            # Rewire if possible
            self.rewire(pivot, candidate, outcast)

        # Calculate CC
        self.cc.append(nx.average_clustering(self.G))

        # # Compute all subcomponents
        # subcomp = nx.connected_components(self.G)
        #
        # # Calculate CPL
        # self.cpl.append(0)
        # for comp in subcomp:
        #     self.cpl[-1] += (nx.average_shortest_path_length(self.G.subgraph(comp)) \
        #                         * (len(comp) / self.n_v))


    def update_attr(self):
        """
        Calculates all new values of all nodes in the graph.
        """

        # Retrieve all current values
        all_values = nx.get_node_attributes(self.G, 'value')

        # Create variable to store new values
        new_values = {}

        # Loop over all nodes
        for i in range(self.n_v):

            # Obtain list of neighbors
            neighbors = list(nx.all_neighbors(self.G, i))

            # Compute part dependent on own node
            # new_value = (1 - self.eps) * self.logistic_map(all_values[i])
            val_i = all_values[i]
            new_value = (1 - self.eps) * (1 - self.a * val_i * val_i)

            # Compute part dependent on neighbor nodes
            neighbors_value = 0
            for neighbor in neighbors:
                val_n = all_values[neighbor]
                # neighbors_value += self.logistic_map(all_values[neighbor])
                neighbors_value += (1 - self.a * val_n * val_n)

            # Catch nodes without neighbors
            try:
                new_value += neighbors_value * (self.eps/len(neighbors))
            except ZeroDivisionError:
                pass

            # Save new value
            new_values[i] = {'value': new_value}

        # Update node value
        nx.set_node_attributes(self.G, new_values)


    def logistic_map(self, x):
        """
        @x: numeric value (int or float)

        Computes the logistic map f(x) = 1 - a * x^2.
        """

        # Return computed value
        return 1 - self.a * x * x


    def pivot(self):
        """
        Rewires a connection from a randomly chosen node to a node with the
        closest value.
        """

        # Pick random pivot node
        pivot = np.random.randint(self.n_v)

        # Get list of neighbors
        neighbors = np.asarray(list(nx.all_neighbors(self.G, pivot)))

        # Return if no neighbors are available
        if len(neighbors) == 0:
            return pivot, pivot, pivot

        # Collect all values
        values = np.asarray(list(nx.get_node_attributes(self.G, 'value').values()))

        # Save pivot value and set to NaN
        pivot_val = values[pivot]
        values[pivot] = np.nan

        # Find candidate
        candidate = np.nanargmin(np.abs(values - pivot_val))

        # Compute outcast
        neighbors_values = values[neighbors]
        outcast = neighbors[np.argmax(np.abs(neighbors_values - pivot_val))]

        # Return pivot and candidate
        return pivot, candidate, outcast

    def rewire(self, pivot, candidate, outcast):
        """
        @pivot: node used as pivot (int)
        @candidate: node to rewire to from pivot (int)
        @outcast: node to drop edge from if needed (int)

        Rewires one of the pivot's connections to the candidate if not
        already connected. If pivot and candidate are the same node, no
        rewire is possible
        """

        # Retrieve all edges connected to pivot node
        edges = list(self.G.edges([pivot]))

        # Check if pivot and candidate are connected and if rewire is possible
        if ((pivot, candidate) not in edges) \
            and (pivot != candidate) \
            and (candidate != outcast):

            # Connect if not yet connected
            self.G.add_edge(pivot, candidate)

            # Drop edge from pivot to outcast
            self.G.remove_edge(pivot, outcast)

    def draw(self):
        """
        Draws the graph.
        """

        # plt.figure(figsize=(8, 8))
        nx.draw_kamada_kawai(self.G, node_color=list(nx.get_node_attributes(self.G, 'value')),
                    cmap=plt.cm.Reds_r, node_size=50)
        # plt.axis('off')
        # plt.show()
