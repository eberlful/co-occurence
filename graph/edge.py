import logging
# from graph.distance_calculator import calc_dice_coefficient

class Edge:

    def __init__(self, source, destination) -> None:
        self.source = source
        self.destination = destination
        self.frequency: int = 1
        self.last_dice_coefficient: float = 0.0

    def strength_connection(self):
        self.frequency += 1

    def significance(self) -> float:
        return 1 / self.frequency


class UndirectedEdge:

    def __init__(self, nodes) -> None:
        assert len(nodes) == 2

        # TODO check if tuple is sorted alphabetically
        self.nodes = sorted(nodes, key=lambda node: node.word)
        self.frequency: int = 1
        self.last_dice_coefficient: float = 0.0

    def get_other_side(self, node):
        if node == self.nodes[0]:
            return self.nodes[1]
        elif node == self.nodes[1]:
            return self.nodes[0]
        else:
            logging.error(f"Couldn't find node {node.word} in edge.")
            raise Exception(f"Couldn't find node {node.word} in edge.")

    def strength_connection(self):
        self.frequency += 1

    def significance(self) -> float:
        self.last_dice_coefficient = calc_dice_coefficient(first_node=self.nodes[0], second_node=self.nodes[1])
        return self.last_dice_coefficient
        # return 1 / self.frequency

    # def __eq__(self, other: Edge):
    #     if not isinstance(other, Edge):
    #         return NotImplemented
    #
    #     return self.nodes[0] == other.nodes[0].word && self.nodes[1] == other.nodes[1].word

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

def __reorder_tuple(first_value: str, edge: UndirectedEdge):
    assert len(edge.nodes) == 2
    if edge.nodes[1].word == first_value:
        return (edge.nodes[1].word, edge.nodes[0].word)
    return (edge.nodes[0].word, edge.nodes[1].word)

"""
:returns [0 - 1]
Je frequenter die beiden Begriffe gemeinsam benutzt werden, um so mehr nähert sich der Wert 1. Treten beide Begriffe nur gemeinsam auf, wird die höchste Signifikanz mit 1 erreicht.
"""
def calc_dice_coefficient(first_node, second_node) -> float:
    # TODO make a difference to direct and undirected edges
    # TODO is the frequency for the calculation needed?
    # if second_node.word not in first_node.edges:
    #     return float("inf")

    first_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in first_node.undirected_edges.values()]
    second_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in second_node.undirected_edges.values()]

    intersection_bigrams = [__reorder_tuple(first_node.word, edge) for edge in list(set(first_node.undirected_edges.values()) & set(second_node.undirected_edges.values()))]
    all_bigrams = [__reorder_tuple(first_node.word, edge) for edge in {*first_node.undirected_edges.values(), *second_node.undirected_edges.values()}]
    dice_coefficient = (2 * len(intersection_bigrams)) / (len(first_node_bigrams) + len(second_node_bigrams))
    assert dice_coefficient >= 0 and dice_coefficient <= 1
    return dice_coefficient