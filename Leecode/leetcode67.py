def addBinary(a, b):

    ans = int(a,2)+int(b,2)
    ans = "{0:b}".format(ans)
    return ans

print(addBinary('11','1'))