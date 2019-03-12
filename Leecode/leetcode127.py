import string
beginWord = "hit"
endWord = "dog"
wordList = ["hot","dot","dog","lot","log","cog","dit"]


def ladderLength(beginWord, endWord, wordList):
    wordDict = set(wordList)
    length = 2
    front, back = set([beginWord]), set([endWord])
    wordDict.discard(beginWord)
    while front:
        front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front
                            for index in range(len(beginWord)) for ch in string.ascii_lowercase))
        if front & back:
            return length
        length += 1
        if len(front) > len(back):
            front, back = back, front
        wordDict -= front
    return 0


print(ladderLength(beginWord, endWord, wordList))