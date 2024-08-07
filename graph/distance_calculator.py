# import logging
#
# from graph.node import Node
# from graph.edge import UndirectedEdge
#
# # http://www.eaqua.net/doku/doku.php/signifikanz
#
# def __reorder_tuple(first_value: str, edge: UndirectedEdge):
#     assert len(edge.nodes) == 2
#     if edge.nodes[1].word == first_value:
#         return (edge.nodes[1].word, edge.nodes[0].word)
#     return (edge.nodes[0].word, edge.nodes[1].word)
#
# """
# :returns [0 - 1]
# Je frequenter die beiden Begriffe gemeinsam benutzt werden, um so mehr nähert sich der Wert 1. Treten beide Begriffe nur gemeinsam auf, wird die höchste Signifikanz mit 1 erreicht.
# """
# def calc_dice_coefficient(first_node: Node, second_node: Node) -> float:
#     # TODO make a difference to direct and undirected edges
#     # TODO is the frequency for the calculation needed?
#     if second_node.word not in first_node.edges:
#         return float("inf")
#
#     first_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in first_node.undirected_edges.values()]
#     second_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in second_node.undirected_edges.values()]
#
#     # TODO check hash value calculation, is it possible to get to same edges
#     intersection_bigrams = [__reorder_tuple(first_node.word, edge) for edge in list(set(first_node.undirected_edges.values()) & set(second_node.undirected_edges.values()))]
#     # all_bigrams = [__reorder_tuple(first_node.word, edge) for edge in {*first_node.undirected_edges.values(), *second_node.undirected_edges.values()}]
#     dice_coefficient = (2 * len(intersection_bigrams)) / (len(first_node_bigrams) + len(second_node_bigrams))
#     assert dice_coefficient >= 0 and dice_coefficient <= 1
#     return dice_coefficient
#
# """
# :returns [0 - 1]
# """
# def calc_jaccard_coefficient(first_node: Node, second_node: Node) -> float:
#     if second_node.word not in first_node.edges:
#         return float("inf")
#
#     first_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in first_node.undirected_edges.values()]
#     second_node_bigrams = [__reorder_tuple(first_node.word, edge) for edge in second_node.undirected_edges.values()]
#
#     all_bigrams = [__reorder_tuple(first_node.word, edge) for edge in {*first_node.undirected_edges.values(), *second_node.undirected_edges.values()}]
#
#     jaccard_coefficient = (len(all_bigrams)) / (len(first_node_bigrams) + len(second_node_bigrams) - len(all_bigrams))
#     assert jaccard_coefficient >= 0 and jaccard_coefficient <= 1
#     return jaccard_coefficient