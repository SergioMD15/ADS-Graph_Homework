import numpy as np


class Graph:

    def __init__(self, numNodes):
        self.edges = self.init_array(numNodes)
        self.num_nodes = numNodes
        self.edge_number = 0

    def add_vertex(self):
        self.edges = np.hstack((self.edges, np.zeros((self.num_nodes, 1))))
        self.edges = np.vstack((self.edges, np.zeros((1, self.num_nodes + 1))))
        self.num_nodes += 1

    def remove_vertex(self, index):
        self.edges = np.delete(self.edges, index, 0)
        self.edges = np.delete(self.edges, index, 1)
        self.num_nodes -= 1

    def add_edge(self, _from, _to, value=1):
        if(_from != _to):
            self.edges[_from][_to] = value
            self.edge_number += 1

    def remove_edge(self, _from, _to):
        self.edges[_from][_to] = 0
        self.edge_number -= 1

    def shift_rows(self, index):
        for i in range(index + 1, self.num_nodes):
            for j in range(0, self.num_nodes):
                self.edges[i][j] = self.edges[i-1][j]

    def shift_columns(self, index):
        for i in range(0, self.num_nodes):
            for j in range(index + 1, self.num_nodes):
                self.edges[i][j] = self.edges[i][j-1]

    def print(self, message):
        print('\n' + message + '\n\n')
        print(self.edges)

    def init_array(self, num_nodes):
        return np.zeros((num_nodes, num_nodes))

    def dijkstra(self, _from, _to):
        visited = self.init_array(self.num_nodes)
