from functools import cmp_to_key


V1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
E1 = ({'a', 'b'}, {'a', 'c'}, {'a', 'f'}, {'b', 'g'}, {'c', 'd'}, {'c', 'e'})


def compare_verts(v1, v2):
    if v1[1] > v2[1]:
        return 1
    if v1[1] < v2[1]:
        return -1
    if v1[0] < v2[0]:
        return 1
    if v1[0] > v2[0]:
        return -1
    return 0


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
    return sorted(verts, key=cmp_to_key(compare_verts), reverse=True)


raw_degree_seq = degrees(V1, E1)
degree_seq_strs = [f'{d[0]}:{d[1]}' for d in raw_degree_seq]
print(', '.join(degree_seq_strs))
