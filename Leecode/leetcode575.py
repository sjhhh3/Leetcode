candies = [1,1,2,2,3,3,4,5]

# lis = sorted(candies, key=lambda s: candies.count(s))
# lis = sorted(dic.items(), key=lambda i:i[1])

kind = set(candies)
print(min(len(kind), len(candies)//2))