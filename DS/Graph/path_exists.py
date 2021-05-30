from graph import Graph
from DS.Stack.my_queue import Queue

def check_path(g, source, destination):
    g.print_graph()
    result = []
    queue = Queue()
    queue.enqueue(source)
    result.append(source)
    while queue.is_empty() is False:
        curr_node = queue.dequeue()
        if curr_node is destination:
            return True

        adjacent = g.array[curr_node].get_head()
        while adjacent:
            if adjacent.data not in result:
                queue.enqueue(adjacent.data)
                result.append(adjacent.data)
            adjacent = adjacent.next
    return False


g1 = Graph(9, False)
g1.add_edge(0, 1)
g1.add_edge(0, 4)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(4, 2)
g1.add_edge(4, 5)
g1.add_edge(2, 5)
g1.add_edge(5, 6)
g1.add_edge(5, 7)
g1.add_edge(5, 3)
g1.add_edge(6, 7)
g2 = Graph(4, False)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)

print('-'*30)
print('Check if path exists between two vertex')
print(f'Path exists between 0 to 6: {check_path(g1, 0, 6)}')
print(f'Path exists between 3 to 0: {check_path(g2, 3, 0)}')
