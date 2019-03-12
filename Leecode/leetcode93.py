def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    def helper(s, k, temp):
        if len(s) > k * 3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3, len(s) - k + 1)):
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                helper(s[i + 1:], k - 1, temp + [s[:i + 1]])

    ans = []
    helper(s, 4, [])
    print(ans)
    return ['.'.join(x) for x in ans]

print(restoreIpAddresses("25525511135"))