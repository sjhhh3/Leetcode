def plusOne(digits):
    diglen = 0
    sum = 0
    while diglen < len(digits):
        sum += digits[diglen] * (10 ** (len(digits)-1-diglen))
        diglen += 1
    ans = []
    sum += 1
    for i in str(sum):
        ans.append(int(i))
    return ans

print(plusOne([0]))