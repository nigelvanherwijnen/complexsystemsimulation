import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import copy
import cProfile

"""
This class simulates a network of neurons that is rewired each timestep. The 
procedure of rewiring is described in Van Den Berg et al. (2005).
"""
class Network:

	# Set parameter valuesand initialise a random network with weights [-1,1]
    def __init__(self, n_v, n_e):
        self.a = 1.7 # Alpha value
        self.e = 0.4 # Epsilon value
        self.n_v = n_v # Number of vertices
        self.n_e = n_e # Number of edges
        self.G = nx.gnm_random_graph(n_v, n_e, seed=133333333333337)
        nx.set_node_attributes(self.G, 'weight', np.random.uniform(-1,1))

    # Logistic function used in update
    def logistic(self, weight):
        return (1 - self.a * weight**2)

    # Rewire the pivot to the candidate and cut connection to the outcast
    # Only if connection to candidate not already present and outcast present
    def rewire(self, pivot, candidate):
        nbrs = self.G.neighbors(pivot)
        if len(nbrs) > 0 and not self.G.has_edge(pivot, candidate):
            weight = nx.get_node_attributes(self.G, 'weight')
            nbr_weights = [np.abs(weight[nbr] - weight[pivot]) for nbr in nbrs]
            outcast = nbrs[nbr_weights.index(np.max(nbr_weights))]
            self.G.add_edge(pivot, candidate)

    # Assign new activation value (weight) to each node based on its own weight
    # and the mean of its neigbours' to which the logistic function is applied
    def update(self):
        weight = nx.get_node_attributes(self.G, 'weight')
        new_weight = copy.deepcopy(weight)
        for n in self.G.nodes():
            f_nbr_weights = [self.logistic(weight[nbr]) for nbr in self.G.neighbors(n)]
            d1 = (1 - self.e) * self.logistic(weight[n])
            if len(f_nbr_weights) > 0:
                d2 = self.e * np.mean(f_nbr_weights)
                new_weight[n] = d1 + d2
            else:
                new_weight[n] = d1

    # Randomly select a pivot and pick a candidate from the remaining node with 
    # the closest activation value
    def pivot(self):
        weight = nx.get_node_attributes(self.G, 'weight')
        nodes = copy.deepcopy(self.G.nodes())
        np.random.shuffle(nodes)
        pivot = nodes.pop()
        weight_diff = [abs(weight[i] - weight[pivot]) for i in nodes]
        candidate = nodes[weight_diff.index(min(weight_diff))]
        self.rewire(pivot, candidate)


# Create a network and apply the update, pivot and rewire function for 
# 'iterations' times
def run(iterations=30000, n_v=700, n_e=8000):
    net = Network(n_v, n_e)
    cluster = []
    for i in range(iterations):
        net.update()
        if i%100 == 0:
            print(i)
            cluster.append(nx.average_clustering(net.G))
        net.pivot()
# cProfile.run('run()')    
    plt.plot(cluster)
    plt.show()
    
run()