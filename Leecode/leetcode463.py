grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

# def delt(list):
#     i = 0
#     count = 0
#     while i < len(list)-1:
#         if list[i] and list[i+1]:
#             count += 1
#         i += 1
#     return count
#
# island = 0
# count = 0
# for row in grid:
#     island += row.count(1)
#     count += delt(row)
# for column in zip(*grid):
#     count += delt(column)
#
# print(island*4-count*2)



def water_around(y, x):
    print(y,x)
    print (
        y == len(grid) - 1 or (grid[y+1][x] == 0) )
    print ((x == 0              or grid[y][x-1] == 0),
            (x == len(grid[0])-1 or grid[y][x+1] == 0),
            (y == 0              or grid[y-1][x] == 0),
            (y == len(grid)-1    or grid[y+1][x] == 0) )

    return ((x == 0              or grid[y][x-1] == 0) +
            (x == len(grid[0])-1 or grid[y][x+1] == 0) +
            (y == 0              or grid[y-1][x] == 0) +
            (y == len(grid)-1    or grid[y+1][x] == 0) )
print(list(water_around(y, x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x]))