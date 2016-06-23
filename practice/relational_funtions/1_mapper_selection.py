import sys

for line in sys.stdin:
    (time, id, url) = line.strip().split("\t")
    if (id == "user10"):
        print(line.strip())