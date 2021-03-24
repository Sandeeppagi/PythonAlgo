from graph import Graph

def coloring_graph(g):
    g.print_graph()
    color_num_arr = [-1] * g.vertices
    available_color = [True] * g.vertices
    color_num_arr[0] = 0

    for i in range(1, g.vertices):
        node = g.array[i].get_head()
        while node:
            if color_num_arr[node.data] != -1:
                available_color[color_num_arr[node.data]] = False
            node = node.next
        for j in range(len(available_color)):
            if available_color[j]:
                color_num_arr[i] = j
                break
        available_color = [True] * g.vertices
    for u in range(g.vertices):
        print("Vertex", u, " ---> Color", color_num_arr[u])


g = Graph(5, True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)


print('-' * 50)
print('Check Cyclic graph iterative')
coloring_graph(g)
