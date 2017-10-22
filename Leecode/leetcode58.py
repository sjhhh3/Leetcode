myinput = " be a ed "

def lengthOfLastWord(s):
    if not s or s.isspace():
        return 0
    s = s.lstrip()
    sr = s[::-1].lstrip()
    if s.find(" ") == -1 or sr.find(" ") == -1:
        return len(sr)
    return sr.find(' ')



print(lengthOfLastWord(myinput))
print(myinput.split(' '))