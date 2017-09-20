
def isPalindrome(x):
    if x>=0:
        return True if str(x) == str(x)[::-1] else False
    else:
        return False

x = 121
print(isPalindrome(x))

'''
# Sample

    def isPalindrome(x):
        string = str(x)
        if string == string[::-1]:
            return True
        return False
'''