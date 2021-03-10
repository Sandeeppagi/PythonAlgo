from graph import Graph
from Stack.my_queue import Queue
from Stack.stack import Stack

# undirected graph
g = Graph(4, True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

# directed graph
g = Graph(5, False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.print_graph()


# directed graph
g1 = Graph(4, False)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)
g1.print_graph()

print('-' * 45)


def bfs_traversal(g, source):
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
                queue.enqueue(vertex.data)
                vertex = vertex.next
        print("".join([str(i) for i in result]))
        return "".join([str(i) for i in result])


bfs_traversal(g, 0)
bfs_traversal(g1, 0)

# TODO: Refactor below method
def dsf_traversal(g, source, result, stack):
    if source < g.vertices:
        if source not in result:
            result.append(source)
        node = g.array[source].get_head()
        if node and node.data not in result:
            stack.push(source)
            dsf_traversal(g, node.data, result, stack)
        elif node and node.data in result:
            if node.next:
                dsf_traversal(g, node.next.data, result, stack)
        elif node is None:
            source = stack.pop()
            dsf_traversal(g, source, result, stack)
    return result

g2 = Graph(6, False)
g2.add_edge(0, 2)
g2.add_edge(0, 1)
g2.add_edge(1, 4)
g2.add_edge(1, 3)
g2.add_edge(2, 5)
g2.print_graph()

stack = Stack()
print(dsf_traversal(g2, 0, [], stack))
