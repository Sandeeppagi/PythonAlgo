from LinkedList.linked_list import LinkedList


class Graph:
    def __init__(self, vertices, is_undirected):
        self.vertices = vertices
        self.array = []
        self.is_undirected = is_undirected
        for i in range(vertices):
            vertex = LinkedList()
            self.array.append(vertex)

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)
            if self.is_undirected:
                self.array[destination].insert_at_head(source)

    def print_graph(self):
        print('-'*50)
        print(f'Printing adjacency list of the {"undirected" if self.is_undirected else "directed"} graphs')
        print()
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            linklist_head = self.array[i].get_head()
            while linklist_head:
                print("[", linklist_head.data, end=" ] -> ")
                linklist_head = linklist_head.next
            print('None')
