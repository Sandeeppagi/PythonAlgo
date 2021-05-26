from DS.LinkedList.linked_list import LinkedList
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self, vertices, is_undirected):
        self.nx = nx
        self.plt = plt
        self.directed = nx.DiGraph()
        self.undirected = nx.Graph()
        self.vertices = vertices
        self.array = []
        self.is_undirected = is_undirected
        for i in range(vertices):
            vertex = LinkedList()
            self.array.append(vertex)
            if self.is_undirected:
                self.undirected.add_node(i)
            else:
                self.directed.add_node(i)

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            if self.is_undirected:
                self.undirected.add_edge(source, destination)
            else:
                self.directed.add_edge(source, destination)

            self.array[source].insert_at_head(destination)
            if self.is_undirected:
                self.array[destination].insert_at_head(source)

    def print_graph(self):
        if self.is_undirected:
            self.nx.draw(self.undirected, with_labels=1)
        else:
            self.nx.draw(self.directed, with_labels=1)
        self.plt.show()
        print('-' * 50)
        print(f'Printing adjacency list of the {"undirected" if self.is_undirected else "directed"} graphs')
        print()
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            linklist_head = self.array[i].get_head()
            while linklist_head:
                print("[", linklist_head.data, end=" ] -> ")
                linklist_head = linklist_head.next
            print('None')

    def print_graph_ui(self):
        if self.is_undirected:
            self.nx.draw(self.undirected, with_labels=1)
        else:
            self.nx.draw(self.directed, with_labels=1)
        self.plt.show()
