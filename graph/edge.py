import logging

class Edge:

    def __init__(self, source, destination) -> None:
        self.source = source
        self.destination = destination
        self.frequence: int = 1

    def strength_connection(self):
        self.frequence += 1

    def significance(self) -> float:
        return 1 / self.frequence
    
class UndirectedEdge:

    def __init__(self, nodes) -> None:
        assert len(nodes) == 2
        self.nodes = nodes
        self.frequence: int = 1

    def strength_connection(self):
        self.frequence += 1

    def significance(self) -> float:
        return 1 / self.frequence 