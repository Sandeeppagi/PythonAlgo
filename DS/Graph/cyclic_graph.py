from graph import Graph
from DS.Stack.stack import Stack


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


def detect_cycle(g):
    g.print_graph()
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices

    # rec_node_stack keeps track of the nodes which are part of the
    # current recursive call
    rec_node_stack = [False] * g.vertices

    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False


def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if rec_node_stack[node]:
        return True

    # It has been visited before this recursion
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True

    head_node = g.array[node].get_head()
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next
    # remove the node from the recursive call
    rec_node_stack[node] = False
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

print('-' * 50)
print('Check Cyclic graph iterative')
print(is_cyclic_graph(g, 0))
print(is_cyclic_graph(g1, 0))
print(is_cyclic_graph(g2, 0))
print(is_cyclic_graph(g3, 0))

print('-' * 50)
print('Check Cyclic graph recursive V2')
print(detect_cycle(g))
print(detect_cycle(g1))
print(detect_cycle(g2))
print(detect_cycle(g3))
