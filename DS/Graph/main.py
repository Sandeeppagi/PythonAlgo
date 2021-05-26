from graph import Graph
from DS.Stack.my_queue import Queue
from DS.Stack.stack import Stack

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


def is_cyclic_graph(g, source):
    g.print_graph()
    result =[]
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



# TODO: Refactor below method
def dsf_traversal_recursive(g, source, result, stack):
    if source < g.vertices:
        if source not in result:
            result.append(source)
        node = g.array[source].get_head()
        if node is None:
            source = stack.pop()
            node = g.array[source].get_head()
        if node:
            if node.data not in result:
                stack.push(source)
                dsf_traversal_recursive(g, node.data, result, stack)
            elif node.data in result:
                if node.next:
                    dsf_traversal_recursive(g, node.next.data, result, stack)
    return result


def dsf_traversal_iterative(g, source):
    result = []
    my_stack = Stack()
    my_stack.push(source)
    while my_stack.is_empty() is False:
        curr_node = my_stack.pop()
        result.append(curr_node)
        node = g.array[curr_node].get_head()
        while node:
            if node.data not in result:
                my_stack.push(node.data)
            node = node.next
    return "".join([str(i) for i in result])


def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = Stack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while (stack.is_empty() is False):
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].get_head()
        while (temp is not None):
            if (visited[temp.data] is False):
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next
    return result, visited  # For the above graph it should return "12453"


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


g2 = Graph(9, False)
g2.add_edge(0, 6)
g2.add_edge(0, 2)
g2.add_edge(0, 1)
g2.add_edge(1, 4)
g2.add_edge(1, 3)
g2.add_edge(2, 5)
g2.add_edge(6, 8)
g2.add_edge(6, 7)
g2.print_graph()

stack = Stack()
print(dsf_traversal_recursive(g2, 0, [], stack))
print(dsf_traversal_iterative(g2, 0))

print(dfs_traversal(g2, 0))
bfs_traversal(g2, 0)

print('-'*45)
print(is_cyclic_graph(g, 0))
print(is_cyclic_graph(g1, 0))
print(is_cyclic_graph(g2, 0))

g4 = Graph(3, False)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 0)
print(is_cyclic_graph(g4, 0))
