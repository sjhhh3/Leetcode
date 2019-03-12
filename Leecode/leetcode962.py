A = [6,0,8,2,1,5]


def maxWidthRamp(A):
    counter = 0
    for i in A:
        if i > A[-1]:
            counter += 1
        else:
            res = len(A)-counter-1
            for c in range(-2, -counter-1, -1):
                newcounter = 0
                for i in A:
                    if i > A[c]:
                        newcounter += 1
                    else:
                        res = max(res, len(A)+c-newcounter)
                        break
            break
    return res

print(maxWidthRamp(A))