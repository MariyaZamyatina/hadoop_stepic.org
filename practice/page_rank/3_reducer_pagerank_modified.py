import sys

emptyAdjancencyList = "{}"
alpha = 0.1
N = 5

lastNode = None
lastPageRank = 0
lastAdjacencyList = emptyAdjancencyList


def get_page_rank(pageRank):
    return 0.1 * (1.0 / N) + (1 - alpha) * pageRank


for line in sys.stdin:
    (node, pageRank, adjacencyList) = line.strip().split("\t")

    if lastNode and lastNode != node:
        print("{0}\t{1:.3f}\t{2}".format(lastNode, get_page_rank(lastPageRank), lastAdjacencyList))

        lastPageRank = 0
        lastAdjacencyList = emptyAdjancencyList

    lastNode = node

    if adjacencyList != emptyAdjancencyList:
        lastAdjacencyList = adjacencyList
    else:
        lastPageRank += float(pageRank)

if lastNode:
    print("{0}\t{1:.3f}\t{2}".format(lastNode, get_page_rank(lastPageRank), lastAdjacencyList))
