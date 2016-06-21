import sys

for line in sys.stdin:
    items = line.strip().split()

    for itemi in items:
        H = {}
        for itemj in items:
            if itemi != itemj:
                if itemj not in H:
                    H[itemj] = 1
                else:
                    H[itemj] += 1

        print("{0}\t{1}".format(itemi, "".join((key + ":" + str(value) + "," for (key, value) in H.items()))[:-1]))
