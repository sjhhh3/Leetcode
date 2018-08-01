S = "12345"

# Output: ["a1b2c", "a1B2c", "a1B2C", "a1b2C", "A1b2c", "A1b2C", "A1B2c", "A1B2C"]

#
def getLaU(st, ls):
    if not ls:
        return st
    res = []
    if not st:
        if ls[0].isdigit():
            res.append(st + ls[0])
        else:
            res.append(st + ls[0].lower())
            res.append(st + ls[0].upper())

    else:
        for i in st:
            if ls[0].isdigit():
                res.append(i + ls[0])
            else:
                res.append(i + ls[0].lower())
                res.append(i + ls[0].upper())
    return getLaU(res, ls[1:])

print(getLaU('', S))

