import sys

lastKey = None
lastValue = None

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey == key and lastValue != value:
        print(lastKey)

    lastKey = key
    lastValue = value