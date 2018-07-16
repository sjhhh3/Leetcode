A = [[1,1,0],[1,0,1],[0,0,0]]
# ans = []
#
# for list in A:
#     newlist = []
#     for num in list[::-1]:
#         newlist.append(int(not num))
#     ans.append(newlist)
#
# print(ans)
ans = []
for lists in A:
    ans.append(list(map(lambda x: int(not x), lists[::-1])))
print(ans)