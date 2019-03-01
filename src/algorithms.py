from graph import Graph
import numpy as np


class Algorithms:

    def __init__(self):
        pass

    def dijkstra(self, graph):
        pass

    def floyd_warshall(self, graph):
        pass

    def density(self, graph):
        return (2 * graph.edge_number / (graph.num_nodes * (graph.num_nodes - 1)))

    def has_cycles(self, graph):
        return graph.edge_number > graph.num_nodes

    def in_degree(self, graph, index):
        return np.count_nonzero(graph.edges[:, index])

    def out_degree(self, graph, index):
        return np.count_nonzero(graph.edges[index])

    def degree(self, graph, index):
        return self.in_degree(graph, index) + self.out_degree(graph, index)
