import sys

(lastKey, sum) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print('{0}\t{1}'.format(lastKey, str(sum)))
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))

if lastKey:
    print('{0}\t{1}'.format(lastKey, str(sum)))