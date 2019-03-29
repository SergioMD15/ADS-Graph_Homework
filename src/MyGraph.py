import numpy as np
from Node import Node


class MyGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if isinstance(node, Node):
            self.nodes[node.name] = node.neighbors

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def remove_node(self, node):
        if isinstance(node, Node):
            self.nodes.pop(node.name)

    def remove_nodes(self, nodes):
        for node in nodes:
            self.remove_node(node)

    def add_edge(self, start_node, end_node):
        if isinstance(start_node, Node) and isinstance(end_node, Node):
            start_node.add_neighbor(end_node)
            if isinstance(start_node, Node) and isinstance(end_node, Node):
                self.nodes[start_node.name] = start_node.neighbors
                self.nodes[end_node.name] = end_node.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def remove_edge(self, edge):
        self.nodes[edge[0].name].remove(edge[1].name)
        self.nodes[edge[1].name].remove(edge[0].name)

    def remove_edges(self, edges):
        for edge in edges:
            self.remove_edge(edge)

    def adjacency_list(self):
        if len(self.nodes) >= 1:
            return [str(key) + ":" + str(self.nodes[key]) for key in self.nodes.keys()]
        else:
            return dict()

    def adjacency_matrix(self):
        if len(self.nodes) >= 1:
            node_names = sorted(self.nodes.keys())
            node_indices = dict(
                zip(node_names, range(len(node_names))))
            self.adjacency_matrix = np.zeros(
                shape=(len(self.nodes), len(self.nodes)))
            for i in range(len(node_names)):
                for j in range(i, len(self.nodes)):
                    for el in self.nodes[node_names[i]]:
                        j = node_indices[el]
                        self.adjacency_matrix[i, j] = 1
            return self.adjacency_matrix
        else:
            return dict()

    def dijsktra(self, graph, initial):
        visited = {}
        visited[initial] = 0
        path = {}
        nodes = self.nodes

        while len(nodes) > 0:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in nodes[min_node.name]:
                weight = current_weight + graph.distance[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

    def floyd_warshall(self, graph):
        pass

    def print(self):
        return str(self.adjacency_list()) + '\n' + '\n' + str(self.adjacency_matrix())

    def print_list(self):
        return str(self.adjacency_list()) + '\n'

    def print_matrix(self):
        return str(self.adjacency_matrix()) + '\n'

###################################################################################
