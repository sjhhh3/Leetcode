li = [[1,-3], [1,2], [3,4]]

def check(li):
    li.sort(key=lambda c: c[0] ** 2 + c[1] ** 2)
    return li

print(check(li))