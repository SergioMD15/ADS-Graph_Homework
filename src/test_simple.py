from Graph import Graph

import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Graph()
        self.g.add_nodes(['a', 'b', 'c', 'd'])
        self.g.add_edges([('a', 'b', 3), ('a', 'd', 2),
                          ('c', 'b', 1), ('c', 'd', 4)])

    def test_add_edge(self):
        print("\nTest Add Edge: Before adding the new edges:\n", self.g.print_edges())

        len_previous = len(self.g.edges['a'])
        self.g.add_edge('a', 'c', 2)
        self.assertLess(len_previous, len(self.g.edges['a']))

        print("\nTest Add Edge: After adding the new edges:\n", self.g.print_edges())

    def test_remove_node(self):
        print("\nTest Remove Node: Before removing the node:\n", self.g.print_edges())

        len_previous = len(self.g.nodes)
        self.g.remove_node('a')
        self.assertLess(len(self.g.nodes), len_previous)

        print("\nTest Remove Node: After removing the node:\n", self.g.print_edges())

    def test_remove_edge(self):
        print("\nTest Remove Edge: Before removing the edge:\n", self.g.print_edges())

        len_previous = len(self.g.edges['a'])
        self.g.remove_edge(('a', 'd'))
        self.assertLess(len(self.g.edges['a']), len_previous)

        print("\nTest Remove Edge: After removing the edge:\n", self.g.print_edges())

    def test_dijkstra(self):
        (visited, path) = self.g.dijsktra('a')
        print("\nDijkstra path:\n", path)
        print("\nDijkstra visited:\n", visited)


if __name__ == '__main__':
    unittest.main()
