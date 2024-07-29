from node import Node
from typing import List

import logging

class Cluster:

    def __init__(self) -> None:
        self.nodes: List[Node] = []

    def add_node(self, node: Node):
        self.nodes.append(node)