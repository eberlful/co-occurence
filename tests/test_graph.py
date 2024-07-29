import unittest

from unittest.mock import Mock, patch

from co_occurence.graph import Graph

class TestGraph(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sut = Graph()
    
    def test_graph(self):
        GRAPH = TestGraph.sut
        self.assertDictEqual(GRAPH.nodes, {})

        GRAPH.add_bigram(("table", "chair"))
        GRAPH.add_bigram(("table", "knife"))
        GRAPH.add_bigram(("table", "shelf"))
        GRAPH.add_bigram(("knife", "chair"))
        GRAPH.add_bigram(("knife", "weapon"))
        GRAPH.add_bigram(("knife", "weapon"))

        expected_nodes = ["table", "chair", "shelf", "knife", "weapon"]

        [self.assertIn(expected_node, GRAPH.nodes) for expected_node in expected_nodes]

        [self.assertEqual(expected_node, GRAPH.nodes[expected_node].word) for expected_node in expected_nodes]

        table_edges = GRAPH.nodes["table"].edges
        self.assertEqual(3, len(table_edges))
        self.assertIn("chair", table_edges)
        self.assertEqual(1, table_edges["chair"].frequence)
        self.assertIn("knife", table_edges)
        self.assertEqual(1, table_edges["knife"].frequence)
        self.assertIn("shelf", table_edges)
        self.assertEqual(1, table_edges["shelf"].frequence)

        chair_edges = GRAPH.nodes["chair"].edges
        self.assertEqual(2, len(chair_edges))
        self.assertIn("table", chair_edges)
        self.assertEqual(1, chair_edges["table"].frequence)
        self.assertIn("knife", chair_edges)
        self.assertEqual(1, chair_edges["knife"].frequence)

        shelf_edges = GRAPH.nodes["shelf"].edges
        self.assertEqual(1, len(shelf_edges))
        self.assertIn("table", shelf_edges)
        self.assertEqual(1, shelf_edges["table"].frequence)

        knife_edges = GRAPH.nodes["knife"].edges
        self.assertEqual(3, len(knife_edges))
        self.assertIn("table", knife_edges)
        self.assertEqual(1, knife_edges["table"].frequence)
        self.assertIn("chair", knife_edges)
        self.assertEqual(1, knife_edges["chair"].frequence)
        self.assertIn("weapon", knife_edges)
        self.assertEqual(2, knife_edges["weapon"].frequence)

        weapon_edges = GRAPH.nodes["weapon"].edges
        self.assertEqual(1, len(weapon_edges))
        self.assertIn("knife", weapon_edges)
        self.assertEqual(2, weapon_edges["knife"].frequence)

        self.assertEqual(knife_edges["weapon"], weapon_edges["knife"])

        self.assertEqual(len(expected_nodes), len(GRAPH.nodes))
        self.assertEqual(5, len(GRAPH.edges))