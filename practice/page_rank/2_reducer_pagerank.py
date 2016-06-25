import sys

emptyAdjancencyList = "{}"

lastNode = None
lastPageRank = 0
lastAdjacencyList = emptyAdjancencyList

for line in sys.stdin:
    (node, pageRank, adjacencyList) = line.strip().split("\t")

    if lastNode and lastNode != node:
        print("{0}\t{1:.3f}\t{2}".format(lastNode, lastPageRank, lastAdjacencyList))

        lastPageRank = 0
        lastAdjacencyList = emptyAdjancencyList

    lastNode = node

    if adjacencyList != emptyAdjancencyList:
        lastAdjacencyList = adjacencyList
    else:
        lastPageRank += float(pageRank)

if lastNode:
    print("{0}\t{1:.3f}\t{2}".format(lastNode, lastPageRank, lastAdjacencyList))