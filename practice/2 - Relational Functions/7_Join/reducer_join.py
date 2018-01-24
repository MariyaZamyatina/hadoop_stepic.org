import sys

lastKey = None
H_url = list()
H_query = list()

def write_result(key):
    for query in H_query:
        for url in H_url:
            print("{0}\t{1}\t{2}".format(key, query, url))

for line in sys.stdin:
    (key, line) = line.strip().split("\t")
    (set, value) = line.split(":")

    if lastKey and lastKey != key:
        write_result(lastKey)

        H_url = list()
        H_query = list()

    if set == "query":
        H_query.append(value)
    if set == "url":
        H_url.append(value)

    lastKey = key

if lastKey:
    write_result(lastKey)
