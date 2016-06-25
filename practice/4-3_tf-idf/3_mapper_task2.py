import sys

for line in sys.stdin:
    (word, doc, tf) = line.strip().split("\t")
    print("{0}\t{1};{2};1".format(word, doc, tf))