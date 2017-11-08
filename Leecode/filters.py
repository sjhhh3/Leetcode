import random
import timeit
data = [x for x in range(10)]
data2 = [random.randint(-10,10) for _ in range(10)]
data2filter = [item for item in filter(lambda x: x >= 0, data2)] #Python 3版本后filter返回值变为迭代器
iterationdata2 = [x for x in data2 if x >= 0] #简易的迭代函数for
print(data)
print(data2filter)
print(iterationdata2)

def iterationtest():
    iterationdata2 = [x for x in data2 if x >= 0]
    return iterationdata2

def filtertest():
    data2filter = [item for item in filter(lambda x: x >= 0, data2)]
    return data2filter

testinglist = []
def fortest():
    for number in data2:
        if number >= 0:
            testinglist.append(number)
    return testinglist

print("it " + str(timeit.timeit(stmt=iterationtest, number=1000000))) # 0.5600411338596614
print("for " + str(timeit.timeit(stmt=fortest, number=1000000))) #0.8092170344430891
print("ft " + str(timeit.timeit(stmt=filtertest, number=1000000))) # 1.4120394366731353

dic = {x: random.randint(60,100) for x in range(1,21)}
filtereddic = {k:v for k,v in dic.items() if v > 90}
print(dic)
print(filtereddic)

s = set(data2)
filteredset = {x for x in s if x % 3 == 0}
print(s)
print(filteredset)