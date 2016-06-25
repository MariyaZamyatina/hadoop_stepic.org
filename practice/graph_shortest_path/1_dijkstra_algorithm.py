import sys

V = set()
E = list()

line = sys.stdin;
(V_num, E_num) = line.strip().split()

for i in range(E_num):
    (from_v, to_v, w) = sys.stdin.strip().split()

    V.add(from_v, to_v)
    E.append((from_v, to_v, ))

