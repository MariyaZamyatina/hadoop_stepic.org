import sys

H = {}

lastValue = None
categories = set()

def update(categories, H):
    for category in categories:
        if category not in H:
            H[category] = 1
        else:
            H[category] += 1

for line in sys.stdin:
    (value, category) = line.strip().split("\t")

    if lastValue and lastValue != value:
        update(categories, H)
        categories = set()
        categories.add(category)
    else:
        categories.add(category)

    lastValue = value

if (lastValue):
    update(categories, H)

for key, value in H.items():
    print("{0}\t{1}".format(key, value))