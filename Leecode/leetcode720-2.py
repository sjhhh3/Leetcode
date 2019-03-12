words =  ["a", "banana", "app", "appl", "ap", "apply", "apple"]


def longestWord(words):
    valid = set([""])

    for word in sorted(words):
        if word[:-1] in valid:
            a = word[:-1]
            valid.add(word)
    return max(sorted(valid), key=lambda x: len(x))

print(longestWord(words))
