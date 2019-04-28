import networkx as nx
import matplotlib.pyplot as plt
from stateNode import stateNode


def drawCurrentlyExploredNodes(statesCompletelyExplored):

    # Instantiating the directional graph
    graph = nx.DiGraph()
    # Iterating over all states that are completely explored
    for exploredState in statesCompletelyExplored:
        # Iterating over the outgoing edges of this state
        edges = exploredState.getOutgoingStateDictionary()
        for uiKey, arrivingState in edges.items():
            graph.add_edge(exploredState.getStateName(), arrivingState.getStateName())
    nx.draw(graph, with_labels=True)
    plt.show()
    plt.savefig("simple_path.png")