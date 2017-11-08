words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]


def longestWord(words):
    ansdic = {}
    finaldic = {}
    maxlist = []
    for word in words:
        ansdic[word] = len(word)
    max_value = max(ansdic.values())

    while len(max(ansdic, key=ansdic.get)) == max_value:
        words.remove(max(ansdic, key=ansdic.get))
        maxlist.append(max(ansdic, key=ansdic.get))
        ansdic.pop(max(ansdic, key=ansdic.get))
    print(maxlist)
    for listitem in maxlist:
        for word in words:
            if listitem.find(word) == 0:
                break
            maxlist.remove(listitem)
            break
    print(maxlist)
    for listitem in maxlist:
        for i in listitem:
            itemsum = ord(i)
            finaldic[listitem] = itemsum
    print(min(finaldic, key=finaldic.get))

print(longestWord(words))