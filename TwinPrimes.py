def Prime(num1):
    divisor = 2
    while divisor <= num1 / 2:
        if num1 % divisor == 0:

            return False # number is not a prime
        divisor += 1

    return True # number is prime


    for i in range(a, b):
        x=[]
        num1 = i
        num2 = i + 2
        if Prime(num1) and Prime(num2):
            print("(", num1, ",", num2, ")")
            


def twinprime(a,b):
    primes = [n for n in range(a,b) if Prime(n)]
    twins = [(p, p+2) for p in primes if p+2 in primes]
    return(twins)
print (twinprime(1,100))
