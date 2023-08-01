def isArmstrong(n):
    a=(len(str(n)))
    var = n
    summ = 0
    while (var!=0):
        r = var%10
        summ += r**a
        var //=10
    if n ==summ:
        return True
       
    else:
        return False
print(isArmstrong(153))
    
