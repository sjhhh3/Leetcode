matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

row = 0
while row < len(matrix)-1:
    if matrix[row][:-1] != matrix[row+1][1:]:
        print('false')
    row += 1
