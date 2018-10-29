widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"

sum = 0
ans = [1,0]

for letter in S:

    if sum + widths[ord(letter) - 97] > 100:
        ans[0] += 1
        sum = widths[ord(letter) - 97]
    else:
        sum += widths[ord(letter) - 97]

    ans[1] = sum

print(ans)

