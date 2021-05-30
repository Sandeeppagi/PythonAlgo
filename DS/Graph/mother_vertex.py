from graph import Graph
from DS.Stack.stack import Stack
from DS.Stack.my_queue import Queue


def find_mother_vertex_recursive(g):
    g.print_graph()
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False] * g.vertices

    # To store last finished vertex (or mother vertex)
    last_v = 0

    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if visited[i] is False:
            perform_DFS(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False] * g.vertices
    perform_DFS(g, last_v, visited)
    if any(i is False for i in visited):
        return -1
    else:
        return last_v


# A recursive function to print DFS starting from v
def perform_DFS(g, node, visited):

    # Mark the current node as visited and print it
    visited[node] = True

    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].get_head()
    while temp:
        if visited[temp.data] is False:
            perform_DFS(g, temp.data, visited)
        temp = temp.next


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

g4 = Graph(4, False)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(3, 0)
g4.add_edge(3, 1)

print('-' * 50)
print('Find mother vertex dfs version')
print(find_mother_vertex(g, True))
print(find_mother_vertex(g1, True))
print(find_mother_vertex(g2, True))
print(find_mother_vertex(g3, True))
print(find_mother_vertex(g4, True))

print('-' * 50)
print('Find mother vertex bfs version')
print(find_mother_vertex(g, False))
print(find_mother_vertex(g1, False))
print(find_mother_vertex(g2, False))
print(find_mother_vertex(g3, False))
print(find_mother_vertex(g4, False))

print('-' * 50)
print('Find mother vertex dfs recursive')
print(find_mother_vertex_recursive(g))
print(find_mother_vertex_recursive(g1))
print(find_mother_vertex_recursive(g2))
print(find_mother_vertex_recursive(g3))
print(find_mother_vertex_recursive(g4))
