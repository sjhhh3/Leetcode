def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    states = [0] + states + [0]
    new = states[:]
    for _ in range(days):
        for i in range(1, len(states)-1):
            if states[i-1] == states[i+1]:
                new[i] = 0
            else:
                new[i] = 1
        states[:] = new
    return states

print(cellCompete([1,1,1,0,1,1,1,1], 2)[1:-1])