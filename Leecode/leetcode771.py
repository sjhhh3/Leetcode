J = "aAb"
S = "aaAAAbbbb"

jewelCounter = 0

for stone in S:

    if stone in J:

        jewelCounter = jewelCounter + 1

print(jewelCounter)


sum = 0
for jewel in J:
    sum += S.count(jewel)
print(sum)


print(sum(S.count(i) for i in J))

print("AABBCCD".count("A"))