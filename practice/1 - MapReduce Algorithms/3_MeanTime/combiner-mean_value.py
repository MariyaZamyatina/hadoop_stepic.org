import sys

lastKey = None
sum = 0
count = 0

for line in sys.stdin:
    (key, value_sum, value_count) = line.strip().replace(";", "\t").split("\t")
    if lastKey and lastKey != key:
        print("{0}\t{1};{2}".format(lastKey, int(sum), count))
        sum = float(value_sum)
        count = int(value_count)
    else:
        sum += float(value_sum)
        count += int(value_count)

    lastKey = key

if lastKey:
    print("{0}\t{1};{2}".format(lastKey, int(sum), count))