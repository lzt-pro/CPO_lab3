import unittest
from hypothesis import given
import hypothesis.strategies as st
from lazy_single_linked_list import *


class TestLazySingleLinkedList(unittest.TestCase):
    def test_head(self):
        List1 = Node(1, Node(2, None))
        List2 = Node(3, Node(1, Node(2, None)))

        self.assertEqual(head(List1)().value, 1)
        self.assertEqual(head(List2)(), Node(3, None))

    def test_hail(self):
        List1 = Node(1, Node(2, Node(5, None)))
        List2 = Node(3, Node(1, Node(2, None)))

        self.assertEqual(tail(List1)().value, 5)
        self.assertEqual(tail(List2)(), Node(2, None))

    def test_length(self):
        List1 = Node(1, Node(2, None))
        List2 = Node(3, List1)

        self.assertEqual(length(List1)(), length(Node('s', Node('a', None)))())
        self.assertEqual(length(List2)(), 3)

    def test_map(self):
        List1 = Node(1, Node(2, None))
        List2 = None
        self.assertEqual(map(List1, str)(), Node('1', Node('2', None)))
        self.assertEqual(map(List2, str)(), "List is None")

    def test_reduce(self):
        List1 = Node(1, Node(2, None))
        List0 = Node(-1, Node(4, None))
        List2 = None
        List3 = Node(None, None)
        self.assertEqual(reduce(List1, lambda x, y: x + y, 0)(), 3)
        self.assertEqual(reduce(List1, lambda x, y: x + y, 0)(), reduce(List0, lambda x, y: x + y, 0)())
        self.assertEqual(reduce(List2, lambda x, y: x + y, 0)(), None)
        self.assertEqual(reduce(List3, lambda x, y: x + y, 0)(), 0)

    def test_mconcat(self):
        List0 = None
        List1 = Node(1, Node(2, None))
        List2 = None
        List3 = Node(5, None)
        self.assertEqual(mconcat(List0, List2)(), None)
        self.assertEqual(mconcat(List0, List1)(), List1)
        self.assertEqual(mconcat(List3, List1)(), Node(5, Node(1, Node(2, None))))

    #
    def test_from_list(self):
        lst = [1, 2, 3, 4]
        List = Node(1, Node(2, Node(3, Node(4, None))))
        self.assertEqual(from_list(lst)(), List)
        # print(from_list(lst)())

    def test_to_list(self):
        lst = [1, 2, 3, 4]
        List = Node(1, Node(2, Node(3, Node(4, None))))
        self.assertEqual(to_list(List)(), lst)

    @given(st.lists(st.integers()))
    def test_from_list_to_List_equal(self, lst):
        self.assertEqual(to_list(from_list(lst)())(), lst)

    def test_iterator(self):
        x = [1, 2, 3]
        lst = from_list(x)()
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst)(), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())


if __name__ == '__main__':
    unittest.main()
