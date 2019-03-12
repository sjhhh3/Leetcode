area = [[1,1,1,1],[0,1,1,1],[0,1,0,1],[1,1,9,1],[0,0,1,1]]
ans = []

def dfs(area, i, j):
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[0]) or area[i][j] not in (1,9):
        return 0

    area[i][j] = "#"
    b = 0 or dfs(area, i + 1, j)
    t = 0 or dfs(area, i - 1, j)
    r = 0 or dfs(area, i, j + 1)
    l = 0 or dfs(area, i, j - 1)

    if area[i][j] == 9:
        ans.append(b+t+r+l+1)
        print('aaa')
        return b+t+r+l+1
    print(area)

print(dfs(area,0,0))
