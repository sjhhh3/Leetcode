A = [[1,2,3],[4,5,6]]

res = []

for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    res.append(row)
    print(res)