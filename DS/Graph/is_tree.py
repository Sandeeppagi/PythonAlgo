from graph import Graph
from Stack.stack import Stack

def is_cyclic_graph(g, source, result):
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

def is_tree(g):
    g.print_graph()
    result = []
    if is_cyclic_graph(g, 0, result) is True:
        return False
    if len(result) != g.vertices:
        return False
    return True


g = Graph(5, False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)


print(is_tree(g))
