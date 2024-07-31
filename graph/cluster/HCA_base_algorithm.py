from typing import List

from graph.node import Node
from graph.edge import Edge
from graph.co_occurence import CoOccurence
from graph.graph import Graph

import copy

class HCAAlgorithm:

    def __init__(self) -> None:
        pass

    def cluster(self, co_occurence: CoOccurence):
        # copy old graph
        old_graph = copy.deepcopy(co_occurence.graph)
        # copy graph without edges
        new_graph = Graph()
        # TODO check which copy
        # new_graph.nodes = old_graph.nodes.copy()
        new_graph.nodes = copy.deepcopy(old_graph.nodes)

        isolated_nodes = []
        connected_nodes = copy.deepcopy(old_graph.nodes)

        h = 1
        sigma = 0
        i = 0

        while len(connected_nodes) != 0:
            for edge in old_graph.edges:
                if edge.significance() < sigma:
                    old_graph.edges.remove(edge)
            
            for node in old_graph.nodes:
                if node.degree() == 0:
                    del connected_nodes[]

