S = "loveleetcod"
C = 'e'
ind = []
res = []
count = 0

for i in S:
    if i == C and count != 0:
        ind.append(count)
        ind.append(0)
        count = 0
    elif i == C:
        ind.append(count)
        count = 0
    else:
        count += 1
ind.append(count)
# print(ind)


def mid(length):
    lis = []
    for num in range(1, length+1):
        if num <= length//2:
            lis.append(num)
        else:
            lis.append(length-num+1)
    return [0] if length == 0 else lis

if ind[0] == 0:
    res.append(0)
Lstart = [i for i in range(ind[0], 0, -1)]
Lend = [i for i in range(1, ind[-1]+1)]

res.extend(Lstart)
for lent in ind[1:-1]:
    res.extend(mid(lent))
    # print(mid(lent))
res.extend(Lend)

# print(res)
