num = 5
arr = [2,4,6,8,18]


def gcd(num1, num2):
    sm, lg = sorted([num1, num2])

    mo = lg % sm
    while mo != 0:


