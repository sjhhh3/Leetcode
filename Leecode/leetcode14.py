'''
{"a","a","b"} should give "" as there is nothing common in all the 3 strings.

{"a", "a"} should give "a" as a is longest common prefix in all the strings.

{"abca", "abc"} as abc

{"ac", "ac", "a", "a"} as a.

# attempt 1
qus = ['a', 'ab', 'abc']
i = 0
while i < len(qus):
    head = list(qus[i])[0]

    i += 1
    print(head)


def detect(list):
    i = 0
    while i < len(list)-1:
        if list[i] == list[i+1]:
            i += 1
        else:
            return 0
    return list[0]

# attempt 2
qus = ['abc','abedefg','abcd']
i = 0
l = 0
solution = []
#while i < len(qus)-1:
while l < (len(qus[i]) if len(qus[i])<len(qus[i+1]) else qus[i+1]):
    if qus[i][l] == qus[i+1][l]:
        solution += qus[i][l]
        l += 1
    else:
        print(0)
        break
print(solution)


# Problem 14
class Solution(object):
    def longestCommonPrefix(self, qus):
        if len(qus) == 0:
            return ''
        else:
            i = 0
            m = 0
            s = qus[i]
            while i < len(qus) - 1:
                if len(s) < len(qus[i + 1]):
                    i += 1
                else:
                    s = qus[i + 1]
                    i += 1
            while m < len(qus):
                if qus[m].find(s) == 0:
                    m += 1
                else:
                    s = s[:-1]
                    m = 0
                    continue
            return s

a = Solution()
p = a.longestCommonPrefix(["flower","flow","flight"])
print(p)
'''

# Smaple
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        #get the smallest word
        strs = sorted(strs)
        smallest = strs[0]
        #compare each char of the smallest word with every other words char at that index
        #if any of the char do not match, return smallest till this index
        for index, char in enumerate(smallest):
            for word in strs:
                if word[index] != char:
                    return smallest[:index]
        #if all chars match, return the smallest word as this is the longest common prefix
        return smallest

a = Solution()
p = a.longestCommonPrefix(["flower","flow","flight",'fla'])
print(p)