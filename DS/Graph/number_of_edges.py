from graph import Graph

def number_of_edges_v1(g):
    g.print_graph()
    edges = []
    for i in range(g.vertices):
        adjacent = g.array[i].get_head()
        while adjacent:
            edge1 = str(i) + ' <=> ' + str(adjacent.data)
            edge2 = str(adjacent.data) + ' <=> ' + str(i)
            if not (edge1 in edges or edge2 in edges):
                edges.append(edge1)
            adjacent = adjacent.next
    print(edges)
    return len(edges)

def number_of_edges_v2(g):
    g.print_graph()
    sum = 0
    for i in range(g.vertices):
        adjacent = g.array[i].get_head()
        while adjacent:
            sum += 1
            adjacent = adjacent.next
    return sum//2

def number_of_edges_v3(g):
    g.print_graph()
    return sum([g.array[i].length() for i in range(g.vertices)])//2

# undirected graph
g = Graph(5, True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# directed graph
g1 = Graph(4, True)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)

g2 = Graph(9, True)
g2.add_edge(0, 6)
g2.add_edge(0, 2)
g2.add_edge(0, 1)
g2.add_edge(1, 4)
g2.add_edge(1, 3)
g2.add_edge(2, 5)
g2.add_edge(6, 8)
g2.add_edge(6, 7)

# Cyclic graph
g3 = Graph(3, True)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)

g4 = Graph(4, True)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(3, 0)
g4.add_edge(3, 1)

g5 = Graph(8, True)
g5.add_edge(0, 1)
g5.add_edge(0, 4)
g5.add_edge(1, 2)
g5.add_edge(1, 3)
g5.add_edge(4, 2)
g5.add_edge(4, 5)
g5.add_edge(2, 5)
g5.add_edge(5, 6)
g5.add_edge(5, 7)
g5.add_edge(5, 3)
g5.add_edge(6, 7)

print('-' * 50)
print('Number of edges in undirected graph')
print(f'Number unique edges {number_of_edges_v1(g)}')
print(f'Number unique edges {number_of_edges_v1(g1)}')
print(f'Number unique edges {number_of_edges_v1(g2)}')
print(f'Number unique edges {number_of_edges_v1(g3)}')
print(f'Number unique edges {number_of_edges_v1(g4)}')
print(f'Number unique edges {number_of_edges_v1(g5)}')

print('-' * 50)
print('Number of edges in undirected graph')
print(f'Number unique edges {number_of_edges_v2(g)}')
print(f'Number unique edges {number_of_edges_v2(g1)}')
print(f'Number unique edges {number_of_edges_v2(g2)}')
print(f'Number unique edges {number_of_edges_v2(g3)}')
print(f'Number unique edges {number_of_edges_v2(g4)}')
print(f'Number unique edges {number_of_edges_v2(g5)}')

print('-' * 50)
print('Number of edges in undirected graph')
print(f'Number unique edges {number_of_edges_v3(g)}')
print(f'Number unique edges {number_of_edges_v3(g1)}')
print(f'Number unique edges {number_of_edges_v3(g2)}')
print(f'Number unique edges {number_of_edges_v3(g3)}')
print(f'Number unique edges {number_of_edges_v3(g4)}')
print(f'Number unique edges {number_of_edges_v3(g5)}')
