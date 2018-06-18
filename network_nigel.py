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
# from operator import itemgetter
from pydash import at

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

        # Set seed for testing
        np.random.seed(1337)

        # Initialize random network
        self.G = nx.gnm_random_graph(n_v, n_e, seed=1337)

        # Compute initial value for each node
        init_values = np.random.uniform(-1, 1, n_v)
        init_attr = dict()
        for i in range(n_v):
            init_attr[i] = {'value': init_values[i]}

        # Set initial value for each node
        nx.set_node_attributes(self.G, init_attr)

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
            pivot, candidate, outcast = graph.pivot()

            # Rewire if possible
            self.rewire(pivot, candidate, outcast)

    def update_attr(self):
        """
        Calculates all new values of all nodes in the graph.
        """

        # Retrieve all current values
        all_values = nx.get_node_attributes(self.G, 'value')

        # Loop over all nodes
        for i in range(self.n_v):

            # Obtain list of neighbors
            neighbors = list(nx.all_neighbors(self.G, i))

            # Compute part dependent on own node
            new_value = (1 - self.eps) * self.logistic_map(all_values[i])

            # Compute part dependent on neighbor nodes
            neighbors_value = 0
            for j, neighbor in enumerate(neighbors):
                neighbors_value += self.logistic_map(all_values[neighbor])

            # Catch nodes without neighbors
            try:
                new_value += neighbors_value * (self.eps/len(neighbors))
            except ZeroDivisionError:
                pass

            # Update node value
            nx.set_node_attributes(self.G, {i: {'value': new_value}})


    def logistic_map(self, x):
        """
        @x: numeric value (int or float)

        Computes the logistic map f(x) = 1 - a * x^2.
        """

        # Return computed value
        return 1 - self.a * (x**2)


    def pivot(self):
        """
        Rewires a connection from a randomly chosen node to a node with the
        closest value.
        """

        # Pick random pivot node
        pivot = np.random.randint(self.n_v)

        # Get list of neighbors
        neighbors = list(nx.all_neighbors(self.G, pivot))

        # Return if no neighbors are available
        if len(neighbors) == 0:
            return pivot, pivot, pivot

        # Collect all values
        values = nx.get_node_attributes(self.G, 'value')

        # Initialize variables
        vmin, candidate = 1, 1
        vmax, outcast = 0, 0

        # Loop over all nodes
        for i in range(self.n_v):

            # Calculate value difference
            value_diff = abs(values[i] - values[pivot])

            # If new minimum difference, save
            if (value_diff < vmin) and (i != pivot):
                vmin = value_diff
                candidate = i

            # If new maximum difference, save
            if (value_diff >= vmax) and (i in neighbors):
                vmax = value_diff
                outcast = i

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
        nx.draw(self.G, node_color=list(nx.get_node_attributes(graph.G, 'value')),
                    cmap=plt.cm.Reds_r, node_size=80)
        # plt.axis('off')
        # plt.show()





# graph = Graph(4, 2)
# plt.subplot(121)
# nx.draw_circular(graph.G, with_labels=True, labels=nx.get_node_attributes(graph.G, 'value'), font_size=8)
# graph.timestep(1)
# print(nx.get_node_attributes(graph.G, 'value'))
# plt.subplot(122)
# nx.draw_circular(graph.G, with_labels=True, labels=nx.get_node_attributes(graph.G, 'value'), font_size=8)
# plt.show()

graph = Graph(100, 60)

plt.figure(figsize=(12, 12))
plt.subplot(221)
graph.draw()

plt.subplot(222)
graph.timestep(1000)
graph.draw()

plt.subplot(223)
graph.timestep(1000)
graph.draw()

plt.subplot(224)
graph.timestep(1000)
graph.draw()

plt.show()
