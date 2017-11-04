input1 = [0,0,0]

def isOneBitCharacter(bits):
    new = bits

    while len(new) > 3:
        if new[0] is 0:
            new = new[1:]
        else:
            new = new[2:]
    print(new)
    if new in [[1,1,0],[1,0,0],[0,0,0],[0,0],[0]]:
        return True
    else:
        return False


print(isOneBitCharacter(input1))