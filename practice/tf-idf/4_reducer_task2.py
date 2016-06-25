import sys

lastWord = None
docs = list()


def print_result(word, docs):
    docs_len = len(docs)
    for doc in docs:
        print("{0}#{1}\t{2}\t{3}".format(word, doc[0], doc[1], docs_len))

for line in sys.stdin:
    (word, line) = line.strip().split("\t")
    (doc, tf, num) = line.split(";")

    if lastWord and lastWord != word:
        print_result(lastWord, docs)
        docs.clear()

    docs.append((doc, tf))
    lastWord = word

if lastWord and len(docs) != 0:
    print_result(lastWord, docs)
