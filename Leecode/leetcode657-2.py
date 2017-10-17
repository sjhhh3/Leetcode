myinput = [1,2,2,3,1,4,2]
myinput2 = [1,3,1,2,2,2,1]

def findShortestSubArray(nums):
    start = {}
    end = {}
    lenth = {}
    times = {}
    exitlist = []
    m = 0
    while m < len(nums):
        if nums[m] not in exitlist:
            exitlist.append(nums[m])
            start[nums[m]] = m
            times[nums[m]] = 0
        end[nums[m]] = m

        if nums[m] in exitlist:
            times[nums[m]] += 1
        m += 1

    for key in start:
        lenth[key] = [times[key]]
        lenth[key] += [end[key]-start[key]+1]

    maxtimes = max(times.values())
    # print(times)
    # print(lenth)
    # print(maxtimes)
    # print(max(lenth.items(), key=lambda x: x[1]))

    minlist = []
    for key in lenth:
        if lenth[key][0] == maxtimes:
            minlist.append(lenth[key][1])
    return min(minlist)

print(findShortestSubArray(myinput))