import sys

lastPair = None

for line in sys.stdin:
    (pair, count) = line.strip().split("\t")
    if lastPair and lastPair != pair:
        print(lastPair)
    lastPair = pair

if (lastPair):
    print(lastPair)