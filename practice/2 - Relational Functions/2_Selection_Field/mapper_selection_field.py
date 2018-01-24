import sys

for line in sys.stdin:
    (time, id, url) = line.strip().split("\t")
    print(url)