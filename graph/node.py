from graph.edge import Edge, UndirectedEdge
from typing import Dict, Optional, List

import logging

class Node:

    def __init__(self, word: str) -> None:
        self.word = word
        self.undirected_edges: Dict[str, UndirectedEdge] = {}
        # self.edges: Dict[str, Edge] = {}
        self.ingoing_edges: Dict[str, Edge] = {}
        self.outgoing_edges: Dict[str, Edge] = {}

    
    def find_ingoing_edge(self, source_word: str) -> Optional[Edge]:
        if source_word in self.ingoing_edges:
            return self.ingoing_edges[source_word]

    def find_outgoing_edge(self, destination_word: str) -> Optional[Edge]:
        if destination_word in self.outgoing_edges:
            return self.outgoing_edges[destination_word]

    def find_undirected_edge(self, destination_word: str) -> Optional[UndirectedEdge]:
        if destination_word in self.undirected_edges:
            return self.undirected_edges[destination_word]

    def add_edge(self, other_word: str, edge: Edge):
        if edge.source.word == self.word:
            # todo check if node already there
            if other_word not in self.outgoing_edges:
                self.outgoing_edges[other_word] = edge
            else:
                logging.error(f"Edge for word {other_word} is already there.")
                raise Exception(f"Edge for word {other_word} is already there.")
        elif edge.destination.word == self.word:
            if other_word not in self.ingoing_edges:
                self.ingoing_edges[other_word] = edge
            else:
                logging.error(f"Edge for word {other_word} is already there.")
                raise Exception(f"Edge for word {other_word} is already there.")
        else:
            logging.error(f"Edge ({edge.source.word} -> {edge.destination.word}) is not connected to node {self.word}.")
            raise Exception()

        # self.edges[destination_word] = edge

    def add_undirected_edge(self, other_word: str, undirected_edge: UndirectedEdge):
        if other_word not in self.undirected_edges:
            self.undirected_edges[other_word] = undirected_edge
        else:
            logging.error(f"UndirectedEdge for word {other_word} is already there.")
            raise Exception(f"UndirectedEdge for word {other_word} is already there.")

    def degree(self) -> int:
        # TODO maybe only ingoing or outgoing
        return len(self.undirected_edges.values())

    # def __eq__(self, other):
    #     if not isinstance(other, Node):
    #         return NotImplemented
    #
    #     return self.word ==


    # http://www.eaqua.net/doku/doku.php/signifikanz

    # @staticmethod
    # def calc_dice_coefficient(self, other_node: Node) -> float:
    #     # TODO make a difference to direct and undirected edges
    #
    #     pass

    # def __reorder_tuple(self, edge: UndirectedEdge):
    #     assert len(edge.nodes) == 2
    #     if edge.nodes[1].word == self.word:
    #         return edge.nodes[1].word, edge.nodes[0].word
    #     return edge.nodes[0].word, edge.nodes[1].word
    #
    # """
    # :returns [0 - 1]
    # Je frequenter die beiden Begriffe gemeinsam benutzt werden, um so mehr nähert sich der Wert 1. Treten beide Begriffe nur gemeinsam auf, wird die höchste Signifikanz mit 1 erreicht.
    # """
    # # def calc_dice_coefficient(self, first_node: Node, second_node: Node) -> float:
    # def calc_dice_coefficient(self, other_word: str, other_undirected_edges: Dict[str, UndirectedEdge]) -> float:
    #     # TODO make a difference to direct and undirected edges
    #     # TODO is the frequency for the calculation needed?
    #     if other_word not in self.undirected_edges:
    #         return float("inf")
    #
    #     first_node_bigrams = [self.__reorder_tuple(edge) for edge in self.undirected_edges.values()]
    #     second_node_bigrams = [self.__reorder_tuple(edge) for edge in other_undirected_edges.values()]
    #
    #     all_bigrams = [self.__reorder_tuple(edge) for edge in {*self.undirected_edges.values(), *other_undirected_edges.values()}]
    #     dice_coefficient = (2 * len(all_bigrams)) / (len(first_node_bigrams) + len(second_node_bigrams))
    #     assert 0 <= dice_coefficient <= 1
    #     return dice_coefficient
    #
    # """
    # :returns [0 - 1]
    # """
    # def calc_jaccard_coefficient(self, first_node, second_node) -> float:
    #     if second_node.word not in first_node.edges:
    #         return float("inf")
    #
    #     first_node_bigrams = [self.__reorder_tuple(first_node.word, edge) for edge in first_node.undirected_edges.values()]
    #     second_node_bigrams = [self.__reorder_tuple(first_node.word, edge) for edge in second_node.undirected_edges.values()]
    #
    #     all_bigrams = [self.__reorder_tuple(first_node.word, edge) for edge in {*first_node.undirected_edges.values(), *second_node.undirected_edges.values()}]
    #
    #     jaccard_coefficient = (len(all_bigrams)) / (len(first_node_bigrams) + len(second_node_bigrams) - len(all_bigrams))
    #     assert jaccard_coefficient >= 0 and jaccard_coefficient <= 1
    #     return jaccard_coefficient