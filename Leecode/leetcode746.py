
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
min_cost0, min_cost1 = cost[0], cost[1]
for c in cost[2:]:
    min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + c
print(min(min_cost0, min_cost1))