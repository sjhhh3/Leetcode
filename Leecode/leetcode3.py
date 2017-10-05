a = "abcbbbbb"
b = "bbbbb"
c = "pwwkew"


def lengthOfLongestSubstring(s):

    max = 0
    for i in range(0,len(s)):
        count = 0
        for n in range(i+1, len(s)-1):
            if s[i] == s[n]:
                break
            else:
                count += 1
                continue
        if max < count:
            max = count
    return max



print(lengthOfLongestSubstring(a))