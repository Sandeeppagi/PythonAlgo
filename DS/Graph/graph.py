from LinkedList.linked_list import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(vertices):
            vertex = LinkedList()
            self.array.append(vertex)

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        print('-'*50)
        print('Printing adjacency list of the directed graphs')
        print()
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            linklist_head = self.array[i].get_head()
            while linklist_head:
                print("[", linklist_head.data, end=" ] -> ")
                linklist_head = linklist_head.next
            print('None')
