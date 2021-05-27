from graph import Graph
from DS.Stack.stack import Stack


def dsf_traversal_iterative(g, source):
    g.print_graph()
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


def dsf_traversal_recursive_alternative_path(g, curr_node, result):
    if curr_node not in result:
        result.append(curr_node)
    adjacent = g.array[curr_node].get_head()
    if adjacent and adjacent.data not in result:
        result.append(adjacent.data)
        result = dsf_traversal_recursive_alternative_path(g, adjacent.data, result)
        adjacent = adjacent.next
        if adjacent:
            result = dsf_traversal_recursive_alternative_path(g, adjacent.data, result)
    return result


def dsf_traversal_recursive(g, curr_node, result):
    if curr_node not in result:
        result.append(curr_node)
    g.array[curr_node].reverse_list()
    adjacent = g.array[curr_node].get_head()
    if adjacent and adjacent.data not in result:
        result.append(adjacent.data)
        result = dsf_traversal_recursive_alternative_path(g, adjacent.data, result)
        adjacent = adjacent.next
        if adjacent:
            result = dsf_traversal_recursive_alternative_path(g, adjacent.data, result)
    return result


def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = Stack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while stack.is_empty() is False:
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].get_head()
        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next
    return result, visited  # For the above graph it should return "12453"


def dfs_traversal(g, source):
    g.print_graph()
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
print('DSF iterative V1')
# print(dsf_traversal_iterative(g, 0))
# print(dsf_traversal_iterative(g1, 0))
# print(dsf_traversal_iterative(g2, 0))
# print(dsf_traversal_iterative(g3, 0))
# print('-' * 50)
# print('DSF iterative V2')
# print(dfs_traversal(g, 0))
# print(dfs_traversal(g1, 0))
# print(dfs_traversal(g2, 0))
# print(dfs_traversal(g3, 0))

print(dsf_traversal_iterative(g1, 0))
print(dsf_traversal_recursive_alternative_path(g1, 0, []))
print(dsf_traversal_recursive(g1, 0, []))
