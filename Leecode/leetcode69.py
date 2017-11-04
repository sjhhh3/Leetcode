
def mySqrt(x, acr):
    """
    :type x: int
    :rtype: int
    """
    l,r = 0,x
    mid = (l+r) / 2
    while str(mid)[::-1].find('.') < acr+1:
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            r = mid
            mid = (l+r) / 2
        else:
            l = mid
            mid = (l+r) / 2
    return round(mid,3)

print(mySqrt(10,14))

# print(str(1234)[::-1].find('.'))