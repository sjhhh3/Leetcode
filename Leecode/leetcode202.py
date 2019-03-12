n=19
li = []
while n != 1 and n not in li:
    res = 0
    li.append(n)
    while n / 10 != 0:
        res += (n % 10) ** 2
        n = n // 10
    res += (n % 10) ** 2
    n = res
    print(res)
print(res == 1)