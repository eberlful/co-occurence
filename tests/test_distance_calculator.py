import unittest

from graph.node import Node
from graph.edge import Edge, UndirectedEdge
# from graph.distance_calculator import calc_dice_coefficient

class TestDistanceCalculator(unittest.TestCase):

    def test_dice(self):
        """
        tomato_edges
        (tomato, potato)
        (tomato, pizza)
        (burger, tomato)

        potato_edges
        (potato, salad)
        !!!(tomato, potato)!!!
        (potato, cabbage)
        :return:
        """
        tomato_node = Node(word="tomato")
        potato_node = Node(word="potato")
        pizza_node = Node(word="pizza")
        burger_node = Node(word="burger")
        salad_node = Node(word="salad")
        cabbage_node = Node(word="cabbage")

        tomato_potato = UndirectedEdge(nodes=(tomato_node, potato_node))
        tomato_pizza = UndirectedEdge(nodes=(tomato_node, pizza_node))
        burger_tomato = UndirectedEdge(nodes=(burger_node, tomato_node))
        potato_salad = UndirectedEdge(nodes=(potato_node, salad_node))
        potato_cabbage = UndirectedEdge(nodes=(potato_node, cabbage_node))

        tomato_node.add_undirected_edge(other_word="potato", undirected_edge=tomato_potato)
        tomato_node.add_undirected_edge(other_word="pizza", undirected_edge=tomato_pizza)
        tomato_node.add_undirected_edge(other_word="burger", undirected_edge=burger_tomato)

        potato_node.add_undirected_edge(other_word="tomato", undirected_edge=tomato_potato)
        potato_node.add_undirected_edge(other_word="salad", undirected_edge=potato_salad)
        potato_node.add_undirected_edge(other_word="cabbage", undirected_edge=potato_cabbage)

        self.assertEqual(tomato_potato.significance(), 0.5)
        # self.assertEqual(tomato_node.calc_dice_coefficient(other_word=potato_node.word, other_undirected_edges=potato_node.undirected_edges), 0.5)
        # self.assertEqual(calc_dice_coefficient(first_node=tomato_node, second_node=potato_node), 0.544545)