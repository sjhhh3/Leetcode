'''

def knightProbability(N, K, r, c):
    list = []
    positionR = r
    positionC = c
    able = 0
    if K > 0:
        if positionR - 2 >= 0 and positionC - 1 >= 0:
            able += 1
            list.append([positionR - 2, positionC - 1])
        if positionR - 1 >= 0 and positionC - 2 >= 0:
            able += 1

        if positionR + 1 <= N and positionC - 2 >= 0:
            able += 1
        if positionR + 2 <= N and positionC - 1 >= 0:
            able += 1

        if positionR + 2 <= N and positionC + 1 <= N:
            able += 1
        if positionR + 1 <= N and positionC + 2 <= N:
            able += 1

        if positionR - 1 >= 0 and positionC + 2 <= N:
            able += 1
        if positionR - 2 >= 0 and positionC + 1 <= N:
            able += 1

    answer = able/8
    return answer

print(knightProbability(3,1,0,0))
'''
list = []
list.append([3,2])
print(list)

