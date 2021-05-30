from graph import Graph
from DS.Stack.my_queue import Queue

def find_min(g, source, destination):
    g.print_graph()
    result = []
    distance = [0]*g.vertices
    queue = Queue()
    queue.enqueue(source)
    result.append(source)
    while queue.is_empty() is False:
        curr_node = queue.dequeue()
        adjacent = g.array[curr_node].get_head()
        while adjacent:
            if adjacent.data not in result or adjacent.data is destination:
                queue.enqueue(adjacent.data)
                result.append(adjacent.data)
                distance[adjacent.data] = distance[curr_node] + 1
                if adjacent.data is destination:
                    return distance[adjacent.data]
            adjacent = adjacent.next
    return -1


g = Graph(7, False)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)

print(f'short path is at level : {find_min(g, 1, 6)}')
print('-'*50)
