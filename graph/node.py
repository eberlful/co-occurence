from graph.edge import Edge
from typing import Dict, Optional, List

import logging

class Node:

    def __init__(self, word: str) -> None:
        self.word = word
        self.undirected_edge: List[Edge] = []
        self.edges: Dict[str, Edge] = {}

    def get_word(self) -> str:
        return self.word
    
    def find_edge(self, destination_word: str) -> Optional[Edge]:
        if destination_word in self.edges:
            return self.edges[destination_word]
        
    def add_edge(self, destination_word: str, edge: Edge):
        self.edges[destination_word] = edge

    def degree(self) -> int:
        # TODO maybe only ingoing or outgoing
        return len(self.edges.items)
    
    # http://www.eaqua.net/doku/doku.php/signifikanz