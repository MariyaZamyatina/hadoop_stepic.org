import sys

for line in sys.stdin:
    H = {}
    for word in line.strip().split(" "):
        if word and (word not in H):
            H[word] = 1
        else:
            H[word] += 1

    for key, value in H.items():
        print("{0}\t{1}".format(key, value))