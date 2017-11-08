words =  ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]

def longestWord(words):
    words, resword, res = sorted(words), '', set()
    for word in words:
        if len(word) == 1 or word[:-1] in res:
            res.add(word)
            resword = word if resword == '' else word if len(word) > len(resword) else resword
    return resword


print(longestWord(words))