import sys

lastWord = None
lastDoc = None
n = 0

for line in sys.stdin:
    (word, num) = line.strip().split("\t")
    (word, doc) = word.split("#")

    if lastWord and (lastWord != word or lastDoc != doc):
        print("{0}\t{1}\t{2}".format(lastWord, lastDoc, n))
        n = 1
    else:
        n += 1

    lastWord = word
    lastDoc = doc

if lastWord:
    print("{0}\t{1}\t{2}".format(lastWord, lastDoc, n))