words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]

def areSentencesSimilar(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    for i in range(len(words1)):
        listxp = [words1[i], words2[i]]
        listxq = [words2[i], words1[i]]
        if listxp in pairs or listxq in pairs or words1[i] == words2[i]:
            continue
        else:
            return False
    return True


print(areSentencesSimilar(words1,words2,pairs))