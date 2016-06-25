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

# первая строка - число вершин и число ребер графа
(V_num, E_num) = sys.stdin.readline().strip().split()
(V_num, E_num) = (int(V_num), int(E_num))

# матрица смежности (первую строку и столбец игнорируем)
matrix = np.zeros((V_num + 1, V_num + 1))

# строки с описанием ребер: исходящая вершина, входящая вершина, вес ребра
for i in np.arange(E_num):
    (from_v, to_v, w) = sys.stdin.readline().strip().split()
    (from_v, to_v, w) = (int(from_v), int(to_v), int(w))
    matrix[from_v, to_v] = w

# последняя строка: начальная и конечная вершина, кратчайший путь между которыми нужно найти
(start_v, end_v) = sys.stdin.readline().strip().split()
(start_v, end_v) = (int(start_v), int(end_v))

# массив с кратчайшими расстояними (элемент с индексом 0 игнорируем)
d = np.ones(V_num + 1) * np.Inf
d[start_v] = 0

# какие вершины просматриваем
Q = np.array([True] * (V_num + 1))
# элемент с индексом 0 игнорируем
Q[0] = False

while Q.sum() != 0:
    u = extract_min(d, Q)
    if u == -1:
        break

    adjancency_list = get_adjacency_list(u, matrix)

    for v in adjancency_list:
        if d[v] > d[u] + matrix[u, v]:
            d[v] = d[u] + matrix[u, v]

    Q[u] = False

if d[end_v] != np.Inf:
    print(int(d[end_v]))
else:
    print(-1)