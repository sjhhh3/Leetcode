def hasAlternatingBits(n):
    a = "{0:b}".format(n)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True


print(hasAlternatingBits(10))