def combinationSum(nums, target):
    res = []
    nums.sort()

    def dfs(left, path, idx):
        if not left:
            res.append(path[:])
        else:
            for i, val in enumerate(nums[idx:]):
                if val > left: break
                dfs(left - val, path + [val], idx + i)

    dfs(target, [], 0)
    return res

print(combinationSum([2,3,6,7], 7))