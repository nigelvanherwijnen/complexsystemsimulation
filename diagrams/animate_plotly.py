import plotly.plotly as py
import plotly.graph_objs as go
import networkx as nx
# import numpy as np
# import random
import pickle
from network import Graph



"THIS CREATES THE POSITIONS FOR THE NODES BASED ON MOST EVOLUTED GRAPH."
def create_node_positions(final_graph):
    layt = nx.spring_layout(final_graph,dim=3)
    N = nx.number_of_nodes(final_graph)

    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates

    return layt, Xn, Yn, Zn

"CREATES THE COORDINATES FOR THE LINES CONNECTING THE NODES, AS WELL AS THE ACTIVATION VALUE OF THE NODES"

def create_edge_positions(layt, graph_edges):
    Edges = nx.edges(graph_edges)
    Xe=[]
    Ye=[]
    Ze=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]

    return Xe, Ye, Ze

    "TURNS POSITIONS INTO PLOTLY TRACES"
def create_scatter_objects(Xn, Yn, Zn, Xe, Ye, Ze, act_val):
    trace1=go.Scatter3d(x=Xe,
                   y=Ye,
                   z=Ze,
                   mode='lines',
                   line=dict(color='black', width=0.8),
                   hoverinfo='none',
                        opacity = 0.3
                   )
    trace2=go.Scatter3d(x=Xn,
                   y=Yn,
                   z=Zn,
                   mode='markers',
                   name='actors',
                   marker=dict(symbol='dot',
                                 size=5,
                                 color=act_val,
                                 colorscale='Greens',
                               reversescale = True
                                 ),
                   text = 'act_val = '+str(act_val),
                   hoverinfo= 'text'
                   )
    return [trace1, trace2]

    "PLOTLY LAYOUT OF GRAPH"
def create_layout():
    axis=dict(showbackground=False,
#               range=[-2, 2],
              showline=False,
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title=''
              )

    layout = go.Layout(
             title="Small world random network",
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]},
                    {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }]}],
             width=1000,
             height=500,
             showlegend=False,
             scene=dict(
                 xaxis=dict(axis),
                 yaxis=dict(axis),
                 zaxis=dict(axis),
            ),
         margin=dict(
            t=100
        ),
        hovermode='closest',
        annotations=[
               dict(
               showarrow=False,
                text="© MIRJAM THOMAS NIGEL MAARTEN",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=dict(
                size=14
                )
                )
            ],    )
    return layout

    "CREATES NEW GRAPHS AND SAVES THEM USING PICKLE"


def build_fig():

	pickle_graphs = []
	data = []
	print('building figure')

	for i in range(200):
		# print('starting opening')
		# if i%10==0:
		# 	print(i)
		if i%20==0:
			pickle_graphs.append(pickle.load(open('pickles_for_animation/big_graph_timestep_'+str(i+1)+'.p',"rb")))


	layt, Xn, Yn, Zn = create_node_positions(pickle_graphs[-1].G)
	# DATA WILL HAVE ALL DATA OF ALL FRAMES
	for i, graph in enumerate(pickle_graphs):
	    Xe, Ye, Ze = create_edge_positions(layt, graph.G)
	    act_val = list(nx.get_node_attributes(graph.G, "value").values())
	    traces = create_scatter_objects(Xn, Yn, Zn, Xe, Ye, Ze, act_val)
	    data.append(traces)

	"OPENS PICKLE GRAPHS"



	layout = create_layout()
	frames = [dict(data=data[i]) for i in range(1,len(data))]

	figure=dict(data=data[0], layout=layout, frames=frames)
	return figure
