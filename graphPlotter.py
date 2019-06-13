import networkx as nx
import matplotlib.pyplot as plt
from stateNode import stateNode
from graphviz import Digraph
import re

def drawCurrentlyExploredNodes(statesCompletelyExplored):

    # Instantiating the directional graph
    graph = nx.DiGraph()
    # Iterating over all states that are completely explored
    for exploredState in statesCompletelyExplored:
        # Iterating over the outgoing edges of this state
        edges = exploredState.getOutgoingStateDictionary()
        for uiKey, arrivingState in edges.items():
            graph.add_edge(exploredState.getStateName(), arrivingState.getStateName())
    # Setting the layout type for the graph
    pos = nx.spring_layout(graph)
    # Setting the figure size
    plt.figure(dpi=500)
    nx.draw(graph, pos, with_labels=True)
    plt.show()
    # plt.savefig("simple_path.png")



def drawCurrentlyExploredNodesGraphivz(statesCompletelyExplored):

    # Instantiating the directional graph
    graph = Digraph('G', filename='C:/Users/artur/PycharmProjects/AndroidTestingPy27/charts/outputGraph.gv', format='png')
    # Iterating over all states that are completely explored
    for exploredState in statesCompletelyExplored:
        # Iterating over the outgoing edges of this state
        edges = exploredState.getOutgoingStateDictionary()
        for uiKey, arrivingState in edges.items():
            # Crafting a compact version of the node name
            startNum = re.sub("[^0-9]", "", exploredState.getStateName())
            arrivingNum = re.sub("[^0-9]", "", arrivingState.getStateName())
            startName = "s" + startNum
            arrivingName = "s" + arrivingNum
            # Instantiating the new edge
            graph.edge(startName, arrivingName, label=str(uiKey))
    graph.render(filename='C:/Users/artur/PycharmProjects/AndroidTestingPy27/charts/outputGraph.gv', format='png')