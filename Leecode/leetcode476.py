num = 5
res = ''
# print(format(num, 'b'))

# for i in format(num, 'b'):
#     if i == '0':
#         res += '1'
#     else:
#         res += '0'
# print(int(res, 2))

print(int(''.join(map(str, [1 ^ int(bit) for bit in bin(num)[2:]])), 2))