import logging
from typing import List

from graph.node import Node
from graph.edge import Edge, UndirectedEdge
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

        # Initialize
        # h >= 1
        h = 1
        sigma = 0
        # result i >= 2
        i = 0

        while len(connected_nodes) != 0:
            for edge in old_graph.edges:
                # TODO what function should be used for the significance
                if edge.significance() < sigma:
                    old_graph.edges.remove(edge)
            
            for node in old_graph.nodes:
                if node.degree() == 0:
                    isolated_nodes.append(node)
                    del connected_nodes[node.word]
                    if len(connected_nodes) != 0:
                        # find nearest neighbor w_nn of w_u in W_conn
                        nearest_neighbor = self.find_nearest_neighbor(node)
                        # create edge e(w_u, w_nn) in G'
                        nearest_neighbor_edge = UndirectedEdge(nodes=(node, nearest_neighbor))
                        new_graph.undirected_edges.append(nearest_neighbor_edge)

                        isolated_nodes.remove(node)
                    else:
                        # Nodes at step i-1 must be root nodes in G'

                        pass

            # update simga_i, sigma_max > sigma_i > sigma_i-1
            # TODO add sigma_max
            sigma = sigma + (1 / h)
            i += 1

    def find_nearest_neighbor(self, node: Node) -> Node:
        if len(node.undirected_edges.values()) == 0:
            logging.error(f"The node {node.word} don't have a neighbor.")
            raise Exception(f"The node {node.word} don't have a neighbor.")

        nearest_neighbor: Node = Node("empty")
        significance: float = 0
        # distance -> DICE
        for word, edge in node.undirected_edges.items():
            # TODO is significance the same manner as distance?
            if edge.significance() > significance:
                significance = edge.significance()
                nearest_neighbor = edge.get_other_side(node)

        return nearest_neighbor
