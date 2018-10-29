a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'


def longest(s1, s2):
    # # return ''.join(sorted(set(s1 + s2)))
    # deleterep = set(s1 + s2)  # set集合函数，去掉重复元素
    # # 输出deleterep = {'f', 'c', 'b', 'w', 'y', 'l', 'o', 'd', 'q', 'x', 'a', 'e', 'p', 'k', 'm'}
    # sortedlist = sorted(deleterep)  # 字母排序，此时输出
    # # sortedlist = ['a', 'b', 'c', 'd', 'e', 'f', 'k', 'l', 'm', 'o', 'p', 'q', 'w', 'x', 'y']
    # tostring = ''.join(sortedlist)  # list转换为string，得到结果'abcdefklmopqwxy'
    # return tostring
    #

    res = []
    for letter in s1+s2:
        if letter not in res:
            res.append(letter)
    return ''.join(sorted(res))

print(longest(a,b))

