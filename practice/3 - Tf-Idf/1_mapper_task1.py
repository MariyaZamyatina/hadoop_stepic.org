import sys
import re

for line in sys.stdin:
    (docid, line) = line.strip().split(":", 1)
    words = re.split("(?:[^a-zA-Z0-9]+)", line)
    if words[0] == "": words = words[1:]
    if words[-1] == "": words = words[:-1]

    for word in words:
        print("{0}#{1}\t1".format(word, docid))