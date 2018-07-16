words = ["Hello", "Alaska", "Dad", "Peace"]
res = []
dic = {}

for i in 'qwertyuiop':
    dic[i] = 1
for i in 'asdfghjkl':
    dic[i] = 2
for i in 'zxcvbnm':
    dic[i] = 3

for word in words:
    take = 1
    row = dic[word.lower()[0]]
    for letter in word[1:]:
        if dic[letter.lower()] != row:
            take = 0
            break
    if take:
        res.append(word)
print(res)