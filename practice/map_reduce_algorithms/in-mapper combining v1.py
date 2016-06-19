import sys

H = {}

for line in sys.stdin:
    for word in line.strip().split(" "):
        if word in H:
            H[word] += 1
        else:
            H[word] = 1

for key, value in H.iteritems():
    print("{0}\t{1}".format(key, value))