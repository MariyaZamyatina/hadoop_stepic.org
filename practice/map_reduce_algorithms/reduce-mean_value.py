import sys

lastKey = None
sum = 0
count = 0

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print('{0}\t{1}'.format(lastKey, str(int(sum/count))))
        sum = int(value)
        count = 1
    else:
        sum += int(value)
        count += 1

    lastKey = key

if lastKey:
    print('{0}\t{1}'.format(lastKey, str(int(sum/count))))