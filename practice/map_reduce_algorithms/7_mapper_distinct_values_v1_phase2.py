import sys

for line in sys.stdin:
    (value, group) = line.strip().split(",")
    print("{0}\t1".format(group))