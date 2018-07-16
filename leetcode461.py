x = 1
y = 4

# ans = 0
# bx = str(bin(x))[2:]
# by = str(bin(y))[2:]
#
# bx = bx.zfill(max(len(bx),len(by)))
# by = by.zfill(max(len(bx),len(by)))
#
# i = 0
# while i < len(bx):
#     if bx[i] != by[i]:
#         ans += 1
#     i += 1
# print(ans)

d = bin(x ^ y)
print(d.count('1'))