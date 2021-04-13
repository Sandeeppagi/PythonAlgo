from graph import Graph

'''
Vertex of graph can represent Subjects
Color of graph can represent Time Slot
Edges of graph can represent dependency between 2 subjects, such that they can't share
same Time slot
'''


def coloring_graph(g):
    # g.print_graph()
    g.print_graph_ui()
    color_number_for_vertex = [-1] * g.vertices
    index_mapped_color_used = [False] * g.vertices
    color_number_for_vertex[0] = 0

    # Start with vertex number 2 / index[1]
    for i in range(1, g.vertices):
        node = g.array[i].get_head()

        # Find all adjacent color used and update index_mapped_color_used True for
        # the color used
        while node:
            if color_number_for_vertex[node.data] != -1:
                index_mapped_color_used[color_number_for_vertex[node.data]] = True
            node = node.next

        # Find the first index with value False that would be color we can use
        for j in range(len(index_mapped_color_used)):
            if not index_mapped_color_used[j]:
                color_number_for_vertex[i] = j
                break

        # Reset array for next vertex
        index_mapped_color_used = [False] * g.vertices

    # Print the colors
    for u in range(g.vertices):
        print("Vertex", u, " ---> Color", color_number_for_vertex[u])


g = Graph(5, True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print('-' * 50)
print('Color the graph')
coloring_graph(g)
