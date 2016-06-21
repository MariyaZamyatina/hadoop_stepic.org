import sys

for line in sys.stdin:
    items = line.strip().split()

    for itemi in items:
        for itemj in items:
            if itemi != itemj:
                print("{0},{1}\t1".format(itemi, itemj))