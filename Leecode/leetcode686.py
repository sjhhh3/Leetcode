a = 'a'
b = 'a'
print(b.find(a))


def repeatedStringMatch(A, B):
    str = A
    i = 1
    while len(str) < 10000:
        str = A * i
        if str.find(B) == -1:
            i += 1
        else:
            return i
    return -1





print(repeatedStringMatch(a,b))