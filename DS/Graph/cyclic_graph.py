from graph import Graph
from Stack.stack import Stack


def is_cyclic_graph(g, source):
    g.print_graph()
    result = []
    stack = Stack()
    stack.push(source)
    while stack.is_empty() is False:
        curr_node = stack.pop()
        if curr_node in result:
            node = g.array[curr_node].get_head()
            while node:
                if node.data in result:
                    return True
                node = node.next
        else:
            result.append(curr_node)
        node = g.array[curr_node].get_head()
        while node:
            stack.push(node.data)
            node = node.next
    return False


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

print('-' * 45)
print('Check Cyclic graph iterative')
print(is_cyclic_graph(g, 0))
print(is_cyclic_graph(g1, 0))
print(is_cyclic_graph(g2, 0))
print(is_cyclic_graph(g3, 0))
