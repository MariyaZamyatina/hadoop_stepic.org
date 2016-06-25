import sys

inf_const = "INF"
empty_adjancency_list = "{}"

for line in sys.stdin:
    line = line.strip()
    (vertice, distance, adjacency_list) = line.split("\t")

    print(line)
    # вершина без информации о дочерних вершинах
    if adjacency_list != empty_adjancency_list:
        adjacency_list = adjacency_list[1:-1].split(",")
        d = inf_const if distance == inf_const else int(distance) + 1

        for v in adjacency_list:
            print("{0}\t{1}\t".format(v, d)+"{}")
