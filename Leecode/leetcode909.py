def snakesAndLadders(board):
    n = len(board)
    need = {1: 0}
    bfs = [1]
    for x in bfs:
        for i in range(x + 1, x + 7):
            a, b = (i - 1) // n, (i - 1) % n
            nxt = board[~a][b if a % 2 == 0 else ~b]
            if nxt > 0: i = nxt
            if i == n * n:
                return need[x] + 1
            if i not in need:
                need[i] = need[x] + 1
                bfs.append(i)

    return -1

Input= [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(Input))