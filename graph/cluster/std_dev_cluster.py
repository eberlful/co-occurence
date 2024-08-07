from typing import Dict

from graph.node import Node

class StdDevCluster:

    def __init__(self, node: Node):
        self.nodes: Dict[str, Node] = {}
        self.average_node: Node = node

    def add_node(self, new_node: Node):
        if new_node.word in self.nodes:
            return

    def __calc_average_node(self) -> Node:
