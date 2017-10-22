'''
prices = [1, 3, 2, 8, 4, 9]
print(max(prices))
times = 1
profit = 0
maximum = 0
while profit >= 0:
    high = prices.index(max(prices))
    low = prices[0:max(prices)].index(min(prices))
    profit = prices[high] - prices[low] - 2
    if profit > maximum:
        maximum = profit
    break
print(profit,maximum)
'''
prices = [1, 3, 2, 8, 4, 9]
d = {}
i = 0
while i < len(prices):
    d[prices[i]] = i
    i += 1

maximum = max(d.items(), key=lambda x: x[1])
minimum = min(d.items(), key=lambda x: x[1])
profit = maximum[0] - minimum[0] - 2

print(profit)







