# def countAndSay(n)


def countAndSay(n):
    count = 1
    init = '1'
    init += '0'
    ans = ''
    for i in range(n-1):
        for c in range(0,len(init)-1):
            if init[c] == init[c+1]:
                count += 1
                continue
            else:
                ans += str(count)+init[c]
                count = 1
        init = ans
        ans = ''
        init += '0'
    return init[:-1]

print(countAndSay(6))