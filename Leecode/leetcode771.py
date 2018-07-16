J = "aAb"
S = "aaAAAbbbb"

# jdic = {}
# sdic = {}
# count = 1
# sum = 0
#
# for i in J:
#     if jdic.get(i, 0):
#         jdic[i] += 1
#     else:
#         jdic[i] = count
#
# for i in S:
#     if sdic.get(i, 0):
#         sdic[i] += 1
#     else:
#         sdic[i] = count
#
# for key in sdic.keys():
#     if key in jdic:
#         sum += sdic[key]

jewelCounter = 0

for stone in S:

    if stone in J:

        jewelCounter = jewelCounter + 1

print(jewelCounter)
