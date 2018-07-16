S = "loveleetcode"
C = 'e'
ans = []


def plalindrome(num):
    plist = []
    for k in range(1, num+1):
        if k <= num/2:
            plist.append(k)
        else:
            plist.append(num-k+1)
    return plist

print(S.split(C))

for length in S.split(C):
    if S.startswith(length):
        ans += [i for i in range(1, len(length)+1)][::-1]
        ans.append(0)
    elif length != '' and S.endswith(length):
        ans += [i for i in range(1, len(length) + 1)]
    elif length == '':
        ans.append(0)
    else:
        ans += plalindrome(len(length))
        ans.append(0)

print(ans)

