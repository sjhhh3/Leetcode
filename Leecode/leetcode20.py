s = '()'
# cur = 0
# for c in s:
#     cur = ord(c)
#
#     print(cur)
'''
def Solution(s):
    c = 0
    if len(s)<2:
        return False
    while c in range(len(s)-1):
        if ord(s[c])+ord(s[c+1]) in (248, 184, 81) and s[c]<s[c+1] and len(s)%2 == 0:
            c += 2
            continue
        else:
            return False

    return True
print(Solution(s))
'''
# a = ['(',')']
# b = ['[',']']
# c = ['{','}']
SYMBOLS = {'}':'{', ']':'[', ')':'('}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return not arr

print(check(s))
