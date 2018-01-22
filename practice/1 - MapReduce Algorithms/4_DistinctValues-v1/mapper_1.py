import sys

for line in sys.stdin:
    (key, values) = line.strip().split("\t")
    values = values.split(",")

    for value in values:
        print("{0},{1}\t1".format(key, value))