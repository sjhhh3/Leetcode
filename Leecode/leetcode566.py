nums = [[1, 2],
        [3, 4],[1, 2],
        [3, 4]]
r = 2
c = 4
res = []

if r * c != len(nums)*len(nums[0]):
    print(nums)

lis = sum(nums, [])

for row in range(r):
    newrow = []
    for column in range(c):
        newrow.append(lis.pop(0))
    res.append(newrow)
print(res)

