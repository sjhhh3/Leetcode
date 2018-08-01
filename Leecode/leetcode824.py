S = "I speak Goat Latin"
res = ""
a = 1
vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for word in S.split(' '):
    if word[0] in vowel:
        word += 'ma'
    else:
        word = word[1:] + word[0] + 'ma'
    word += "a" * a
    res += (word + " ")
    a += 1
print(res[:-1])

