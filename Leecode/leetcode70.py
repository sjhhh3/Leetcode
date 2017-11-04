def climbStairs(n):

    def counter(t,p):
        sum, sum2 = 1, 1
        for it in range(0,p):
            sum *= (t-it)
            # print(sum)
        for ip in range(1,p+1):
            sum2 *= ip
            # print(sum2)
        return int(sum/sum2)

    twos, count = 1, 0
    while twos < n//2+1:
        ones = n - 2*twos
        count += counter(ones+twos,twos)
        twos += 1
    return 1+count

print(climbStairs(5))

'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1

        res = (1,1)
        i = 2
        while i < n+1:
            res = (res[1],res[1]+res[0])
            i += 1

        return res[-1]
'''