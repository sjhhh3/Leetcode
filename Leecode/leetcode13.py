'''
I = 1
IV = 4
V = 5
IX = 9
X = 10
XL = 40
L = 50
XC = 90
C = 100
CD = 400
D = 500
CM = 900
M = 1000

dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dic2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
qus = 'LXXXIV'
ans = 0
for key in dic2:
    if qus.find(key) != -1:
        ans += dic2[key]
        qus = qus.replace(key, '')
a = list(qus)
for x in a:
    ans += dic[x]
print(ans)

# Problem 13
class Solution(object):
    def romanToInt(self, s):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        ans = 0
        for key in dic2:
            if s.find(key) != -1:
                ans += dic2[key]
                s = s.replace(key, '')
        a = list(s)
        for x in a:
            ans += dic[x]
        return ans

num = Solution()
print(num.romanToInt("CMLIX"))

# Sample 1
def romanToInt(s):
    tran = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    slist = list(s)
    slist.reverse()
    last_n = -1
    for c in slist:
        n = tran[c]
        if n < last_n:
            ans -= n
        else:
            ans += n
        last_n = n
    print(ans)
qus = 'CMLIX'
romanToInt(qus)
'''
# Sample 2
def romanToInt(self, s):
    values = {
        "M": 1000, "D": 500,
        "C": 100, "L": 50,
        "X": 10, "V": 5,
        "I": 1
    }
    prev = 0
    total = 0
    for val in s:
        current = values[val]
        total += (current - 2 * prev) if (current > prev) else current
        prev = current
    return total