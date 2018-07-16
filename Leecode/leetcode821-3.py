S = "loveleetcod"
C = 'e'

indexes = [i for i, x in enumerate(S) if x == C]

print(indexes)

distances = []
for i in range(len(S)):
    distances.append(min([abs(i - x) for x in indexes]))
print(distances)

# return [min([abs(i-j) for j in [k for k in range(len(S)) if S[k]==C]]) for i in range(len(S))]