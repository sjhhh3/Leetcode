myinput = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
list = []
max = 0
for x in range(len(myinput)):
    # print(myinput[x])
    for y in range(len(myinput[0])):
        # print(x,',',y,":",myinput[x][y])
        if myinput[x][y] == 1:
            list += [x+y]
print(list)
i = 0
while i < len(list)-1:
    if list[i] == list[i+1] or list[i] == list[i+1] + 1:

# xlist = []
# for point in list:
#     xlist += [point[0]]
# i = 1
# while i < len(xlist)-1:
#     if xlist[0] == xlist[i]:
#         print(i)
#     i += 1


