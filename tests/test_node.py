import unittest

from datastruct.node import Node


class TestNode(unittest.TestCase):
    def setUp(self):

        self.n1 = Node(5, None)
        self.n2 = Node('a', self.n1)

    def test_get_attributes(self):

        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n1.next_node, None)
        self.assertEqual(self.n2.data, 'a')
        self.assertEqual(self.n2.next_node, self.n1)

    def test_set_attributes(self):

        self.n1.data = 10
        self.n1.next_node = self.n2
        self.n2.data = 'ab'
        self.n2.next_node = None

        self.assertEqual(self.n1.data, 10)
        self.assertEqual(self.n1.next_node, self.n2)
        self.assertEqual(self.n2.data, 'ab')
        self.assertEqual(self.n2.next_node, None)

    def test_object_name_str(self):

        self.assertEqual(str(self.n1), 'Node(data=5, next_node=None)')

    def test_object_name_repr(self):

        self.assertEqual(repr(self.n1), "'Node(data=5, next_node=None)'")