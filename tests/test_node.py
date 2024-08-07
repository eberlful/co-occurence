import unittest

from unittest.mock import Mock, patch

from graph.node import Node
from graph.edge import Edge

class TestNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = Node(word="any-word")

    def test_should_get_word(self):
        self.assertEqual(self.sut.word, "any-word")

    def test_should_find_edge_if_exists(self):
        expected_edge = Edge(source=Mock(), destination=Mock())
        self.assertIsNone(self.sut.find_edge("test"))
        self.sut.add_edge(destination_word="test", edge=expected_edge)
        self.assertEqual(self.sut.find_edge("test"), expected_edge)

    def test_should_not_find_edge(self):
        expected_edge = Edge(source=Mock(), destination=Mock())
        self.sut.add_edge(destination_word="test", edge=expected_edge)
        self.assertIsNone(self.sut.find_edge("another-edge"))