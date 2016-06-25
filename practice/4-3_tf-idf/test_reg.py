import re

#data = "1:a:"
#data = '10:Jof333hns mom went there, but he wasnt 1there. So3 she said: Where are you 33!! A a'
data = "12: !aaaa, bbb! ff 11dd:fff gg:"
(docid, data) = data.split(":", 1)
print(docid)
print(data)

res = re.split("(?:[^a-zA-Z0-9]+)", data)

if res[0] == "":
    res = res[1:]
if res[-1] == "":
    res = res[:-1]
print(res)