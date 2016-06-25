import sys
import numpy as np

def extract_min(d, valid):
    min_index = -1
    min_d = np.Inf
    for i in np.arange(1, V_num + 1):
        if valid[i] and d[i] < min_d:
            min_d = d[i]
            min_index = i

    return min_index

def get_adjacency_list(v, matrix):
    adjacency_list = list()
    for i in np.arange(1, matrix.shape[0]):
        if matrix[v, i] != 0:
            adjacency_list.append(i)

    return adjacency_list

(V_num, E_num) = sys.stdin.readline().strip().split()
(V_num, E_num) = (int(V_num), int(E_num))

matrix = np.zeros((V_num+1, V_num+1))

for i in np.arange(E_num):
    (from_v, to_v, w) = sys.stdin.readline().strip().split()
    (from_v, to_v, w) = (int(from_v), int(to_v), int(w))
    matrix[from_v, to_v] = w

print(matrix)
(start_v, end_v) = sys.stdin.readline().strip().split()
(start_v, end_v) = (int(start_v), int(end_v))

d = np.ones(V_num + 1) * np.Inf
d[start_v] = 0

# какие вершины просматриваем
valid = np.array([True] * (V_num + 1))
valid[0] = False

while valid.sum() != 0:
    u = extract_min(d, valid) #index of min

    adjancency_list = get_adjacency_list(u, matrix)

    for v in adjancency_list:
        if d[v] > d[u] + matrix[u, v]:
            d[v] = d[u] + matrix[u, v]

    valid[u] = False

print(d)
print(d[end_v])