from graph import Graph

import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(8)
        self.create_edges()

    def create_edges(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(0, 6)

        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 7)

        self.graph.add_edge(2, 1)
        self.graph.add_edge(2, 0)
        self.graph.add_edge(2, 6)

        self.graph.add_edge(3, 1)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(3, 6)

        self.graph.add_edge(4, 1)
        self.graph.add_edge(4, 2)
        self.graph.add_edge(4, 5)

        self.graph.add_edge(5, 0)
        self.graph.add_edge(5, 3)
        self.graph.add_edge(5, 7)

        self.graph.add_edge(6, 2)
        self.graph.add_edge(6, 3)
        self.graph.add_edge(6, 5)

        self.graph.add_edge(7, 0)
        self.graph.add_edge(7, 1)
        self.graph.add_edge(7, 4)

    def test_add_vertex(self):
        old_num_nodes = self.graph.num_nodes
        self.graph.add_vertex()
        self.assertGreater(self.graph.num_nodes, old_num_nodes,
                           "Current number of vertices should be greater than before")
        self.graph.print('New vertex:')
        

    def test_remove_vertex(self):
        old_num_nodes = self.graph.num_nodes
        self.graph.remove_vertex(4)
        self.assertLess(self.graph.num_nodes, old_num_nodes,
                           "Current number of vertices should be less than before")
        self.graph.print('After removing vertex 4:')

    def test_add_edge(self):
        old_num_edges = self.graph.edge_number
        self.graph.add_edge(4, 3)
        self.assertGreater(self.graph.edge_number, old_num_edges,
                           "Current number of edges should be greater than before")
        self.graph.print('After adding an edge from vertex 4 to vertex 3:')

    def test_remove_edge(self):
        old_num_edges = self.graph.edge_number
        self.graph.remove_edge(4, 5)
        self.assertLess(self.graph.edge_number, old_num_edges,
                           "Current number of nodes should be less than before")
        self.graph.print('After adding an edge from vertex 4 to vertex 5:')


if __name__ == '__main__':
    unittest.main()
