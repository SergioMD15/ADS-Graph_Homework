from collections import defaultdict
import random


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_nodes(self, list):
        for node in list:
            self.add_node(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def add_edges(self, tuples):
        for t in tuples:
            self.add_edge(t[0], t[1], t[2])

    def remove_edge(self, edge):
        if self.distances.get(edge):
            self.edges[edge[0]].remove(edge[1])
            self.edges[edge[1]].remove(edge[0])
            self.distances.pop(edge)

    def remove_edges(self, edges):
        for edge in edges:
            self.remove_edge(edge)

    def remove_node(self, node):
        for n in self.nodes:
            if(node != n):
                self.remove_edge((node, n))
        self.nodes.remove(node)

    def remove_nodes(self, nodes):
        for node in nodes:
            self.remove_node(node)
    
    def random_graph(self, num_nodes, prob_axis):
        g = Graph()
        g.add_nodes(range(1, num_nodes + 1))
        for source in g.nodes:
            for target in g.nodes:
                if (source != target and random.random() < prob_axis and (not g.distances.get((source, target)))):
                    g.add_edge(source, target, random.randint(1, num_nodes))
        return g

    def dijkstra(self, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(self.nodes)

        while nodes:
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

            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

    
