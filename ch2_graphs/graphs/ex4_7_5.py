E1 = ({'a', 'b'}, {'a', 'c'}, {'a', 'f'}, {'b', 'g'}, {'c', 'd'}, {'c', 'e'})
E2 = ({'t', 'z'}, {'u', 'v'}, {'u', 'y'}, {'u', 'z'}, {'v', 'w'}, {'v', 'x'})
E3 = ({'a', 'b'}, {'a', 'c'}, {'a', 'f'}, {'b', 'g'}, {'c', 'd'}, {'f', 'e'})
f = {
    'a': 'u',
    'b': 'z',
    'c': 'v',
    'd': 'w',
    'e': 'x',
    'f': 'y',
    'g': 't'
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
    return sorted(verts, key=lambda x: x[1], reverse=True)


E1_transformed = transform(E1, f)
print(same_edges(E1_transformed, E2))
print(degrees(f, E1))
print(degrees([f[i] for i in f], E2))
print(degrees(f, E3))
