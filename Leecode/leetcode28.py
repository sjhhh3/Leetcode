a = 'I love u us'
b = 'us'


def strStr(haystack, needle):
    if haystack == needle or not needle:
        return 0
    ans = haystack.find(needle)
    return ans


print(strStr(a,b))

'''
for i in range(len(haystack) - len(needle)+1):
    if haystack[i:i+len(needle)] == needle:
        return i
return -1
'''