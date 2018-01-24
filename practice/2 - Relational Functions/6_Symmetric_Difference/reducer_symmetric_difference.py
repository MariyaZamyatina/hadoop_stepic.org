import sys

lastKey = None
lastValue = None
n = 0

for line in sys.stdin:
    (key, value) = line.strip().split("\t")

    if (lastKey is None) or (lastKey and lastKey != key):
        if n == 1:
            print(lastKey)
        n = 1

    if lastKey and lastKey == key:
        n += 1

    lastKey = key
    lastValue = value

if lastKey and n == 1:
    print(lastKey)