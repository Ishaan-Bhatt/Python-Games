
def  get_reverse(num):
    if num<0:
        return -1
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    return (rev)    

def isPalindrome(num):
    new=get_reverse(num)
    

    if(num==new):
        return ( True)
    else:
        return (False)


def palindrome_sum(first,last):
    if first<0 or last<0:
        return -1
    elif first<last:
        return -2
    a=[]
    for i in range(first,last):
        if isPalindrome(i) in range(first,last)==0:
            return 0
        if(isPalindrome(i)):
            a.append(i)
    for j in a:
        b= (sum(list(a)))
        return (b)
print (palindrome_sum(60,60))      

    

