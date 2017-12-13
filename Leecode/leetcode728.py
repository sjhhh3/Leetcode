left = 1
right = 22
def selfDividingNumbers(left, right):
    alist= []
    for i in range(left,right+1):
        judge = 0
        if "0" in list(str(i)):
            continue
        for num in list(str(i)):
            if i % int(num) == 0:
                judge = 1
                continue
            else:
                judge = 0
                break
        if judge:
            alist.append(i)
    return alist



selfDividingNumbers(left,right)