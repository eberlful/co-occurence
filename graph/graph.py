import logging
from typing import List, Dict

from graph.edge import Edge, UndirectedEdge
from graph.node import Node


class Graph:

    def __init__(self) -> None:
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []
        self.undirected_edges: List[UndirectedEdge] = []

    def add_bigram(self, bigram: tuple):
        logging.info(f"Add bigram: {bigram}")

        # check bigram
        if len(bigram) != 2:
            raise Exception(f"The tuple is not a bigram. Tuple: {bigram}")

        source_node = self.__find_or_create_node(bigram[0])
        destination_word: str = bigram[1]
        second_edge = source_node.find_undirected_edge(destination_word)
        if second_edge:
            # TODO update weight
            logging.info(f"Strength the connection between '{source_node.word}' and '{destination_word}'")
            second_edge.strength_connection()
        else:
            logging.info(f"Destination node for word: {destination_word} not found.")
            # check if word exists in global node list
            if destination_word in self.nodes:
                logging.info(f"Destination node in global list found.")
                destination_node = self.nodes[destination_word]
            else:
                logging.info(f"Could not find destination node in global list.")
                destination_node = Node(destination_word)
                self.nodes[destination_word] = destination_node
            
            # connect the nodes
            outgoing_edge = Edge(source=source_node, destination=destination_node)
            undirected_edge = UndirectedEdge(nodes=(source_node, destination_node))
            source_node.add_edge(other_word=destination_word, edge=outgoing_edge)
            # destination_node.add_edge(destination_word=source_node.word, edge=outgoing_edge)
            source_node.add_undirected_edge(other_word=destination_word, undirected_edge=undirected_edge)
            destination_node.add_undirected_edge(other_word=source_node.word, undirected_edge=undirected_edge)

            # TODO is this needed
            self.edges.append(outgoing_edge)
            self.undirected_edges.append(undirected_edge)


    def __find_or_create_node(self, word: str) -> Node:
        if word not in self.nodes:
            logging.info(f"Could not find node for word: {word}")
            new_node = Node(word)
            self.nodes[word] = new_node
            return new_node
        return self.nodes[word]
    
    def find_highest_connection(self) -> List[tuple]:
        return [(edge.frequency, edge.source.word, edge.destination.word) for edge in sorted(self.edges, key=lambda edge: edge.frequency)[:10]]