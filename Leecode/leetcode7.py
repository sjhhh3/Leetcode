'''
timu = 123145
x = str(timu)
d = {}
l = list(x)
for i,num in enumerate(l):
    d[num] = len(l) - i
    newd = sorted(d.items(),key=lambda d:d[1])
b = []
for m in range(len(l)):
    ans = list(newd[m])[0]
    b += ans
a = ''.join(map(str, b))
print(b)
print(a)

#print(sorted(d.items(),key=lambda d:d[1]))

list1= ['6']
list2= ['4']
list3= ['2']
list4= ['8']
newlist = list1+list2+list3+list4
a = int(''.join(map(str, newlist)))
print (a+1)

timu = -42645712435121
if timu < 0:
    anslist = abs(timu)
else:
    anslist = timu

l = list(str(anslist))
b = ['0'] * len(l)
m = len(l)
for i,num in enumerate(l):
    b[len(l)-i-1] = num
a = ''.join(map(str, b))

if timu < 0:
    print('-' + a)
else:
    print(a)




n=0
x = 15123725
m = -1 if x < 0 else 1
x = x * m
while x > 0:
    n = (n * 10) + (x % 10)
    x = x / 10
print(n*m)

# Problem 7
class Solution(object):
    def reverse(self, x):
        m = -1 if x < 0 else 1
        x = x * m
        l = list(str(x))
        b = ['0'] * len(l)
        for i, num in enumerate(l):
            b[len(l) - i - 1] = num
        a = ''.join(map(str, b))
        ans = int(a)
        if abs(ans) > 2**31:
            return 0
        else:
            return(ans*m)

answ = Solution()
p=answ.reverse(102345678)
print(p)
'''
# Sample
class Solution(object):
    def reverse(self, x):
          if x<0:
            x_n='-'+str(abs(x))[::-1]
          else:
            x_n=str(abs(x))[::-1]
          return int(x_n) if abs(int(x_n))<2**31 else 0