import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import cProfile

v = 700
e = 8000
a = 1.7
eps = 0.4
np.random.seed(1337)
G = nx.gnm_random_graph(v, e, seed=1337, directed=False)


# initialize nodes
ac_val_list = np.random.uniform(-1.0, 1.0, v)
node_init_list = np.arange(0,v)
dictionary = dict(zip(node_init_list, ac_val_list))
nx.set_node_attributes(G, dictionary, 'activation_val')


# The logistic map function
def log_map(x):
	return 1 - a * x**2


def update_activation_values(G):
	" Updates all activation values at once"
	# remember all old values for synchronous updating
	activation_values_dict = nx.get_node_attributes(G,'activation_val')

	# iterate through all nodes and perform eq. 1
	for node in G.nodes():

		log_map_self = log_map(nx.get_node_attributes(G,'activation_val')[node])
		
		its_neighbors = list(nx.all_neighbors(G, node))
		number_of_neighbors = len(its_neighbors)
		act_val_of_neighbors = np.asarray(list(nx.get_node_attributes(G,'activation_val').values()))[its_neighbors]
		sum_act_neighbors = sum(list(map(log_map,act_val_of_neighbors)))
		log_map_neighbors = sum_act_neighbors

		# Evade division by 0 error
		if number_of_neighbors != 0:
			prefix = eps/number_of_neighbors
		else: prefix = 0

		new_activation_val = (1- eps) *log_map_self + prefix * log_map_neighbors

		# store activation value
		activation_values_dict[node] = new_activation_val

	# put in new updated values
	nx.set_node_attributes(G,activation_values_dict,'activation_val')



def update_edges(G):
	" Updates edges of the network if possible"
	activation_values_array = np.asarray(list(nx.get_node_attributes(G,'activation_val').values()))
	pivot = np.random.randint(0,v)
	pivot_act_val = activation_values_array[pivot]

	# ignores index of pivot itself
	activation_values_array[pivot] = np.nan

	# finds the closest one, assigns candidate
	candidate = np.nanargmin(np.abs((activation_values_array-pivot_act_val)))
	neighbors_array = np.asarray(list(nx.all_neighbors(G, pivot)))

	neighbors_act_val_array = list(map(lambda nb: nx.get_node_attributes(G,'activation_val')[nb],neighbors_array))

	if len(neighbors_array) != 0 and G.has_edge(pivot, candidate) != True:
		outcast_index = np.nanargmax(np.abs((neighbors_act_val_array-pivot_act_val)))
		outcast = neighbors_array[outcast_index]

		G.remove_edge(pivot, outcast)
		G.add_edge(pivot, candidate)

	return

def calc_CC(G):
	cc_list = np.asarray(list(nx.clustering(G).values()))
	cc_min = np.min(cc_list)
	# cc_min_node = cc_list[cc_min]
	cc_max = np.max(cc_list)
	# cc_max_node = cc_list[cc_max]
	cc_avg = np.average(cc_list)
	return cc_min, cc_max, cc_avg

def calc_avg_cc(G):
	return nx.average_clustering(G)

iterations = 1000
cc_min_list = np.empty(iterations)
cc_max_list = np.empty(iterations)
cc_avg_list = np.empty(101)

def run_iterations(G):
	for i in range(0,iterations):


		update_activation_values(G)
		update_edges(G)
		# cc_min_list[i], cc_max_list[i], cc_avg_list[i] = calc_CC(G)

		if i%100 == 0:
			print(i)
			cc_avg_list[i] = calc_avg_cc(G)
	return cc_avg_list	

cProfile.run('run_iterations(G)')

# plt.plot(np.arange(0,iterations), cc_avg_list)
# plt.show()



# plt.subplot(122)
# nx.draw_shell(G, labels = nx.get_node_attributes(G, 'activation_val'), font_size = 5)
# print(nx.get_node_attributes(G, 'activation_val'))
# plt.show()

