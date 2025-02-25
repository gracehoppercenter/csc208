E1 = ({'a', 'b'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'b', 'e'}, {'b', 'f'},
      {'c', 'g'}, {'d', 'e'}, {'e', 'f'}, {'f', 'g'})
E2 = ({'v1', 'v4'}, {'v1', 'v5'}, {'v1', 'v7'}, {'v2', 'v3'}, {'v2', 'v6'},
      {'v3', 'v5'}, {'v3', 'v7'}, {'v4', 'v5'}, {'v5', 'v6'}, {'v5', 'v7'})
f = {
    'a': 'v4',
    'b': 'v5',
    'c': 'v1',
    'd': 'v6',
    'e': 'v2',
    'f': 'v3',
    'g': 'v7'
}
f2 = {
    'a': 'v4',
    'b': 'v5',
    'c': 'v6',
    'd': 'v1',
    'e': 'v7',
    'f': 'v3',
    'g': 'v2'
}


def map_edge(edge, f):
    e = set()
    for vertex in edge:
        e.add(f[vertex])
    return e


def transform(edges, f):
    PE2 = []
    for edge in edges:
        PE2.append(map_edge(edge, f))
    return PE2


def same_edges(e1, e2):
    if len(e1) != len(e2):
        return False
    for edge in e1:
        if edge not in e2:
            print(f'{edge} from e1 not in e2')
            return False
    return True 


def degree(vertex, edges):
    d = 0
    for edge in edges:
        if vertex in edge:
            d += 1
    return d


def degrees(f, E1):
    verts = []
    for v in f:
        verts.append((v, degree(v, E1)))
    return sorted(verts, key=lambda x: x[1])


E1_transformed = transform(E1, f)
print(same_edges(E1_transformed, E2))
E1_transformed = transform(E1, f2)
print(same_edges(E1_transformed, E2))
print(degrees(f2, E1))
print(degrees([f2[i] for i in f2], E2))
