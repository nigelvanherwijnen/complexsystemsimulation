import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pickle
import plotly.plotly as py
import plotly
import plotly.graph_objs as go


def plot_chance_connected(graph,rangechoice):
    """
    Function computes connectivity between different activity ranges. It returns a list of normalized values.

    """
    edges = graph.G.edges() #list of all edges
    act_values=nx.get_node_attributes(graph.G, 'value') #dict of all activation values
    val=[]
    for node,value in act_values.items():
        val.append(value)
    val1=[]
    nodes1=[]
    val2=[]
    nodes2=[]
    val3=[]
    nodes3=[]
    val4=[]
    nodes4=[]
    val5=[]
    nodes5=[]
    val6=[]
    nodes6=[]
    val7=[]
    nodes7=[]
    val8=[]
    nodes8=[]
    for i in range(len(val)): #make lists of all nodes in different ranges of activation value, and a list of their activation value
        if val[i]<-.75:
            val1.append(val[i])
            nodes1.append(i)
        elif val[i]>=-.75 and val[i]<-.5:
            val2.append(val[i])
            nodes2.append(i)
        elif val[i]>=-.5 and val[i]<-.25:
            val3.append(val[i])
            nodes3.append(i)
        elif val[i]>=-.25 and val[i]<0:
            val4.append(val[i])
            nodes4.append(i)
        elif val[i]>=0 and val[i]<.25:
            val5.append(val[i])
            nodes5.append(i)
        elif val[i]>=.25 and val[i]<.5:
            val6.append(val[i])
            nodes6.append(i)
        elif val[i]>=.5 and val[i]<.75:
            val7.append(val[i])
            nodes7.append(i)
        elif val[i]>=.75:
            val8.append(val[i])
            nodes8.append(i)

    nodelist=[nodes1,nodes2,nodes3,nodes4,nodes5,nodes6,nodes7,nodes8]
    vallist=[val1,val2,val3,val4,val5,val6,val7,val8]
    connections=[]
    for node in nodelist[rangechoice-1]:
        edges=list(graph.G.edges(node)) #get all nodes that the nodes in our range are connected with
        for j in range(len(edges)):
            neighbor=edges[j][1]
            for k in range(8):
                if val[neighbor]>=(-1+k*(2/8)) and val[neighbor]<(-1+(k+1)*(2/8)): #save range connected node is in
                    connections.append(k+1)

    con=np.zeros((8,1))
    for number in connections: #count connections with certain ranges
        for l in range(8):
            if number==l+1:
                con[l]+=1
    lnode=[len(nodelist[0]),0,0,0,0,0,0,0]
    lnode[1]=len(nodelist[1])
    lnode[2]=len(nodelist[2])
    lnode[3]=len(nodelist[3])
    lnode[4]=len(nodelist[4])
    lnode[5]=len(nodelist[5])
    lnode[6]=len(nodelist[6])
    lnode[7]=len(nodelist[7])

    for i in range(8):
        if lnode[i]==0:
            lnode[i]=1

    con[0]=con[0]/(lnode[rangechoice-1]*lnode[0]) #devide by number of nodes in both ranges to make independent
    con[1]=con[1]/(lnode[rangechoice-1]*lnode[1])
    con[2]=con[2]/(lnode[rangechoice-1]*lnode[2])
    con[3]=con[3]/(lnode[rangechoice-1]*lnode[3])
    con[4]=con[4]/(lnode[rangechoice-1]*lnode[4])
    con[5]=con[5]/(lnode[rangechoice-1]*lnode[5])
    con[6]=con[6]/(lnode[rangechoice-1]*lnode[6])
    con[7]=con[7]/(lnode[rangechoice-1]*lnode[7])

    tot=0
    listcon=[]
    for i in range(8): #normalization
        tot+=con[i][0]
        listcon.append(con[i][0])
    if tot != 0:
        listcon=listcon/tot

    return listcon

def peak_plot():

    plotly.tools.set_credentials_file(username='mirbruin', api_key='EG8PItSCmhBwX6KWnsi5')
    graph = pickle.load(open('pickles_for_plots/graph_10000.p','rb'))


    z_data=[(plot_chance_connected(graph,i+1)) for i in range(8)]

    data = [
        go.Surface(
            z=z_data

        )
    ]

    labels=['[-1,-0.75)','[-0.75,-0.5)','[-0.5,-0.25)','[-0.25,0)','[0,0.25)','[0.25,0.5)','[0.5,0.75)','[0.75,1]']


    layout1 = go.Layout(
                        scene = dict(
                        xaxis = dict(
                            title='Ranges',
                            tickvals=[0,1,2,3,4,5,6,7],
                            ticktext=labels),
                        yaxis = dict(
                            title='Ranges',
                            tickvals=[0,1,2,3,4,5,6,7],
                            ticktext=labels),
                        zaxis = dict(
                            title='P'),),
                        width=700,
                        margin=dict(
                        r=20, b=10,
                        l=10, t=10)
                      )

    fig = go.Figure(data=data, layout=layout1)
    py.iplot(fig,filename='groetjes')
