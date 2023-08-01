def isPrime(num):
    if (num<=0):
        return "invalid input"
    elif (num==2):
        return True;
    else:
        for x in range(2,num):
            if(num % x==0):
                return False
        return True             
print(isPrime(20))
