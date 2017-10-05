# H1, H2, M1, M2
time = "00:31"
def nextClosestTime(time):
    H1 = time[0]
    H2 = time[1]
    M1 = time[3]
    M2 = time[4]
    nums = []
    list = []
    i = 0
    for num in time:
        if num.isdigit():
            nums += num

    for h1 in nums:
        for h2 in nums:
            if int(h1+h2) < 24:
                for m1 in nums:
                    if int(m1) < 6:
                        for m2 in nums:
                            list.append(int(h1+h2+m1+m2))

    list.sort()
    while i < len(list)-1:
        if list[i] == list[i+1]:
            list.remove(list[i+1])
        else:
            i += 1
    print(list)
    ori = int(H1+H2+M1+M2)
    if ori == 0:
        return "00:00"
    elif ori == list[-1]:
        output = str(list[0])
    elif list[list.index(ori)+1] < 100:
        output = str(list[list.index(ori) + 1])
        return '00' + ':' + output[0:2]
    elif list[list.index(ori)+1] < 1000:
        output = str(list[list.index(ori)+1])
        return '0'+output[0:1]+':'+output[1:3]
    else:
        output = str(list[list.index(ori)+1])
    return output[0:2]+':'+output[2:4]

print(nextClosestTime(time))














'''
if nums.index(M2) < 3 and nums[2] != nums[3]:
    M2 = nums[nums.index(M2)+1]
    print(H1+H2+':'+M1+M2)
elif nums[nums.index(M1)+1] < 6:
    M1 = nums[nums.index(M1)+1]
    print(H1+H2+':'+M1+M2)


print(H1,H2,M1,M2,nums)
'''