import sys

lastKey = None

for line in sys.stdin:
    (key, value) = line.strip().split("\t")

    if lastKey and lastKey != key:
        print(lastKey)
    lastKey = key

if (lastKey):
    print(lastKey)
