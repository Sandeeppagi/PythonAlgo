from graph import Graph

def delete_edge(g, source, destination):
    g.print_graph()
    if g.vertices == 0:
        return g
    if source >= g.vertices or source < 0:
        return g
    if destination >= g.vertices or destination < 0:
        return g
    g.array[source].delete_node(destination)
    return g


g = Graph(5, False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 0)

delete_edge(g, 1, 3)
print('-'*50)
print('Graph after deletion of edge')
g.print_graph()
