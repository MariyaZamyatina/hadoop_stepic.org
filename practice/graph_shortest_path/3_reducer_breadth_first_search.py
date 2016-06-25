import sys

inf_const = "INF"
empty_adjancency_list = "{}"

lastVertice = None
last_min_distance = float('inf')
last_adjacency_list = empty_adjancency_list

for line in sys.stdin:
    line = line.strip()
    (vertice, distance, adjacency_list) = line.split("\t")

    if lastVertice and lastVertice != vertice:
        print("{0}\t{1}\t{2}".format(
            lastVertice,
            last_min_distance if last_min_distance != float('inf') else inf_const,
            last_adjacency_list))

        last_min_distance = float('inf')
        last_adjacency_list = empty_adjancency_list

    lastVertice = vertice

    if distance != inf_const and int(distance) < last_min_distance:
        last_min_distance = int(distance)

    if adjacency_list != empty_adjancency_list:
        last_adjacency_list = adjacency_list

if lastVertice:
    print("{0}\t{1}\t{2}".format(
        lastVertice,
        last_min_distance if last_min_distance != float('inf') else inf_const,
        last_adjacency_list))