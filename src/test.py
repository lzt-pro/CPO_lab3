import unittest
from hypothesis import given
import hypothesis.strategies as st
from lazy_single_linked_list import *


class TestLazySingleLinkedList(unittest.TestCase):
    def test_head(self):
        self.assertEqual(head(Node(1, Node(2, None))), 0)
