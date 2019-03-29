from MyGraph import MyGraph
from Node import Node

import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.a = Node('A')
        self.b = Node('B')
        self.c = Node('C')
        self.d = Node('D')
        self.e = Node('E')
        self.a.add_neighbors([self.b, self.c, self.e])
        self.b.add_neighbors([self.a, self.c])
        self.c.add_neighbors([self.b, self.d, self.a, self.e])
        self.d.add_neighbor(self.c)
        self.e.add_neighbors([self.a, self.c])
        self.g = MyGraph()
        self.g.add_nodes([self.a, self.b, self.c, self.d, self.e])

    def test_add_neighbors(self):
        self.assertEqual(len(self.e.neighbors), 2)
        self.e.add_neighbors([self.b, self.d])
        self.assertEqual(len(self.e.neighbors), 4)

    def test_add_edge(self):
        print("\nBefore adding the new edges:\n", self.g.print_list())

        len_previous = len(self.g.nodes[self.a.name])
        self.g.add_edge(self.a, self.d)
        len_after = len(self.g.nodes[self.a.name])
        self.assertLess(len_previous, len_after)

        len_previous = len(self.g.nodes[self.d.name])
        self.g.add_edges([[self.b, self.d], [self.d, self.e]])
        len_after = len(self.g.nodes[self.d.name])
        self.assertLess(len_previous, len_after)

        print("\nAfter adding the new edges:\n", self.g.print_list())
        print(self.g.print_matrix())

    def test_remove_node(self):
        print("\nBefore removing the node:\n", self.g.print_list())

        len_previous = len(self.g.nodes)
        self.g.remove_node(self.a)
        len_after = len(self.g.nodes)
        self.assertLess(len_after, len_previous)

        print("\nAfter removing the node:\n", self.g.print_list())

    def test_remove_edge(self):
        print("\nBefore removing the edge:\n", self.g.print_list())

        len_previous = len(self.g.nodes[self.a.name])
        self.g.remove_edge([self.a, self.e])
        len_after = len(self.g.nodes[self.a.name])
        self.assertLess(len_after, len_previous)

        print("\nAfter removing the edge:\n", self.g.print_list())

    def test_dijkstra(self):

        array = self.g.dijsktra
        print(array)


if __name__ == '__main__':
    unittest.main()
