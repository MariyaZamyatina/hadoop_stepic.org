# Вычитание множества B из A
import sys

lastKey = None
lastValue = None
n = 0

for line in sys.stdin:
    (key, value) = line.strip().split("\t")

    if lastKey and lastKey != key:
        n = 1
    if lastKey and lastKey == key:
        n = 2

    if n == 1 and lastValue == "A":
        print(lastKey)

    lastKey = key
    lastValue = value

if n == 1 and lastValue == "A":
    print(lastKey)