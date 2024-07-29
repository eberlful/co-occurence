import logging

class Edge:

    def __init__(self, source, destination) -> None:
        self.source = source
        self.destination = destination
        self.frequence: int = 1

    def strength_connection(self):
        self.frequence += 1