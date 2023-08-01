def getCollatzSequence(x):
    a=[]
    a.append(x)
    if x<0:
        return []
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            a.append(x)

        elif x % 2 == 1:
            x = x * 3 + 1
            a.append(x)
    return (a)
print(getCollatzSequence(20))

