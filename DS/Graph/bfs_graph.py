from graph import Graph
from Stack.my_queue import Queue

def bfs_traversal(g, source):
    g.print_graph()
    result = []
    queue = Queue()
    if source < g.vertices:
        queue.enqueue(source)
        while queue.size() > 0:
            idx = queue.dequeue()
            if idx not in result:
                result.append(idx)
            vertex = g.array[idx].get_head()
            while vertex:
                if vertex.data not in result:
                    queue.enqueue(vertex.data)
                vertex = vertex.next
        return "".join([str(i) for i in result])

# directed graph
g = Graph(5, False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# directed graph
g1 = Graph(4, False)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)

g2 = Graph(9, False)
g2.add_edge(0, 6)
g2.add_edge(0, 2)
g2.add_edge(0, 1)
g2.add_edge(1, 4)
g2.add_edge(1, 3)
g2.add_edge(2, 5)
g2.add_edge(6, 8)
g2.add_edge(6, 7)

# Cyclic graph
g3 = Graph(3, False)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)

print('-' * 50)
print('BSF iterative')
print(bfs_traversal(g, 0))
print(bfs_traversal(g1, 0))
print(bfs_traversal(g2, 0))
print(bfs_traversal(g3, 0))
