import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


v = 100
e = 60
a = 1.7
eps = 0.4
np.random.seed(1337)
G = nx.gnm_random_graph(v, e, seed=1337, directed=False)


# initialize nodes
ac_val_list = np.random.uniform(-1.0, 1.0, v)
node_init_list = np.arange(0,v)
dictionary = dict(zip(node_init_list, ac_val_list))
nx.set_node_attributes(G, dictionary, 'activation_val')

# Draws initial graph
plt.subplot(121)
nx.draw_shell(G, with_labels = True)


# The logistic map function
def log_map(x):
	return 1 - a * x**2

# The Update Units function
def update_activation_values(G):
	# remember all old values for synchronous updating
	activation_values_dict = nx.get_node_attributes(G,'activation_val')

	# iterate through all nodes and perform eq. 1
	for node in G.nodes():

		log_map_self = log_map(nx.get_node_attributes(G,'activation_val')[node])
		
		its_neighbors = list(nx.all_neighbors(G, node))
		number_of_neighbors = len(its_neighbors)
		sum_act_neighbors = sum(list(map(log_map,list(map(lambda neighbor: nx.get_node_attributes(G,'activation_val')[neighbor],its_neighbors)))))
		log_map_neighbors = sum_act_neighbors

		if number_of_neighbors != 0:
			prefix = eps/number_of_neighbors
		else: prefix = 0

		new_activation_val = (1- eps) *log_map_self + prefix * log_map_neighbors

		# store activation value
		activation_values_dict[node] = new_activation_val

	# put in new updated values
	nx.set_node_attributes(G,activation_values_dict,'activation_val')


# update_activation_values(G)

def update_edges(G):

	activation_values_array = np.asarray(list(nx.get_node_attributes(G,'activation_val').values()))
	pivot = np.random.randint(0,v)
	pivot_act_val = activation_values_array[pivot]

	# ignores index of pivot itself
	activation_values_array[pivot] = np.nan

	# finds the closest one, assigns candidate
	candidate = np.nanargmin(np.abs((activation_values_array-pivot_act_val)))
	# candidate_act_val = activation_values_array[candidate]

	# print(pivot, pivot_act_val)
	neighbors_array = np.asarray(list(nx.all_neighbors(G, pivot)))
	# print(neighbors_array)

	neighbors_act_val_array = list(map(lambda nb: nx.get_node_attributes(G,'activation_val')[nb],neighbors_array))
	# print(neighbors_act_val_array)
	# print('neighborsactval - pivot act', neighbors_act_val_array-pivot_act_val)

	if len(neighbors_array) != 0 and G.has_edge(pivot, candidate) != True:
		outcast_index = np.nanargmax(np.abs((neighbors_act_val_array-pivot_act_val)))
		outcast = neighbors_array[outcast_index]
		# print('pivot',pivot)
		# print('outcast',outcast)
		G.remove_edge(pivot, outcast)
		G.add_edge(pivot, candidate)



	return

plt.show()

for i in range(0,3000):
	# print(i)
	update_activation_values(G)

# plt.subplot(132)
# nx.draw_shell(G, labels = nx.get_node_attributes(G, 'activation_val'), font_size = 5)

	update_edges(G)

plt.subplot(122)
nx.draw_shell(G, labels = nx.get_node_attributes(G, 'activation_val'), font_size = 5)
print(nx.get_node_attributes(G, 'activation_val'))
plt.show()







