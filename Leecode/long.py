def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    def findlong(string, left, right):

        while left >= 0 and right < len(string) and string[left] == string[right]:

            left -= 1
            right += 1

        return string[left + 1:right]

    ans = ""
    for i in range(len(s)):

        ans = max(ans, findlong(s, i, i), key=len)
        ans = max(ans, findlong(s, i, i + 1), key=len)

    return ans


print(longestPalindrome("babad"))