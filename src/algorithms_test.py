from graph import Graph
from algorithms import Algorithms

import unittest
import numpy as np
import os
dirname = os.path.dirname(__file__)


class TestGraph(unittest.TestCase):

    filename = os.path.join(dirname, '../data/basic.npy')

    def setUp(self):
        matrix = np.load(self.filename)
        self.graph = Graph(matrix=matrix)
        self.algorithms = Algorithms()

    def test_density(self):
        old_density = self.algorithms.density(self.graph)
        self.graph.add_vertex()
        new_density = self.algorithms.density(self.graph)
        self.assertLess(new_density, old_density,
                        "There was an error calculating density")
        print("After adding another node, the current density (%.3f) is lower than old density (%.3f)" % (
            new_density, old_density))

    def test_degree(self):
        out_degree = self.algorithms.out_degree(self.graph, 7)
        in_degree = self.algorithms.in_degree(self.graph, 7)
        total_degree = self.algorithms.degree(self.graph, 7)
        self.assertEqual(out_degree, 3, "The out degree of 7 is not 3")
        self.assertEqual(in_degree, 2, "The in degree of 7 is not 2")
        self.assertEqual(total_degree, 5, "The total degree of 7 is not 5")


if __name__ == '__main__':
    unittest.main()
