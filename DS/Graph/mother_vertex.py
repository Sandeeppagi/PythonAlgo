from graph import Graph
from Stack.stack import Stack
from Stack.my_queue import Queue


def find_mother_vertex_helper_dfs(g, node):
    result = []
    stack = Stack()
    stack.push(node)
    while stack.is_empty() is False:
        curr_node = stack.pop()
        if curr_node not in result:
            result.append(curr_node)
        adjacent = g.array[curr_node].get_head()
        while adjacent:
            if adjacent.data not in result:
                stack.push(adjacent.data)
            adjacent = adjacent.next
    if len(result) == g.vertices:
        return node, True
    else:
        return node, False

def find_mother_vertex_helper_bfs(g, node):
    result = []
    queue = Queue()
    queue.enqueue(node)
    while queue.is_empty() is False:
        curr_node = queue.dequeue()
        if curr_node not in result:
            result.append(curr_node)
        adjacent = g.array[curr_node].get_head()
        while adjacent:
            if adjacent.data not in result:
                queue.enqueue(adjacent.data)
            adjacent = adjacent.next
    if len(result) == g.vertices:
        return node, True
    else:
        return node, False

def find_mother_vertex(g, is_dfs):
    g.print_graph()
    result = []
    for i in range(g.vertices):
        if is_dfs:
            result.append(find_mother_vertex_helper_dfs(g, i))
        else:
            result.append(find_mother_vertex_helper_bfs(g, i))
    return result


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
print('Find mother vertex dfs version')
print(find_mother_vertex(g, True))
print(find_mother_vertex(g1, True))
print(find_mother_vertex(g2, True))
print(find_mother_vertex(g3, True))

print('-' * 50)
print('Find mother vertex bfs version')
print(find_mother_vertex(g, False))
print(find_mother_vertex(g1, False))
print(find_mother_vertex(g2, False))
print(find_mother_vertex(g3, False))
