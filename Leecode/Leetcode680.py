input = ["5","-2","4","C","D","9","+","+"]
def calPoints(ops):
    output = 0
    arr = [0,0]

    for ops in input:
        if ops == "C":
            arr.pop()
        elif ops == "D":
            arr.append(int(arr[-1]) * 2)
        elif ops == "+":
            arr.append(int(arr[-1]) + int(arr[-2]))
        else:
            arr.append(int(ops))


    for num in arr:
        output += int(num)
    return output

print(calPoints(input))