from functools import reduce
s = "abcd"
t = "abcde"

print(chr(reduce(lambda x, y: x ^ ord(y), s + t, 0)))