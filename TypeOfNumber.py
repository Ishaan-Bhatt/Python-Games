
def sum_of_divisors(num):
    result=0
    for i in range(1,num):
        if(num%i)==0:
            result=result+i
    if result==num:
        return num


def type_of_number(num):
    result=0
    if num <0:
        return "invalid input"
    for i in range(1,num):
        if(num%i)==0:
            result=result+i
    if result==num:
        return ("perfect Number")
    elif result > num:
        return ("Abundant Number")
    elif result < num:
        return ("Deficient Number")
    

    
