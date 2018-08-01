num = 9999999999

def adding(number):
    if number < 10:
        return number
    res = 0
    for i in str(number):
        res += int(i)
    return adding(res)

print(adding(num))