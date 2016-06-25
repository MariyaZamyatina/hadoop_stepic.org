import sys

for line in sys.stdin:
    line = line.strip()
    (node, page_rank, adjacency_list) = line.split("\t")
    page_rank = float(page_rank)
    adjacency_list = adjacency_list[1:-1].split(",")
    rank = page_rank / len(adjacency_list)

    print(line)

    for v in adjacency_list:
        print("{0}\t{1:.3f}\t".format(v, rank) + "{}")